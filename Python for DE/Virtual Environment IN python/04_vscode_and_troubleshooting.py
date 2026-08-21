"""VS Code and Windows troubleshooting command reference."""


GUIDE = {
    "select_interpreter": "Ctrl+Shift+P -> Python: Select Interpreter -> choose .venv\\Scripts\\python.exe",
    "activation_policy": "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser",
    "run_without_activation": ".\\.venv\\Scripts\\python.exe your_script.py",
    "run_module_without_activation": ".\\.venv\\Scripts\\python.exe -m pip list",
    "find_python": "Get-Command python",
    "find_pip": "python -m pip --version",
    "recreate_environment": "Remove-Item -Recurse -Force .venv; python -m venv .venv",
}


if __name__ == "__main__":
    for topic, instruction in GUIDE.items():
        print(f"{topic}:\n  {instruction}\n")
