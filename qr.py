import argparse
from model import QRCode

def main() -> None:

    qr_code: QRCode = QRCode()
    args: argparse.Namespace = qr_code.get_arg_parser().parse_args()

    if args.gui:
        from gui_app import QRCodeGeneratorGUI
        qr_gui: QRCodeGeneratorGUI = QRCodeGeneratorGUI(qr_code)
        qr_gui.launch()
        return
    else:
        from cli_app import QRCodeGeneratorCLI
        qr_cli = QRCodeGeneratorCLI = QRCodeGeneratorCLI(qr_code)
        qr_cli.main()

if __name__ == "__main__":
    main()
