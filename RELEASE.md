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
    - On a headless build host, a `$DISPLAY`/windowing error is acceptable as long as GUI imports succeed and the failure is clearly environmental rather than a missing packaged module.
- [ ] Review PyInstaller warnings for missing GUI/runtime modules before publishing
- [ ] If Pillow/Tkinter is used, confirm the packaged binary no longer errors on missing `PIL._tkinter_finder` / `PyImagingPhoto`

## Release notes template

```
## Summary
- ...

## Details
- ...

## Notes
- ...
```
