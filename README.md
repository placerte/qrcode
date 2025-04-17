# Simple QR Code Generator

## Description

A simple QR code generator CLI app, wrapper of the [QRCode class](https://pypi.org/project/qrcode/), written in Python.
*(if you don't trust the free websites QR code generator ;))*


## Installation

Not packaged in any meaningful way for now so it **requires Python 3.1x** and **git** to be installed on the machine.

1. Clone the git repo locally
    ```bash
    git clone https://github.com/placerte/qrcode.git
    ```
1. Create a virtual environnement (venv or other)
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
    .venv activation will differ depending on the machine OS
1. Intall *requirements.txt*
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Launch the app from the local repo in your terminal using
```bash
python qr.py
```
1. Follow the instructions in the terminal (Provide url and a title)
1. File will be exported in the local repo in a directory named **output**.


## TODO / Wish List

- [ ] Package the app in a bin for broader public
- [ ] Implement a simple GUI
- [ ] Provide better documentation for the arguments / usage in the README 
