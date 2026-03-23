# Simple QR Code Generator

Generate QR codes from the CLI or a small Tkinter GUI. Output images are saved
as PNG files in `./output/` by default.

Changelog: `CHANGELOG.md`

## Installation

### Option A: Pre-built binary (recommended when available)

Download the latest release binary and put it on your PATH.

Linux example:

```bash
curl -L -o qrcode \
  https://github.com/placerte/qrcode/releases/latest/download/qrcode-linux-x86_64

chmod +x qrcode
sudo mv qrcode /usr/local/bin/qrcode
```

Windows and macOS builds follow the same pattern with the appropriate filename.

### Option B: Run from source with `uv` (Python 3.9+)

```bash
git clone https://github.com/placerte/qrcode.git
cd qrcode
uv sync
```

You can then run the entry point with:

```bash
uv run qrcode --help
```

### Option C: Run from source with `venv` + `pip` (Python 3.9+)

```bash
git clone https://github.com/placerte/qrcode.git
cd qrcode
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You can then run the entry point with:

```bash
python -m qrcode_generator.qr --help
```

## Typical usage

Basic CLI:

```bash
qrcode --url https://example.com --title "Example"
```

Basic CLI from source:

```bash
uv run qrcode --url https://example.com --title "Example"
```

No title:

```bash
qrcode --url https://example.com --no-title
```

Custom output directory and filename prefix:

```bash
qrcode --url https://example.com --title "Example" --output-dir ./output --file-prefix Demo-
```

GUI mode:

```bash
qrcode --gui
```

Batch file mode:

```bash
qrcode --batch-file ./examples/urls.txt
```

Batch file format rules:
- One URL per line
- Optional title in parentheses: `https://example.com (Example title)`
- Lines starting with `#` are ignored
- If no title is provided, the QR is generated without a printed title and the
  filename is derived from the URL

## Build (PyInstaller)

Install build dependencies:

```bash
uv sync --extra dev
```

Use a Python 3.12 virtualenv when building the binary. Current PyInstaller
support for Python 3.13 is not reliable for this app, and the resulting
executable can crash on launch.

Build a single-file executable:

```bash
uv run --group dev pyinstaller qrcode.spec
```

The executable will be in `dist/`.

## Development

Run tests:

```bash
uv run pytest
```

Formatting is optional and intentionally not pinned in project metadata. If you want to use `black`, install or run it separately in your own environment.

Optional dump tooling is intentionally not pinned in the project metadata. If you want to use `produm` for one-off repository dumps, install or run it separately in your own environment.

## Notes

- Output files are saved to `./output/` by default.
- CLI prompts appear when required values are missing.
- The GUI updates the preview live when fields change.
- Titles are rendered with the best available TrueType font on the system.
  If none is found, Pillow falls back to a basic bitmap font and the title may
  look rough.

## TODO / Wish List

- [ ] Package the app in a bin for broader public
  - [ ] Verify licence compliance of packages
- [x] Implement a simple GUI
- [x] Provide better documentation for the arguments / usage in the README
- [x] Finish the parser refactor
- [ ] Improve the CLI app ergonomics further
