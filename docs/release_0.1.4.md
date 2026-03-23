## Summary
- Corrected the Linux binary packaging for the GUI path.
- Rebuilt and republished after verifying the packaged app includes the required Pillow/Tk pieces.

## Details
- Updated the PyInstaller spec to collect Pillow submodules needed by `ImageTk`, including `PIL._tkinter_finder`.
- Rebuilt the Linux executable and re-ran the packaged `--gui` path.
- Confirmed the binary no longer fails on missing `tkinter`, `PIL._tkinter_finder`, or `PyImagingPhoto` packaging issues.

## Notes
- On a headless Linux host, `--gui` may still fail with a `$DISPLAY` / windowing error; that is environmental and distinct from the packaging bug fixed here.
- This release supersedes `v0.1.3` for Linux GUI packaging.
