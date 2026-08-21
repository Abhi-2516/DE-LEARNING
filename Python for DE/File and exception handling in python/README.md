# Exception Handling and File Handling in Python

A structured, runnable reference based on the concepts studied in `combined.py`. The examples use chai-shop scenarios, but the techniques apply to APIs, data pipelines, scripts, and backend services.

## Learning path

| File | Focus |
| --- | --- |
| `01_exception_basics.py` | `try`, `except`, `else`, and `finally` |
| `02_handling_multiple_exceptions.py` | Expected exception types and exception chaining |
| `03_raising_and_custom_exceptions.py` | `raise` and domain-specific exceptions |
| `04_exception_safe_order_service.py` | A small exception-aware service |
| `05_text_file_handling.py` | Read, write, append, encoding, and context managers |
| `06_csv_and_json_files.py` | Structured CSV and JSON data |
| `07_file_errors_and_paths.py` | `pathlib` and common file errors |
| `08_logging_and_best_practices.py` | Logging and production habits |

## Run an example

```text
python 01_exception_basics.py
python 06_csv_and_json_files.py
```

Run all lessons in PowerShell:

```powershell
Get-ChildItem -Filter '0[1-8]_*.py' | ForEach-Object { Write-Output "--- $($_.Name)"; python $_.FullName }
```

For definitions, flow diagrams, design rules, and revision questions, read [`LEARNING_NOTES.md`](LEARNING_NOTES.md).
