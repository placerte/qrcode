# Changelog

All notable changes to this project will be documented in this file.

## Unreleased
- (Nothing yet.)

## 0.1.4
- Fixed PyInstaller packaging so Pillow/Tk helper modules are bundled in the Linux binary.
- Rebuilt the Linux release asset after validating the packaged GUI path no longer fails on missing Tk/Pillow modules.

## 0.1.3
- Rebuilt the Linux binary with Tkinter available so the packaged `--gui` path works.
- Tightened release QC to validate GUI support in the packaged executable before publishing.

## 0.1.2
- Added lightweight smoke tests for parser and batch parsing helpers.
- Added GitHub Actions CI to run the smoke tests.
- Refreshed README and AGENTS guidance for the current workflow.
- Ignored local `*-dump-*` artifacts and removed the tracked dump file from the repo.
- Cleaned small code issues in the CLI entry flow and path handling.

## 0.1.1
- Added `--version` CLI flag.
- Documented Python 3.12 requirement for PyInstaller builds.

## 0.1.0
- Initial release.
- Added batch file support for CLI input.
- Added PyInstaller build scaffolding.
