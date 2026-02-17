# AGENTS.md
# Guidance for agentic coding assistants working in this repo.

# Project snapshot
# - Simple QR code generator with CLI and Tkinter GUI.
# - Source is in `src/qrcode_generator`.
# - Dependencies are lightweight (qrcode + pillow).

# Repo rules
# - No Cursor rules found in `.cursor/rules/` or `.cursorrules`.
# - No GitHub Copilot instructions found in `.github/copilot-instructions.md`.

# Environment setup
# - Python: 3.8+ (README mentions 3.1x; pyproject requires >=3.8).
# - Create venv: `python -m venv .venv`
# - Activate: `source .venv/bin/activate`
# - Install deps: `pip install -r requirements.txt`

# Build / lint / test commands
# - Build (PyInstaller): `pyinstaller pyinstaller.spec`
# - Lint: none configured.
# - Format: none configured.
# - Tests: none configured.
# - Single test: not applicable (no test runner or tests in repo).
#
# If you add tooling, document it here and mirror any new commands in README.

# Dependency management
# - Runtime deps are pinned in `requirements.txt` and mirrored in `pyproject.toml`.
# - Dev/build deps live in `pyproject.toml` optional extras (e.g., `dev`).
# - If you add a dependency, update `requirements.txt` and reflect it in README.
# - Avoid adding heavy libraries; keep the app lightweight.

# Run commands (manual verification)
# - CLI app: `python src/qrcode_generator/qr.py`
# - GUI app: `python src/qrcode_generator/qr.py --gui`
# - Output dir defaults to `./output/` (created if missing).

# CLI/GUI workflow expectations
# - CLI prompts should remain short and clear.
# - GUI should update preview and filepath when fields change.
# - Save action should always create the output directory if missing.

# Layout and entry points
# - `src/qrcode_generator/qr.py` is the main entry point.
# - `src/qrcode_generator/cli_app.py` implements CLI prompts.
# - `src/qrcode_generator/gui_app.py` implements Tkinter GUI.
# - `src/qrcode_generator/model.py` handles QR creation and image output.
# - `src/qrcode_generator/parser.py` handles argparse CLI args.
# - `src/qrcode_generator/defaults.py` contains UI and filesystem defaults.

# Code style guidelines
# These reflect current patterns in the codebase.

# Formatting
# - Use 4-space indentation.
# - Keep blank lines between methods and logical sections.
# - Line length is not enforced; prefer PEP 8 style when editing.
# - No formatter is configured; avoid reformatting unrelated lines.
# - Avoid trailing whitespace and keep file-level spacing consistent.

# Imports
# - Follow standard order when possible:
#   1) standard library
#   2) third-party
#   3) local modules
# - Existing modules use local imports like `from model import QRCode`.
#   Keep the local import style consistent within this package.
# - Avoid wildcard imports.
# - Keep Tkinter imports grouped (`import tkinter as tk`, `from tkinter import ttk`).

# Naming conventions
# - Classes: PascalCase (e.g., `QRCodeGeneratorGUI`).
# - Functions/methods: snake_case (e.g., `_update_image_widget`).
# - Constants: ALL_CAPS (e.g., `FILE_PREFIX`).
# - Private helpers use a single leading underscore.
# - Avoid double-underscore for new methods unless name-mangling is intended.

# Types and typing
# - Type hints are used for class attributes and variables.
# - Prefer explicit types for public methods and class attributes.
# - Use `typing.Union` or `|` only where needed; keep annotations simple.
# - Avoid introducing heavy typing frameworks unless required.
# - Use concrete types for Tk variables where possible (StringVar/BooleanVar).

# Error handling
# - Current code uses simple `try/except` with `print` for user feedback.
# - Prefer specific exceptions (`except OSError:`) over bare `except:`.
# - For CLI/GUI flows, `print`-based errors are acceptable.
# - For library-like helpers, raise exceptions rather than swallowing them.
# - Keep error messages user-facing and short.

# Data and I/O
# - Output directory is created if missing (`os.makedirs`).
# - File paths are concatenated as strings; keep behavior stable.
# - Image operations use PIL (Pillow) and qrcode library.
# - Preserve output filename format: `<output_dir><file_prefix><title>.png`.
# - Avoid changing defaults without updating `defaults.py`.

# CLI behavior
# - argparse is used in `QRCode_Parser`.
# - Keep existing flag names; add new flags carefully to avoid breaking.
# - `--gui` switches from CLI to GUI.

# GUI behavior
# - Tkinter is used with `ttk` widgets.
# - UI state lives in Tk variables (StringVar/BooleanVar).
# - Update UI labels and image widgets when state changes.
# - Keep references to `PhotoImage` on the instance to avoid garbage collection.
# - Layout uses grid/pack with padding constants from `DefaultsUI`.

# File structure conventions
# - Keep new modules inside `src/qrcode_generator`.
# - Avoid adding top-level scripts unless documented in README.
# - Update `defaults.py` for new configurable defaults.
# - Keep output assets in `output/` (generated at runtime).

# Testing guidance
# - No test suite exists; use manual verification:
#   - Generate QR code with and without title.
#   - Verify output file path and image contents.
#   - Check GUI updates when fields change.
# - If you add tests, prefer pytest and document single-test command:
#   `pytest -k <pattern>` or `pytest path/to/test_file.py::TestName::test_name`.

# Misc conventions
# - Keep user-facing strings short and friendly.
# - Prefer minimal dependencies.
# - Avoid changing CLI prompts or output filenames unless required.
# - Keep variable names descriptive; avoid abbreviations in new code.

# Packaging notes
# - `pyproject.toml` is metadata only; no build backend configured.
# - Do not assume `pip install .` works unless you add build config.

# Version control notes
# - The `output/` directory contains generated images; avoid relying on it
#   for source data. If you add new generated files, consider ignoring them.
# - Do not delete user artifacts unless explicitly requested.

# When updating this file
# - Keep it concise and accurate.
# - Update command sections if new tools are added.
# - Add new rules from Cursor/Copilot if they appear later.
