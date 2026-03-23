# TODO

## Audit: small-effort, high-gain updates

- [x] Align the Python version story everywhere (`README.md`, `pyproject.toml`, `AGENTS.md`, release/build notes as needed)
  - Updated `pyproject.toml` runtime baseline to Python 3.9+ to match the documented source-install story.
  - Verified build notes still call out Python 3.12 specifically for PyInstaller builds.
- [x] Refresh `AGENTS.md` so it matches the current repo reality
  - Updated environment, packaging, build, formatting, and command guidance to match the current repo.
- [x] Add a tiny smoke-test suite (batch parsing, fallback title generation, CLI parser basics)
  - Added `pytest` as a dev dependency.
  - Added `tests/test_qr.py` covering batch parsing, fallback title generation, and parser basics.
- [x] Clean small code smells in `src/qrcode_generator/qr.py`
  - Removed the odd CLI instantiation assignment.
  - Kept the control flow simpler and easier to read.
- [x] Improve or document font fallback behavior
  - Improved the fallback warning text.
  - Documented fallback behavior in `README.md`.
- [x] Tighten the `uv` source workflow in the README
  - Added a `uv sync` install path and clearer source-run examples.
  - Kept one-off dump tooling out of managed project dependencies so normal dev/test workflows remain compatible with the stated Python baseline.
- [x] Decide whether `qrcode-dump-20260217-1447.txt` should stay at repo root or move elsewhere
  - Added `*-dump-*` to `.gitignore`.
  - Will stop tracking dump files in git so they stay local dev artifacts.
- [x] Consider adding minimal CI after tests exist
  - Added a small GitHub Actions workflow that runs `uv sync --group dev` and `uv run pytest`.
- [x] Polish README examples and small usage details
  - Added source-run examples, custom output example, development commands, and clarified build notes.
