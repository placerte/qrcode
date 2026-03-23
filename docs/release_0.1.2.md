## Summary
- Added smoke tests and minimal CI.
- Tightened the docs and repo guidance.
- Cleaned up small code issues and stopped tracking local dump artifacts.

## Details
- Added `pytest` smoke tests covering parser behavior and batch parsing helpers.
- Added a GitHub Actions workflow that runs `uv sync --group dev` and `uv run pytest`.
- Refreshed `README.md` and `AGENTS.md` to match the current repo workflow.
- Added `*-dump-*` to `.gitignore` and removed the tracked dump artifact from git.
- Cleaned up `qr.py` and improved path/font fallback handling.

## Notes
- This release keeps the app runtime compatible with Python 3.9+.
- Pierre prefers using the latest stable Python when practical; the current development environment is Python 3.13.
- PyInstaller builds should still be sanity-checked on the target platform after publishing.
