import argparse

from qrcode_generator import __version__
from qrcode_generator.model import QRCode
from qrcode_generator.defaults import DefaultsFileManagent as dfm


class QRCode_Parser:
    qr_code: QRCode
    args: argparse.Namespace

    def __init__(self) -> None:
        self.args = self._build_parser().parse_args()
        self.qr_code = QRCode(
            title=self.args.title,
            url=self.args.url,
            file_prefix=self.args.file_prefix,
            print_title=not self.args.no_title,
            output_dir=self.args.output_dir,
        )

    def _build_parser(self) -> argparse.ArgumentParser:
        class _HelpFormatter(
            argparse.ArgumentDefaultsHelpFormatter,
            argparse.RawDescriptionHelpFormatter,
        ):
            pass

        description: str = (
            "Generate a QR Code as a PNG image. If an option is omitted, the CLI "
            "prompts for it."
        )
        epilog: str = (
            "Examples:\n"
            "  qrcode --url https://example.com --title Example\n"
            "  qrcode --url https://example.com --no-title\n"
            "  qrcode --gui\n"
            "  qrcode --output-dir ./output/ --file-prefix QRCode-\n"
            "  qrcode --batch-file ./examples/urls.txt\n"
        )
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            prog="qrcode",
            description=description,
            epilog=epilog,
            formatter_class=_HelpFormatter,
        )
        parser.add_argument(
            "--version",
            action="version",
            version=f"qrcode {__version__}",
            help="Show the qrcode version and exit.",
        )

        parser.add_argument(
            "--title",
            type=str,
            metavar="TITLE",
            help="Title to display below the QR code.",
        )
        parser.add_argument(
            "--url",
            type=str,
            metavar="URL",
            help="URL to encode in the QR code.",
        )
        parser.add_argument(
            "--no-title",
            action="store_true",
            help="Do not render the title under the QR code.",
        )
        parser.add_argument(
            "--file-prefix",
            type=str,
            metavar="PREFIX",
            default=dfm.FILE_PREFIX,
            help="Filename prefix for the output image.",
        )

        parser.add_argument(
            "--output-dir",
            type=str,
            metavar="DIR",
            default=dfm.OUTPUT_DIR_PATH,
            help="Output directory path (include trailing slash).",
        )

        parser.add_argument(
            "--gui",
            action="store_true",
            help="Launch the GUI instead of CLI prompts.",
        )

        parser.add_argument(
            "--batch-file",
            type=str,
            metavar="PATH",
            help=(
                "Read URLs from a text file (one per line). Optional title can be "
                "included in parentheses. Lines starting with # are ignored."
            ),
        )

        return parser
