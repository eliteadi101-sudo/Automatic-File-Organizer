# Automatic File Organizer

Sort files in a selected folder into type-based subfolders, with a dry-run mode by default.

## Tech stack
Python 3, pathlib, shutil

## Features
- A working core implementation with a simple, usable interface or CLI.
- Input validation and basic error handling where appropriate.
- Source code organized for learning and extension.

## Getting started

Choose the instructions for this project's stack.

1. Install Python 3.10 or newer.
2. Install dependencies if a `requirements.txt` file exists:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python organize.py /path/to/folder
   ```
   For file organizer, preview moves first; add `--apply` only when ready.

## Project structure

The source files are kept in the root directory or in `public/`, `templates/`, or the conventional language-specific folders. Generated local databases, secrets, and dependency folders are excluded with `.gitignore` where applicable.

## Notes
- These are intermediate-level starter repositories intended for learning and customization. Review, test, and personalize them before presenting them as your own work.
- Never commit API keys, passwords, tokens, or private user data.
- Some projects use external APIs and therefore require an internet connection.
