# CLI app
from model import QRCode

class QRCodeGeneratorCLI():

    qr_code: QRCode

    def __init__(self, qr_code: QRCode):
        self.qr_code = qr_code

    def launch(self):
        title: str = self.qr_code.title or input("Enter title: ")
        url: str = self.qr_code.url or input("Enter URL: ")
        print_title: bool = self.qr_code.print_title or input(
            "Print title? [Y/n]: "
        ).strip().lower() in ["", "y", "yes"]
        prefix: str = self.qr_code.prefix

        print("yeah")
