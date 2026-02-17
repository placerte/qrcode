# Release process

## Pre-release checklist

- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md`
- [ ] Build in a Python 3.12 venv (PyInstaller 6.6 does not support 3.13)
- [ ] Verify CLI runs: `qrcode --help`
- [ ] Generate a QR code (CLI) and verify output image
- [ ] Launch GUI and verify live preview
- [ ] Build with PyInstaller: `pyinstaller pyinstaller.spec`
- [ ] Smoke test the executable in `dist/`

## Release notes template

```
## Summary
- ...

## Details
- ...

## Notes
- ...
```
