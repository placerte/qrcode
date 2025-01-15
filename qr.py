from qrcode.main import QRCode, GenericImage
from qrcode import constants
from PIL import Image, ImageDraw, ImageFont


title : str = "Charleston 1 - Hiver 2025 - Ariane et Pierre"
url : str = "https://www.facebook.com/share/g/18YMvk1xgp/"
print_title : bool = True


prefix : str = "QR Code - "
filename : str = prefix + title + ".png"

# Generate QR code
qr : QRCode = QRCode(version=1,
                    error_correction=constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create a new image with space for the text
qr_img : GenericImage = qr.make_image(fill_color="black", back_color="white")

if print_title:

    qr_width, qr_height = qr_img.size
    img_width = qr_width
    img_height = qr_height + 50  # Add extra space for text
    img = Image.new('RGB', (img_width, img_height), color='white')

    # Paste the QR code onto the new image
    img.paste(qr_img, (0, 0))

    # Add text
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)  # Adjust font and size as needed
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_position = ((img_width - text_width) // 2, qr_height + 10)
    draw.text(text_position, title, font=font, fill='black')

    # Save the image
    img.save(filename)

else:

    qr_img.save(filename)

