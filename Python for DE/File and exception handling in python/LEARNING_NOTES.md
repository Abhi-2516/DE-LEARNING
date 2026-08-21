# Exception Handling and File Handling Notes

## 1. Why these topics matter

Programs fail for ordinary reasons: a user enters invalid data, a key is missing, a file does not exist, or an external service is unavailable. Exception handling lets a program respond deliberately instead of crashing unexpectedly. File handling lets a program persist and exchange data safely.

The goal is not to hide every error. The goal is to handle expected failures, add useful context, clean up resources, and allow unexpected failures to remain visible.

## 2. Exception terminology

- **Exception**: an object describing an abnormal event during execution.
- **Raise**: explicitly create an exception with `raise`.
- **Handle**: catch an exception with `except`.
- **Traceback**: Python's diagnostic report showing where an unhandled exception occurred.

Common built-in exceptions include `ValueError` for a valid type with an invalid value, `TypeError` for an inappropriate type, `KeyError` for a missing dictionary key, `IndexError` for an invalid sequence index, `FileNotFoundError` for a missing file, and `ZeroDivisionError` for division by zero.

## 3. The exception flow

```python
try:
    risky_operation()
except ValueError as error:
    recover_from_bad_value(error)
else:
    run_only_when_no_exception_occurred()
finally:
    release_resources_or_record_completion()
```

- `try` contains the smallest operation that may fail.
- `except` handles a known failure.
- `else` runs only when the `try` block succeeds.
- `finally` runs whether the operation succeeds or fails.

Keep the `try` block small. A large block can make it unclear which line caused the exception and can accidentally catch failures from unrelated code.

## 4. Handling multiple exceptions

Catch specific exceptions before broader ones. This is clearer:

```python
try:
    price = menu[flavour]
    cups = int(raw_cups)
except KeyError:
    print("Unknown flavour")
except ValueError:
    print("Cups must be a number")
```

Avoid bare `except:` because it also catches `KeyboardInterrupt` and `SystemExit`. Avoid `except Exception` unless you are at a deliberate application boundary, such as logging and returning an error response.

## 5. Raising errors and exception chaining

Use `raise` to enforce a business rule:

```python
if cups <= 0:
    raise ValueError("cups must be positive")
```

When translating a low-level error into a domain-level error, use `raise ... from error`. This keeps the original cause available for debugging while presenting a useful message to callers.

## 6. Custom exceptions

Custom exceptions make domain failures precise and catchable:

```python
class OrderError(Exception):
    pass

class UnknownFlavourError(OrderError):
    pass
```

Use a small hierarchy when callers need to handle all order errors together or specific errors separately. Name exceptions with an `Error` suffix and give them a clear domain meaning.

## 7. File modes and context managers

Common text modes:

- `r`: read; the file must exist.
- `w`: write; creates or replaces the file.
- `a`: append; creates the file if needed and writes at the end.
- `x`: create a new file; fails if it already exists.
- `rb` / `wb`: read or write binary data.

Prefer `pathlib.Path` and always specify `encoding="utf-8"` for text files when portability matters. Use `with` so Python closes the file even if writing or reading raises an exception:

```python
from pathlib import Path

path = Path("orders.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Masala chai\n")
```

A context manager implements setup and cleanup around a block. It is the modern replacement for manually calling `open()` and remembering `close()` in `finally`.

## 8. Text, CSV, and JSON

Use plain text for human-readable lines. Use `csv.DictReader` and `csv.DictWriter` for tabular data; opening CSV files with `newline=""` avoids platform-specific blank lines. Use `json.dump`/`json.load` or `json.dumps`/`json.loads` for structured data that must be exchanged with other systems.

JSON supports objects, arrays, strings, numbers, booleans, and `null`. It does not preserve every Python type, so convert dates, sets, and custom objects explicitly when necessary.

## 9. File errors and safe paths

Check or handle the operation itself rather than relying only on `exists()`, because a file can change between a check and the operation. Catch `FileNotFoundError`, `PermissionError`, and `IsADirectoryError` when those failures are meaningful to your application.

`Path` makes joining paths portable:

```python
path = Path("data") / "orders.json"
```

Avoid constructing paths by manually concatenating backslashes. Never trust user-provided path fragments without validating the allowed directory and filename.

## 10. Logging and production practice

Use the `logging` module for diagnostics in reusable programs. Logging supports levels such as `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`, and can be routed to files or monitoring systems. Do not log passwords, tokens, payment details, or other secrets.

Good practice:

1. Catch exceptions you can actually recover from.
2. Validate inputs at the boundary.
3. Raise specific errors with actionable messages.
4. Preserve causes with `raise ... from ...`.
5. Keep cleanup in context managers or `finally`.
6. Do not silently use `pass` for failures.
7. Log unexpected failures with enough context.
8. Test both success and failure paths.

## Revision questions

1. When does the `else` block run?
2. Why should a `try` block be small?
3. What is the difference between `ValueError` and `TypeError`?
4. Why is `raise NewError(...) from error` useful?
5. What happens to an existing file in `w` mode?
6. Why is `with open(...)` safer than manually calling `close()`?
7. When should you choose CSV instead of JSON?
8. Why should application code avoid a bare `except:`?

## Mini-project extension

Build an order ledger that:

- reads orders from a JSON file,
- validates flavour and quantity,
- calculates totals,
- writes successful orders to a CSV file,
- records rejected orders with `logging`, and
- handles missing or malformed input files with clear messages.
