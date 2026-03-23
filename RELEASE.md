# Release process

## Pre-release checklist

- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md`
- [ ] Verify source workflow first:
  - [ ] `uv run pytest`
  - [ ] `uv run qrcode --help`
  - [ ] `uv run qrcode --url https://example.com --title Example`
  - [ ] `uv run qrcode --gui` (or otherwise verify GUI on a machine with a working display/toolkit)
- [ ] Verify the build host has Tkinter available before packaging:
  - [ ] `python -c "import tkinter"`
- [ ] Build with PyInstaller using the intended release environment:
  - [ ] `uv run --group dev pyinstaller qrcode.spec`
- [ ] Smoke test the built executable in `dist/`:
  - [ ] `./dist/qrcode --help`
  - [ ] `./dist/qrcode --url https://example.com --title Example`
  - [ ] `./dist/qrcode --gui` to confirm the GUI entry path imports and launches
- [ ] Review PyInstaller warnings for missing GUI/runtime modules before publishing

## Release notes template

```
## Summary
- ...

## Details
- ...

## Notes
- ...
```
