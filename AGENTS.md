# AGENTS.md
# Guidance for agentic coding assistants working in this repo.

# Project snapshot
# - Simple QR code generator with CLI and Tkinter GUI.
# - Source is in `src/qrcode_generator`.
# - Dependencies are intentionally lightweight (`qrcode` + `pillow`).
# - Packaging is configured via `pyproject.toml` with a setuptools build backend.

# Repo rules
# - No Cursor rules found in `.cursor/rules/` or `.cursorrules`.
# - No GitHub Copilot instructions found in `.github/copilot-instructions.md`.

# Environment setup
# - Runtime support target: Python 3.9+.
# - For source installs, prefer `uv`:
#   - `uv sync`
#   - `uv run qrcode --help`
# - Traditional venv also works:
#   - `python -m venv .venv`
#   - `source .venv/bin/activate`
#   - `pip install -r requirements.txt`
# - Pierre prefers the latest stable Python when the ecosystem supports it cleanly
#   (currently Python 3.13).
# - Before packaging a binary, verify the build host can import `tkinter` so the
#   GUI path is not silently excluded from the executable.

# Build / lint / test commands
# - Run CLI help: `uv run qrcode --help`
# - Run CLI app: `uv run qrcode --url https://example.com --title Example`
# - Run GUI: `uv run qrcode --gui`
# - Build (PyInstaller): `uv run --extra dev pyinstaller qrcode.spec`
# - Format: optional ad-hoc tooling (not pinned in project metadata)
# - Tests: `uv run pytest`
# - CI: GitHub Actions runs `uv sync --group dev` and `uv run pytest`
#
# If you add tooling, document it here and mirror any new commands in README.

# Dependency management
# - Runtime deps are pinned in `requirements.txt` and mirrored in `pyproject.toml`.
# - Dev/build deps live in `pyproject.toml` under `[dependency-groups]`.
# - One-off dump tooling such as `produm` should stay out of managed project
#   dependencies unless the supported Python range is adjusted to match.
# - If you add a runtime dependency, update both `requirements.txt` and README.
# - Avoid adding heavy libraries; keep the app lightweight.

# Run commands (manual verification)
# - CLI help: `uv run qrcode --help`
# - Generate a QR code: `uv run qrcode --url https://example.com --title Example`
# - Batch mode: `uv run qrcode --batch-file ./examples/urls.txt`
# - GUI app: `uv run qrcode --gui`
# - Output dir defaults to `./output/` (created if missing).

# CLI/GUI workflow expectations
# - CLI prompts should remain short and clear.
# - GUI should update preview and filepath when fields change.
# - Save action should always create the output directory if missing.
# - Batch mode should stay compatible with the documented `examples/urls.txt` format.

# Layout and entry points
# - `src/qrcode_generator/qr.py` is the main entry point.
# - `src/qrcode_generator/cli_app.py` implements CLI prompts.
# - `src/qrcode_generator/gui_app.py` implements Tkinter GUI.
# - `src/qrcode_generator/model.py` handles QR creation and image output.
# - `src/qrcode_generator/parser.py` handles argparse CLI args.
# - `src/qrcode_generator/defaults.py` contains UI and filesystem defaults.
# - Console script entry point: `qrcode = qrcode_generator.qr:main`.

# Code style guidelines
# These reflect current patterns in the codebase.

# Formatting
# - Use 4-space indentation.
# - Keep blank lines between methods and logical sections.
# - Prefer PEP 8 style when editing.
# - `black` is available in dev dependencies, but avoid unrelated reformatting.
# - Avoid trailing whitespace and keep file-level spacing consistent.

# Imports
# - Follow standard order when possible:
#   1) standard library
#   2) third-party
#   3) local modules
# - Use package-qualified imports inside `src/qrcode_generator`.
# - Avoid wildcard imports.
# - Keep Tkinter imports grouped (`import tkinter as tk`, `from tkinter import ttk`).

# Naming conventions
# - Classes: PascalCase (e.g., `QRCodeGeneratorGUI`).
# - Functions/methods: snake_case.
# - Constants: ALL_CAPS.
# - Private helpers use a single leading underscore.
# - Avoid double-underscore for new methods unless name-mangling is intended.

# Types and typing
# - Type hints are used in several modules; keep new annotations simple and explicit.
# - Prefer explicit return types for new or edited public methods.
# - Avoid introducing heavy typing frameworks unless required.

# Error handling
# - Current code uses simple `try/except` with `print` for user feedback.
# - Prefer specific exceptions (`except OSError:`) over broader catches.
# - For CLI/GUI flows, short `print`-based errors are acceptable.
# - For helper functions, prefer raising exceptions over swallowing them silently.

# Data and I/O
# - Output directory is created if missing.
# - Preserve output filename behavior unless intentionally changing it.
# - Image operations use Pillow and qrcode.
# - Avoid changing defaults without updating `defaults.py` and README.

# CLI behavior
# - argparse is used in `QRCode_Parser`.
# - Keep existing flags stable where possible.
# - `--gui` switches from CLI to GUI.
# - `--batch-file` expects the documented plain-text line format.

# GUI behavior
# - Tkinter is used with `ttk` widgets.
# - UI state lives in Tk variables.
# - Keep references to `PhotoImage` on the instance to avoid garbage collection.
# - Layout uses constants from `DefaultsUI`.

# File structure conventions
# - Keep new modules inside `src/qrcode_generator`.
# - Avoid adding top-level scripts unless documented in README.
# - Generated output belongs in `output/` and should stay ignored.
# - Build artifacts (`dist/`, `build/`, `*.egg-info/`) should remain ignored.

# Testing guidance
# - Automated smoke tests live under `tests/` and run with `uv run pytest`.
# - Manual verification is still useful for GUI and output checks:
#   - Generate QR code with and without title.
#   - Verify output file path and image contents.
#   - Check batch file behavior.
#   - Check GUI updates when fields change.
# - If you add more tests, keep them lightweight and document any new commands in README and here.

# Misc conventions
# - Keep user-facing strings short and friendly.
# - Prefer minimal dependencies.
# - Avoid changing CLI prompts or output filenames unless required.
# - Keep variable names descriptive; avoid unnecessary abbreviations.

# Packaging notes
# - `pyproject.toml` is the canonical package metadata and build configuration.
# - `pip install .` / `uv sync` should be assumed to work and stay working.
# - Keep the console-script entry point functional.

# Version control notes
# - `output/` contains generated files and should remain ignored.
# - Do not delete user artifacts unless explicitly requested.
# - Be cautious about one-off dump files at repo root; prefer documenting or relocating them intentionally.

# When updating this file
# - Keep it concise and accurate.
# - Update command sections if tooling changes.
# - Add new rules from Cursor/Copilot if they appear later.
ew rules from Cursor/Copilot if they appear later.
they appear later.
