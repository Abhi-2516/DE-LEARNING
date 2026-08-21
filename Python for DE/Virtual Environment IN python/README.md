# Python Virtual Environments

This folder explains how to create isolated Python environments and reproduce a project's dependencies. The commands target Windows PowerShell, with equivalent command notes in [`LEARNING_NOTES.md`](LEARNING_NOTES.md).

## Contents

| File | Focus |
| --- | --- |
| `01_create_and_activate.py` | Creation, activation, verification, and deactivation commands |
| `02_packages_and_requirements.py` | Installing packages and managing `requirements.txt` |
| `03_verify_environment.py` | Inspecting the active interpreter at runtime |
| `04_vscode_and_troubleshooting.py` | VS Code setup and common Windows fixes |
| `LEARNING_NOTES.md` | Complete explanations, workflows, and best practices |
| `combined.py` | Original study placeholder, preserved |

## Quick start: PowerShell

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install requests
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
deactivate
```

When activation succeeds, PowerShell normally shows `(.venv)` at the beginning of the prompt. Always use `python -m pip` so pip belongs to the same interpreter as `python`.

Run the demonstrations:

```powershell
python .\01_create_and_activate.py
python .\02_packages_and_requirements.py
python .\03_verify_environment.py
python .\04_vscode_and_troubleshooting.py
```
