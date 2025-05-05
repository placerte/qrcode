# CLI app
import argparse
from defaults import DefaultsFileManagent as dfm
from logic import *

def get_parser()->argparse.ArgumentParser:
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

class QRCodeGeneratorCLI():

    args: argparse.Namespace

    def __init__(self, args: argparse.Namespace):
        self.args = args

    def main(self):
        title: str = self.args.title or input("Enter title: ")
        url: str = self.args.url or input("Enter URL: ")
        print_title: bool = self.args.print_title or input(
            "Print title? [Y/n]: "
        ).strip().lower() in ["", "y", "yes"]
        prefix: str = self.args.prefix

        generate_qr_code_image(title, url, print_title, prefix)
    
