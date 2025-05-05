import argparse
from qrcode.main import QRCode
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont
from typing import Union
import os
from defaults import DefaultsFileManagent as dfm


def generate_qr_code_image(title: str, url: str, print_title: bool, prefix: str):

    # Generate filepath
    filepath: str = generate_filepath(title=title, prefix=prefix)

    # Generate QR code
    qr_code: QRCode = generate_qr_code(url=url)

    # Create a new image with space for the text
    qr_img: Image.Image = qr_code.make_image(fill_color="black", back_color="white")

    # Manage title printing
    if print_title:
        qr_img = add_text_to_image(qr_img, title)

    # Manage output directory
    manage_output_directory()

    qr_img.save(filepath)

    print(f"QR Code saved as {filepath}")


# TODO: refactor to put output dir as an argument
def generate_filepath(title: str, prefix: str) -> str:

    filepath: str = dfm.OUTPUT_DIR_PATH + prefix + title + ".png"
    return filepath


def generate_qr_code(url: str) -> QRCode:
    qr: QRCode = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    return qr


def add_text_to_image(qr_img: Image.Image, title: str) -> Image.Image:
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

    bbox: tuple[int, int, int, int] = draw.textbbox((0, 0), title, font=font)
    text_width: int = bbox[2] - bbox[0]
    text_height: int = bbox[3] - bbox[1]
    text_position: tuple[int, int] = ((img_width - text_width) // 2, qr_height + 10)
    draw.text(text_position, title, font=font, fill="black")

    return img


def manage_output_directory(output_dir: str):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def main() -> None:
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

    args: argparse.Namespace = parser.parse_args()

    if args.gui:
        qr_gui: QRCodeGeneratorGUI = QRCodeGeneratorGUI()
        qr_gui.launch()
        return

    title: str = args.title or input("Enter title: ")
    url: str = args.url or input("Enter URL: ")
    print_title: bool = args.print_title or input(
        "Print title? [Y/n]: "
    ).strip().lower() in ["", "y", "yes"]
    prefix: str = args.prefix

    generate_qr_code_image(title, url, print_title, prefix)


if __name__ == "__main__":
    main()
