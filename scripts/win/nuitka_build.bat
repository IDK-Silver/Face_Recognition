@echo off


venv/Scripts/nuitka --mingw64 --standalone --show-progress --show-memory  --plugin-enable=pyside6 --nofollow-imports --follow-import-to=src --output-dir=out main.py





