# CLI app
from qrcode_generator.model import QRCode


class QRCodeGeneratorCLI:
    qr_code: QRCode

    def __init__(self, qr_code: QRCode):
        self.qr_code = qr_code

    def launch(self):
        self.set_missing_variables()
        self.qr_code.save_image()

    def set_missing_variables(self):
        self.qr_code.title = self.qr_code.title or input("Enter title: ")
        self.qr_code.url = self.qr_code.url or input("Enter URL: ")
        self.qr_code.print_title = self.qr_code.print_title or input(
            "Print title? [Y/n]: "
        ).strip().lower() in ["", "y", "yes"]
        self.qr_code.file_prefix = self.qr_code.file_prefix or input(
            "Enter file prefix (optional): "
        )
