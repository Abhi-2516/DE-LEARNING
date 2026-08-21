"""Inspect the Python interpreter and installed package location."""

import platform
import sys


if __name__ == "__main__":
    print(f"Python version: {platform.python_version()}")
    print(f"Executable: {sys.executable}")
    print(f"Prefix: {sys.prefix}")
    print(f"Base prefix: {sys.base_prefix}")
    print(f"Running inside venv: {sys.prefix != sys.base_prefix}")

    try:
        import pip
    except ImportError:
        print("pip is not available in this interpreter")
    else:
        print(f"pip version: {pip.__version__}")
