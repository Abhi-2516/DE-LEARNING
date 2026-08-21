# Python Virtual Environments: Professional Notes

## 1. What is a virtual environment?

A virtual environment is an isolated directory containing a Python interpreter and its own package-installation location. It lets each project use its required package versions without changing the global Python installation or interfering with another project.

A virtual environment is not a second operating system and it is not a complete copy of every system file. It is a lightweight project boundary that points to a base Python installation and keeps project packages separate.

## 2. Why use one?

Without isolation, installing or upgrading a package for one project can break another project. A project may need `pandas` version A while an older project needs version B. A virtual environment gives each project its own dependency set.

Benefits:

- Reproducible development and deployment.
- Fewer version conflicts.
- Safer experimentation.
- Clear project ownership of dependencies.
- Easier onboarding for another developer.
- Cleaner global Python installation.

## 3. How `venv` works

Python's standard-library `venv` module creates the environment:

```powershell
python -m venv .venv
```

`python -m venv` means "run Python's built-in `venv` module." `.venv` is a conventional folder name. The environment stores scripts, a Python executable or launcher, and package metadata. On Windows, activation scripts are under `.venv\Scripts\`.

Activation changes the current shell's `PATH`, so `python` and `pip` resolve to the environment. Activation is convenient but not required; you can call the environment's executable directly.

## 4. Complete Windows PowerShell workflow

### Create

Run this from the project root:

```powershell
python --version
python -m venv .venv
```

If several Python versions are installed, the Windows launcher can select one:

```powershell
py --list
py -3.12 -m venv .venv
```

Do not create the environment inside a package or source directory. Keep it at the project root and name it `.venv`.

### Activate

```powershell
.\.venv\Scripts\Activate.ps1
```

A successful activation normally adds `(.venv)` to the PowerShell prompt.

Command Prompt uses a different script:

```bat
.venv\Scripts\activate.bat
```

Git Bash uses:

```bash
source .venv/Scripts/activate
```

### Verify

```powershell
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Both paths should point into the project's `.venv` directory. You can also run `03_verify_environment.py`.

### Install packages

```powershell
python -m pip install --upgrade pip
python -m pip install requests pandas
python -m pip list
python -m pip show pandas
```

Use `python -m pip`, rather than bare `pip`, to ensure pip belongs to the Python interpreter you selected.

### Save and restore dependencies

After installing the packages a project needs:

```powershell
python -m pip freeze > requirements.txt
```

On another machine or after recreating the environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`requirements.txt` records exact installed versions. Review it before committing because `pip freeze` can include transitive packages that you did not install directly.

### Deactivate and remove

```powershell
deactivate
Remove-Item -Recurse -Force .venv
```

A virtual environment is disposable. If it becomes corrupted, deactivate it, delete `.venv`, recreate it, and reinstall from `requirements.txt`.

## 5. VS Code setup

1. Open the project root in VS Code.
2. Press `Ctrl+Shift+P`.
3. Run `Python: Select Interpreter`.
4. Choose `.venv\Scripts\python.exe`.
5. Open a new terminal if the old terminal still uses another interpreter.
6. Verify with `python -c "import sys; print(sys.executable)"`.

VS Code may auto-detect `.venv`, but the selected interpreter and terminal activation are separate settings. Always verify when imports behave unexpectedly.

## 6. PowerShell execution-policy issue

If activation is blocked with a script-execution error, use a user-scoped policy change:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then open a new terminal and activate again. This changes the policy for your Windows user, not the entire computer. If company policy prevents the change, run the environment without activation:

```powershell
.\.venv\Scripts\python.exe your_script.py
.\.venv\Scripts\python.exe -m pip install requests
```

## 7. Git and project hygiene

Do not commit the `.venv` directory. It is machine-specific, can be large, and can be recreated. Add this to a project-level `.gitignore`:

```gitignore
.venv/
venv/
__pycache__/
*.py[cod]
```

Commit dependency declarations such as `requirements.txt`, not the environment itself. A lockfile or modern dependency tool may be preferable for larger applications, but `venv` remains the isolation mechanism.

## 8. Troubleshooting

### `python` is not recognized

Install Python, enable the Python PATH option during installation, or use `py --version`. In VS Code, confirm the Python extension and interpreter selection.

### `pip` installs into the wrong place

Do not use bare `pip`. Run:

```powershell
python -m pip --version
python -c "import sys; print(sys.executable)"
```

If the paths do not point into `.venv`, activate the environment or call `.venv\Scripts\python.exe` directly.

### A package import fails

Check the active interpreter, install into that interpreter, and test the import:

```powershell
python -m pip install package_name
python -c "import package_name; print(package_name.__file__)"
```

### Environment is broken

```powershell
deactivate
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 9. Best practices

- Use one `.venv` per project.
- Create it with the Python version the project supports.
- Keep `.venv` out of version control.
- Record dependencies in a reviewed file.
- Upgrade packages intentionally and test afterward.
- Use `python -m pip` consistently.
- Verify the active interpreter before debugging imports.
- Treat the environment as reproducible output, not source code.

## Revision questions

1. What problem does a virtual environment solve?
2. What does `python -m venv .venv` do?
3. What changes when an environment is activated?
4. Why is `python -m pip` safer than bare `pip`?
5. Why should `.venv` not be committed to Git?
6. What is the purpose of `requirements.txt`?
7. How can you use an environment without activating it?
8. What should you check when VS Code reports an import error?
