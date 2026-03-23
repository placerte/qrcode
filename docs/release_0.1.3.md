## Summary
- Rebuilt the Linux binary with GUI packaging fixed.
- Added stricter release QC for packaged GUI verification.

## Details
- Installed the missing Tkinter runtime on the build host and rebuilt the Linux executable.
- Verified the packaged binary help output and GUI import path before release.
- Added explicit release checklist steps for checking `import tkinter` and testing `./dist/qrcode --gui`.

## Notes
- `v0.1.2` shipped with a defective Linux binary for GUI usage because Tkinter was missing from the build host.
- `v0.1.3` is the corrective release.
