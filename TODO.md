# TODO

## Audit: small-effort, high-gain updates

- [x] Align the Python version story everywhere (`README.md`, `pyproject.toml`, `AGENTS.md`, release/build notes as needed)
  - Updated `pyproject.toml` runtime baseline to Python 3.9+ to match the documented source-install story.
  - Verified build notes still call out Python 3.12 specifically for PyInstaller builds.
- [x] Refresh `AGENTS.md` so it matches the current repo reality
  - Updated environment, packaging, build, formatting, and command guidance to match the current repo.
- [ ] Add a tiny smoke-test suite (batch parsing, fallback title generation, CLI parser basics)
- [ ] Clean small code smells in `src/qrcode_generator/qr.py`
- [ ] Improve or document font fallback behavior
- [ ] Tighten the `uv` source workflow in the README
- [ ] Decide whether `qrcode-dump-20260217-1447.txt` should stay at repo root or move elsewhere
- [ ] Consider adding minimal CI after tests exist
- [ ] Polish README examples and small usage details
