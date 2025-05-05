import argparse
from cli_app import get_parser
import argparse

def main() -> None:

    args: argparse.Namespace = get_parser().parse_args()

    if args.gui:
        from gui_app import QRCodeGeneratorGUI
        qr_gui: QRCodeGeneratorGUI = QRCodeGeneratorGUI()
        qr_gui.launch()
        return
    else:
        from cli_app import QRCodeGeneratorCLI
        qr_cli = QRCodeGeneratorCLI = QRCodeGeneratorCLI(args)
        qr_cli.main()

if __name__ == "__main__":
    main()
