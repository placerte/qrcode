# CLI app
import argparse
from defaults import DefaultsFileManagent as dfm
from logic import *

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
    
