from qrcode.main import QRCode as QRCodeBase
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont
from typing import Union
import os
from defaults import DefaultsFileManagent as dfm


class QRCode:

    title: str
    url: str
    print_title: bool
    file_prefix: str
    output_dir: str

    @property
    def filepath(self) -> str:
        return self.output_dir + self.file_prefix + self.title + ".png"

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
        if self.print_title:
            qr_img = self.__add_title_to_image(qr_img)

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

    def __add_title_to_image(self, qr_img: Image.Image) -> Image.Image:
        qr_width: int
        qr_height: int
        qr_width, qr_height = qr_img.size
        img_width: int = qr_width
        img_height: int = qr_height + 50  # Add extra space for text
        img: Image.Image = Image.new("RGB", (img_width, img_height), color="white")

        # Paste the QR code onto the new image
        img.paste(qr_img, (0, 0))

        # Add text
        draw: ImageDraw.ImageDraw = ImageDraw.Draw(img)

        font: Union[ImageFont.FreeTypeFont, ImageFont.ImageFont]
        try:
            font = ImageFont.truetype("arial.ttf", 20)  # Adjust font and size as needed
        except OSError:
            print("Default font used: arial.ttf not found.")
            font = ImageFont.load_default()

        bbox: tuple[int, int, int, int] = draw.textbbox((0, 0), self.title, font=font)
        text_width: int = bbox[2] - bbox[0]
        text_height: int = bbox[3] - bbox[1]
        text_position: tuple[int, int] = ((img_width - text_width) // 2, qr_height + 10)
        draw.text(text_position, self.title, font=font, fill="black")

        return img

    def __manage_output_directory(self):

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
