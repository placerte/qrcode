from qrcode.main import QRCode as QRCodeBase
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont
from typing import Union
import os

class QRCode:

    title: str
    url: str
    print_title: bool
    file_prefix: str
    output_dir: str

    @property
    def filepath(self) -> str:
        if (
                self.title is not None and
                self.output_dir is not None and
                self.file_prefix is not None
                ):
            return self.output_dir + self.file_prefix + self.title + ".png"
        else:
            return ""

    @property
    def __qr_code_base(self) -> QRCodeBase:
        qr: QRCodeBase = QRCodeBase(
            version=1,
            error_correction=constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
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
        img_with_text_height: int = qr_height + 50  # Add extra space for text
        img_with_text: Image.Image = Image.new("RGB", (img_with_text_width, img_with_text_height), color="white")

        # Paste the QR code onto the new image
        qr_img = qr_img.convert("RGB")
        try:
            img_with_text.paste(qr_img, (0, 0))
        except:
            print("Could not paste the image (_add_title_to_image)")

        # Add text
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(img_with_text)

        font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont]
        try:
            font = ImageFont.truetype("arial.ttf", 20)  # Adjust font and size as needed
        except OSError:
            print("Default font used: arial.ttf not found.")
            font = ImageFont.load_default()

        bbox: tuple[int, int, int, int] = draw.textbbox((0, 0), self.title, font=font)
        text_width: int = bbox[2] - bbox[0]
        text_height: int = bbox[3] - bbox[1]
        text_position: tuple[int, int] = ((img_with_text_width - text_width) // 2, qr_height + 10)
        draw.text(text_position, self.title, font=font, fill="black")

        return img_with_text

    def __manage_output_directory(self):

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
