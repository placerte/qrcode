import argparse
import os
import re
import sys
from typing import Iterable, List, Optional, Tuple
from urllib.parse import urlparse

if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from qrcode_generator.model import QRCode
from qrcode_generator.parser import QRCode_Parser


def main() -> None:
    parser: QRCode_Parser = QRCode_Parser()
    args: argparse.Namespace = parser.args
    qr_code: QRCode = parser.qr_code

    if args.batch_file and args.gui:
        print("Batch mode is not supported with --gui.")
        return

    if args.batch_file:
        _process_batch_file(
            args.batch_file,
            output_dir=qr_code.output_dir,
            file_prefix=qr_code.file_prefix,
        )
        return

    if args.gui:
        from qrcode_generator.gui_app import QRCodeGeneratorGUI

        qr_gui: QRCodeGeneratorGUI = QRCodeGeneratorGUI(qr_code)
        qr_gui.mainloop()
        return
    else:
        from qrcode_generator.cli_app import QRCodeGeneratorCLI

        qr_cli = QRCodeGeneratorCLI = QRCodeGeneratorCLI(qr_code)
        qr_cli.launch()


if __name__ == "__main__":
    main()


def _process_batch_file(batch_path: str, output_dir: str, file_prefix: str) -> None:
    try:
        with open(batch_path, "r", encoding="utf-8") as batch_file:
            lines: Iterable[str] = batch_file.readlines()
    except OSError:
        print(f"Could not read batch file: {batch_path}")
        return

    entries: List[Tuple[str, Optional[str]]] = _parse_batch_lines(lines)
    if not entries:
        print("No valid entries found in batch file.")
        return

    for url, title in entries:
        resolved_title: str
        print_title: bool = bool(title)
        if title:
            resolved_title = title
        else:
            resolved_title = _fallback_title_from_url(url)

        qr_code = QRCode(
            title=resolved_title,
            print_title=print_title,
            url=url,
            file_prefix=file_prefix,
            output_dir=output_dir,
        )
        try:
            qr_code.save_image()
        except OSError:
            print(f"Failed to save QR code for: {url}")


def _parse_batch_lines(lines: Iterable[str]) -> List[Tuple[str, Optional[str]]]:
    entries: List[Tuple[str, Optional[str]]] = []
    for line in lines:
        stripped: str = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        match = re.match(r"^(.*?)\s*\((.*)\)\s*$", stripped)
        if match:
            url = match.group(1).strip()
            title = match.group(2).strip() or None
        else:
            url = stripped
            title = None

        if not url:
            continue

        entries.append((url, title))

    return entries


def _fallback_title_from_url(url: str) -> str:
    parsed = urlparse(url)
    base: str = parsed.netloc or parsed.path or url
    base = base.strip().strip("/")
    if not base:
        return "untitled"

    base = re.sub(r"[^A-Za-z0-9._-]+", "_", base)
    return base or "untitled"
