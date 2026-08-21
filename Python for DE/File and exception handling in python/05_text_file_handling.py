"""Write, read, and append text files with context managers."""

from pathlib import Path
from tempfile import TemporaryDirectory


def demonstrate_text_files(folder: Path) -> None:
    order_file = folder / "orders.txt"

    order_file.write_text("Masala chai - 2 cups\n", encoding="utf-8")
    with order_file.open("a", encoding="utf-8") as file:
        file.write("Ginger chai - 1 cup\n")

    with order_file.open("r", encoding="utf-8") as file:
        print(file.read(), end="")

    print(f"Stored at: {order_file.name}")


if __name__ == "__main__":
    with TemporaryDirectory() as temporary_folder:
        demonstrate_text_files(Path(temporary_folder))
