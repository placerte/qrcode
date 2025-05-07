import argparse
from model import QRCode
from defaults import DefaultsFileManagent as dfm

class QRCode_Parser():

    qr_code: QRCode
    args: argparse.Namespace

    def __init__(self) -> None:
        self.args = self._build_parser().parse_args()
        self.qr_code = QRCode(
            title = self.args.title,
            url = self.args.url,
            prefix = self.args.prefix,
            print_title = self.args.print_title,
            output_dir = self.args.output_dir
        )


    def _build_parser(self)->argparse.ArgumentParser:
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            description="Generate a QR Code with optional title."
        )
        parser.add_argument("--title", type=str, help="Title to display below the QR Code.")
        parser.add_argument("--url", type=str, help="URL to encode in the QR Code.")
        parser.add_argument(
            "--print-title",,
            action="store_true",
            help="Whether to display the title below the QR Code.",
        )
        parser.add_argument(
            "--prefix",
            type=str,
            default=dfm.FILE_PREFIX,
            help="Filename prefix for the output image.",
        )

        parser.add_argument(
            "--output-dir",
            type=str,
            default=dfm.OUTPUT_DIR_PATH,
            help="Specify the default output directory"
        )

        parser.add_argument("--gui", action="store_true", help="Lauches GUI instead of CLI")

        return parser
