import argparse
from model import QRCode
from defaults import DefaultsFileManagent as dfm

class QRCode_Parser():

    qr_code: QRCode

    def __init__(self) -> None:
        self.qr_code = QRCode()


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

        parser.add_argument(
            "--output-dir",
            type=str,
            default=dfm.OUTPUT_DIR_PATH,
            help="Specify the default output directory"
        )

        parser.add_argument("--gui", action="store_true", help="Lauches GUI instead of CLI")

        self.__populate_qr_code(parser.parse_args())

        return parser

    def __populate_qr_code(self, args: argparse.Namespace):
        self.qr_code.title = args.title
        self.qr_code.url = args.url
        self.qr_code.prefix = args.prefix
        self.qr_code.print_title = args.print_title
        self.qr_code.output_dir = args.output_dir

