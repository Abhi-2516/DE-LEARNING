"""Handle common file errors and inspect paths safely."""

from pathlib import Path
from tempfile import TemporaryDirectory


def read_required_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Required file not found: {path}") from error
    except PermissionError as error:
        raise PermissionError(f"Permission denied: {path}") from error


if __name__ == "__main__":
    with TemporaryDirectory() as temporary_folder:
        folder = Path(temporary_folder)
        existing_file = folder / "menu.txt"
        existing_file.write_text("masala\nginger\n", encoding="utf-8")

        print(read_required_file(existing_file), end="")
        print(f"Exists: {existing_file.exists()}")

        try:
            read_required_file(folder / "missing.txt")
        except FileNotFoundError as error:
            print(error)
