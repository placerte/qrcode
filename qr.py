import argparse
from model import QRCode
from parser import QRCode_Parser

def main() -> None:

    parser: QRCode_Parser = QRCode_Parser()
    args: argparse.Namespace = parser.args 
    qr_code: QRCode = parser.qr_code

    if args.gui:
        from gui_app import QRCodeGeneratorGUI
        qr_gui: QRCodeGeneratorGUI = QRCodeGeneratorGUI(qr_code)
        qr_gui.launch()
        return
    else:
        from cli_app import QRCodeGeneratorCLI
        qr_cli = QRCodeGeneratorCLI = QRCodeGeneratorCLI(qr_code)
        qr_cli.launch()

if __name__ == "__main__":
    main()
