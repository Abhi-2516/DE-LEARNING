"""Virtual environment workflow reference for Windows PowerShell.

This file prints commands and explanations. It does not execute shell commands.
"""


COMMANDS = [
    ("Check Python", "python --version", "Confirms that Python is available."),
    (
        "Create an environment",
        "python -m venv .venv",
        "Creates an isolated environment in the .venv folder.",
    ),
    (
        "Activate in PowerShell",
        ".\\.venv\\Scripts\\Activate.ps1",
        "Makes this environment's Python and pip the active commands.",
    ),
    (
        "Verify the interpreter",
        "python -c \"import sys; print(sys.executable)\"",
        "Shows the exact Python executable being used.",
    ),
    (
        "Leave the environment",
        "deactivate",
        "Returns the terminal to its previous Python environment.",
    ),
]


if __name__ == "__main__":
    for title, command, explanation in COMMANDS:
        print(f"{title}:\n  {command}\n  {explanation}\n")
