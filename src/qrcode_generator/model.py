import os
from typing import Optional, Sequence, Tuple, Union

from qrcode import constants
from qrcode.main import QRCode as QRCodeBase
from PIL import Image, ImageDraw, ImageFont

_FONT_FALLBACK_WARNED = False


class QRCode:
    BOX_SIZE: int = 10
    BORDER: int = 4

    title: str
    url: str
    print_title: bool
    file_prefix: str
    output_dir: str

    @property
    def filepath(self) -> str:
        if (
            self.title is not None
            and self.output_dir is not None
            and self.file_prefix is not None
        ):
            return self.output_dir + self.file_prefix + self.title + ".png"
        else:
            return ""

    @property
    def __qr_code_base(self) -> QRCodeBase:
        qr: QRCodeBase = QRCodeBase(
            version=1,
            error_correction=constants.ERROR_CORRECT_L,
            box_size=self.BOX_SIZE,
            border=self.BORDER,
        )
        qr.add_data(self.url)
        qr.make(fit=True)

        return qr

    @property
    def image(self) -> Image.Image:
        # Create a new image with space for the text
        qr_img: Image.Image = self.__qr_code_base.make_image(
            fill_color="black", back_color="white"
        )

        # Manage title printing
        if self.print_title and self.title:
            qr_img = self._add_title_to_image(qr_img)

        return qr_img

    def __init__(
        self, title: str, print_title: bool, url: str, file_prefix: str, output_dir: str
    ) -> None:
        self.title = title
        self.print_title = print_title
        self.url = url
        self.file_prefix = file_prefix
        self.output_dir = output_dir

    def save_image(self):
        # Manage output directory
        self.__manage_output_directory()

        self.image.save(self.filepath)

        # TODO: move to cli app
        print(f"QR Code saved as {self.filepath}")

    def _add_title_to_image(self, qr_img: Image.Image) -> Image.Image:
        qr_width: int
        qr_height: int
        qr_width, qr_height = qr_img.size
        img_with_text_width: int = qr_width
        quiet_zone: int = self.BORDER * self.BOX_SIZE
        horizontal_padding: int = 4
        vertical_padding: int = 10
        available_width: int = max(
            1, img_with_text_width - (quiet_zone * 2) - (horizontal_padding * 2)
        )

        font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont]
        font, text_bbox = self._fit_title_font(self.title, available_width)
        text_width: int = text_bbox[2] - text_bbox[0]
        text_height: int = text_bbox[3] - text_bbox[1]
        img_with_text_height: int = qr_height + text_height + (vertical_padding * 2)

        # Paste the QR code onto the new image
        qr_img = qr_img.convert("RGB")
        try:
            img_with_text: Image.Image = Image.new(
                "RGB", (img_with_text_width, img_with_text_height), color="white"
            )
            img_with_text.paste(qr_img, (0, 0))
        except OSError:
            print("Could not paste the image (_add_title_to_image)")
            return qr_img

        # Add text
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(img_with_text)
        text_left: int = (
            quiet_zone + horizontal_padding + ((available_width - text_width) // 2)
        )
        text_position: tuple[int, int] = (
            text_left - text_bbox[0],
            qr_height + vertical_padding - text_bbox[1],
        )
        draw.text(text_position, self.title, font=font, fill="black")

        return img_with_text

    def _fit_title_font(
        self, text: str, max_width: int
    ) -> Tuple[
        Union[ImageFont.FreeTypeFont, ImageFont.ImageFont], Tuple[int, int, int, int]
    ]:
        font_paths: Sequence[str] = self._candidate_font_paths()
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(Image.new("RGB", (1, 1)))

        font: Optional[Union[ImageFont.FreeTypeFont, ImageFont.ImageFont]] = None
        selected_font_path: Optional[str] = None
        for font_path in font_paths:
            try:
                font = ImageFont.truetype(font_path, 12)
                selected_font_path = font_path
                break
            except OSError:
                continue

        if font is None:
            self._warn_font_fallback("Default bitmap font used: no TTF found.")
            font = ImageFont.load_default()
            text_bbox = self._measure_text_bbox(draw, text, font)
            return font, text_bbox

        if selected_font_path is None:
            self._warn_font_fallback("Default bitmap font used: no TTF found.")
            font = ImageFont.load_default()
            text_bbox = self._measure_text_bbox(draw, text, font)
            return font, text_bbox

        min_size: int = 6
        min_font: ImageFont.FreeTypeFont = ImageFont.truetype(
            selected_font_path, min_size
        )
        min_bbox: Tuple[int, int, int, int] = self._measure_text_bbox(
            draw, text, min_font
        )
        min_width: int = min_bbox[2] - min_bbox[0]
        while min_width > max_width and min_size > 1:
            min_size -= 1
            min_font = ImageFont.truetype(selected_font_path, min_size)
            min_bbox = self._measure_text_bbox(draw, text, min_font)
            min_width = min_bbox[2] - min_bbox[0]

        max_size: int = max(min_size, max_width)
        best_font: ImageFont.FreeTypeFont = ImageFont.truetype(
            selected_font_path, min_size
        )
        best_bbox: Tuple[int, int, int, int] = min_bbox

        low: int = min_size
        high: int = max_size
        while low <= high:
            mid: int = (low + high) // 2
            candidate: ImageFont.FreeTypeFont = ImageFont.truetype(
                selected_font_path, mid
            )
            bbox: Tuple[int, int, int, int] = self._measure_text_bbox(
                draw, text, candidate
            )
            width: int = bbox[2] - bbox[0]
            if width <= max_width:
                best_font = candidate
                best_bbox = bbox
                low = mid + 1
            else:
                high = mid - 1

        return best_font, best_bbox

    def _measure_text_bbox(
        self, draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont
    ) -> Tuple[int, int, int, int]:
        return draw.textbbox((0, 0), text, font=font)

    def _candidate_font_paths(self) -> Sequence[str]:
        pil_dir: str = os.path.dirname(ImageFont.__file__)
        return [
            os.path.join(pil_dir, "fonts", "DejaVuSans.ttf"),
            "DejaVuSans.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/Library/Fonts/Arial.ttf",
            "C:\\Windows\\Fonts\\arial.ttf",
        ]

    def _warn_font_fallback(self, message: str) -> None:
        global _FONT_FALLBACK_WARNED
        if _FONT_FALLBACK_WARNED:
            return
        _FONT_FALLBACK_WARNED = True
        print(message)

    def __manage_output_directory(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
