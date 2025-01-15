import argparse
from qrcode.main import QRCode
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont
from typing import Union

def generate_qr_code(title: str, url: str, print_title: bool, prefix: str) -> None:
    filename: str = prefix + title + ".png"

    # Generate QR code
    qr: QRCode = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create a new image with space for the text
    qr_img: Image.Image = qr.make_image(fill_color="black", back_color="white")

    if print_title:
        img: Image.Image = add_text_to_image(qr_img, title)
        img.save(filename)
    else:
        qr_img.save(filename)

    print(f"QR Code saved as {filename}")

def add_text_to_image(qr_img: Image.Image, title: str) -> Image.Image:
    qr_width: int
    qr_height: int
    qr_width, qr_height = qr_img.size
    img_width: int = qr_width
    img_height: int = qr_height + 50  # Add extra space for text
    img: Image.Image = Image.new('RGB', (img_width, img_height), color='white')

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
    draw.text(text_position, title, font=font, fill='black')

    return img

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Generate a QR Code with optional title.")
    parser.add_argument("--title", type=str, help="Title to display below the QR Code.")
    parser.add_argument("--url", type=str, help="URL to encode in the QR Code.")
    parser.add_argument("--print-title", action="store_true", help="Whether to display the title below the QR Code.")
    parser.add_argument("--prefix", type=str, default="QR Code - ", help="Filename prefix for the output image.")

    args: argparse.Namespace = parser.parse_args()

    title: str = args.title or input("Enter title: ")
    url: str = args.url or input("Enter URL: ")
    print_title: bool = args.print_title or input("Print title? (yes/no): ").strip().lower() == "yes"
    prefix: str = args.prefix

    generate_qr_code(title, url, print_title, prefix)

if __name__ == "__main__":
    main()

