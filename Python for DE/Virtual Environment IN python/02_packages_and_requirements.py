"""Package installation and reproducibility command reference."""


COMMANDS = {
    "upgrade_pip": "python -m pip install --upgrade pip",
    "install_package": "python -m pip install requests",
    "install_multiple": "python -m pip install pandas numpy",
    "show_packages": "python -m pip list",
    "show_details": "python -m pip show requests",
    "save_dependencies": "python -m pip freeze > requirements.txt",
    "install_dependencies": "python -m pip install -r requirements.txt",
    "check_dependencies": "python -m pip check",
    "remove_package": "python -m pip uninstall requests",
}


if __name__ == "__main__":
    for name, command in COMMANDS.items():
        print(f"{name}: {command}")
