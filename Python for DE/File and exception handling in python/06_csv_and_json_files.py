"""Structured file handling with CSV and JSON."""

import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory


ORDERS = [
    {"flavour": "masala", "cups": 2, "paid": True},
    {"flavour": "ginger", "cups": 1, "paid": False},
]


def write_and_read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["flavour", "cups", "paid"])
        writer.writeheader()
        writer.writerows(ORDERS)

    with path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_and_read_json(path: Path) -> list[dict]:
    path.write_text(json.dumps(ORDERS, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    with TemporaryDirectory() as temporary_folder:
        folder = Path(temporary_folder)
        print(write_and_read_csv(folder / "orders.csv"))
        print(write_and_read_json(folder / "orders.json"))
