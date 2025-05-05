import argparse
from qrcode.main import QRCode as QRCodeBase
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont
from typing import Union
import os
from defaults import DefaultsFileManagent as dfm

class QRCode():

    title: str
    url: str
    print_title: bool
    prefix: str
    output_dir: str

    #def __init__(self, args: argparse.Namespace) -> None:

    @property
    def filepath(self)->str:
        return self.output_dir + self.prefix + self.title + ".png"
    
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
    def qr_code_image(self)->Image.Image:

        # Create a new image with space for the text
        qr_img: Image.Image = self.__qr_code_base.make_image(fill_color="black", back_color="white")

        # Manage title printing
        if self.print_title:
            qr_img = self.__add_title_to_image(qr_img)


        return qr_img

    def save_image(self):

        # Manage output directory
        self.__manage_output_directory()

        self.qr_code_image.save(self.filepath)

        #TODO: move to cli app
        print(f"QR Code saved as {filepath}")

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

    def get_arg_parser(self)->argparse.ArgumentParser:
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description="Generate a QR Code with optional title."
        )
        parser.add_argument("--title", type=str, help="Title to display below the QR Code.")
        parser.add_argument("--url", type=str, help="URL to encode in the QR Code.")
        parser.add_argument(
            "--print-title",
            action="store_true",
            help="Whether to display the title below the QR Code.",
        )
        parser.add_argument(
            "--prefix",
            type=str,
            default=dfm.FILE_PREFIX,
            help="Filename prefix for the output image.",
        )
        parser.add_argument("--gui", action="store_true", help="Lauches GUI instead of CLI")

        return parser
