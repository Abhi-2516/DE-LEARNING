# Small Automation Projects in Python

This folder contains four beginner-friendly automation projects. Together they revise:

- File and folder operations
- Filtering files by extension
- Batch renaming with a preview and confirmation step
- Real-time folder monitoring with events
- System resource monitoring
- Functions, classes, dictionaries, loops, exceptions, and formatted strings
- Standard-library modules and third-party libraries

The scripts are intentionally small so that each idea can be studied separately.

## Project Files

| File | Main idea | Libraries |
| --- | --- | --- |
| `1_file_organizer.py` | Sort existing files into folders by extension | `os`, `shutil` |
| `2_get_photos_organized.py` | Batch rename files after a preview | `os` |
| `3_to_monitor_Streming_of_events.py` | Watch a folder and move new files automatically | `os`, `shutil`, `watchdog` |
| `4_system_resource_monitor.py` | Display CPU, RAM, and disk usage continuously | `psutil`, `time`, `os` |
| `TextFiles/sample.txt` | Sample `.txt` file for file-organizing practice | None |
| `Others/` | Destination for unknown file types | None |

## Setup

Use Python 3. The first and second projects use only the Python standard library. Install the two external packages needed by the other projects:

```bash
python -m pip install watchdog psutil
```

On Windows, `py` may be used instead of `python`:

```bash
py -m pip install watchdog psutil
```

Run commands from this folder:

```bash
python 1_file_organizer.py
python 2_get_photos_organized.py
python 3_to_monitor_Streming_of_events.py
python 4_system_resource_monitor.py
```

Stop the long-running projects with `Ctrl+C`.

## 1. File Organizer

### What it does

`1_file_organizer.py` scans a selected folder and moves files into these destination folders:

- `.pdf` -> `PDFs`
- `.jpg`, `.jpeg`, `.png` -> `Images`
- `.txt` -> `TextFiles`
- Any other file type -> `Others`

Folders are ignored during the move. Destination folders are created only when required.

### Main ideas learned

- `import os` provides operating-system and path functions.
- `import shutil` provides higher-level file operations such as moving files.
- A dictionary can store configuration instead of a long chain of `if/elif` statements.
- A list stores multiple extensions for one destination folder.
- `os.listdir(path)` returns names inside a folder.
- `os.path.join(a, b)` builds a path using the correct separator for the operating system.
- `os.path.splitext(filename)` returns the filename and extension as a tuple.
- `.lower()` makes extension matching case-insensitive.
- `os.path.isfile(path)` checks that a path is a file, not a folder.
- `os.makedirs(path, exist_ok=True)` creates a folder and does not fail if it already exists.
- `shutil.move(source, destination)` moves a file.
- `return` sends a result back from a function and exits that function.

### Important syntax

```python
EXTENSION_TO_FOLDER = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png"],
}

for folder, extensions in EXTENSION_TO_FOLDER.items():
    if extension in extensions:
        return folder
```

`.items()` gives both the dictionary key and value during iteration.

### Current behavior to remember

- The script may move the files in the same folder as the script, because the current working directory is used when the input is blank.
- A file with an unknown extension goes to `Others`.
- If a destination already contains a file with the same name, the result depends on the operating system and `shutil` behavior. A production version should check for collisions and choose a new name.
- A safer production version should also validate that the source folder exists and handle permission errors.

## 2. Batch File Renamer

### What it does

`2_get_photos_organized.py` finds files with a chosen extension, sorts their names, previews the proposed names, and renames them only after the user enters `y`.

Example:

```text
photo_a.jpg -> image_1.jpg
photo_b.jpg -> image_2.jpg
```

### Main ideas learned

- List comprehensions create a filtered list in one expression.
- `.endswith(value)` checks whether a string ends with a suffix.
- Calling `.lower()` on both sides makes extension filtering case-insensitive.
- `.sort()` changes a list in place.
- `enumerate(files, start=1)` supplies both an index and an item.
- An f-string inserts expressions into a string: `f"{base_name}_{i}{extension}"`.
- `.strip()` removes extra whitespace from user input.
- `.lower()` normalizes confirmation input such as `Y` to `y`.
- `os.rename(source, destination)` changes a file's name.
- An early `return` cancels the operation when no files are found or confirmation is not `y`.

### Important syntax

```python
files = [
    file_name
    for file_name in os.listdir(folder)
    if file_name.lower().endswith(extension.lower())
]
```

This is equivalent to: loop through the folder, keep only matching names, and store them in a list.

### Why the preview matters

Renaming files is a destructive-looking operation: the original names change. Showing the mapping first and requiring confirmation is a simple safety pattern. The current script does not implement the docstring's optional undo file, so the rename cannot be automatically reversed.

### Current behavior to remember

- The user must include the dot in the extension, for example `.jpg`.
- The generated name always uses the extension entered by the user, even if the original file uses a different case such as `.JPG`.
- Existing destination names can cause collisions or platform-specific rename errors. A production version should validate every destination before making any change.
- A two-phase rename using temporary names is safer when a destination name is also an existing source name.
- The function name and file name are about batch renaming, not specifically organizing photos.

## 3. Real-Time Folder Organizer with Watchdog

### What it does

`3_to_monitor_Streming_of_events.py` watches the user's Downloads folder. When a new file is created, it chooses a destination and moves the file:

- `.pdf` -> `PDFs`
- `.jpg`, `.jpeg`, `.png` -> `Images`
- `.zip` -> `Archives`
- Everything else -> `Others`

### New library: `watchdog`

`watchdog` is a third-party library for receiving file-system events. Its main pieces here are:

- `FileSystemEventHandler`: base class for event callbacks.
- `Observer`: background service that watches a path.
- `on_created(self, event)`: callback called when an item is created.
- `observer.schedule(handler, path, recursive=False)`: registers what to watch.
- `observer.start()`: starts the observer thread.
- `observer.stop()`: requests shutdown.
- `observer.join()`: waits for the observer thread to finish.

The program is event-driven: the handler reacts when the operating system reports a new item instead of repeatedly listing the folder.

### Python concepts used

- A class groups related behavior and state.
- Inheritance is used with `class FileMoverHandler(FileSystemEventHandler)`.
- `self` refers to the current handler object.
- `event.is_directory` prevents folders from being moved as files.
- `.get(key, default)` reads a dictionary value and supplies a fallback.
- `os.path.basename(path)` extracts only the final filename.
- `try/except` prevents one move failure from immediately crashing the handler.
- `KeyboardInterrupt` is raised when the user presses `Ctrl+C`.

### Current behavior to remember

- `WATCH_FOLDER` is fixed to `~/Downloads`; it is expanded with `os.path.expanduser()`.
- `recursive=False` means subfolders are not monitored.
- The handler may receive an event before a download has finished writing. A robust version should wait until the file is stable and confirm that it is ready to move.
- The bare `except:` hides the real error. Prefer `except OSError as error:` and log `error`.
- The destination is built from the global `WATCH_FOLDER`, so the handler is not reusable for another watched folder without changing the code.
- A file with an unknown extension is moved to `Others`.

## 4. System Resource Monitor

### What it does

`4_system_resource_monitor.py` repeatedly clears the terminal and displays:

- CPU percentage
- RAM percentage, used GB, and total GB
- Disk percentage, used GB, and total GB

The display refreshes every three seconds and stops cleanly with `Ctrl+C`.

### New library: `psutil`

`psutil` means Python system and process utilities. It reads operating-system statistics:

- `psutil.cpu_percent(interval=1)` measures CPU usage and waits one second for a useful sample.
- `psutil.virtual_memory()` returns a memory-information object with values such as `.percent`, `.used`, and `.total`.
- `psutil.disk_usage(path)` returns disk values such as `.percent`, `.used`, and `.total`.

The code divides byte counts by `1e9` to display decimal gigabytes and uses `round(value, 2)` to keep two decimal places.

### Python concepts used

- `time.sleep(3)` pauses before the next refresh.
- `os.name` identifies the operating-system family.
- `os.system()` sends a command to the terminal; this script uses `cls` on Windows and `clear` on Unix-like systems.
- A `while True` loop repeats forever until an exception or another control statement stops it.
- The `try/except KeyboardInterrupt` pattern gives a long-running command a friendly shutdown message.
- F-strings make readable output while mixing text and calculated values.

### Current behavior to remember

- The docstring says the script warns above 80% CPU or RAM, but the current implementation only prints values; no warning condition exists yet.
- `psutil.disk_usage('/')` is commonly usable on Windows, but `Path.home().anchor` or `os.path.abspath(os.sep)` can be clearer when choosing the system drive.
- `os.system()` is simple but less controlled than a terminal UI library. It is acceptable for this small learning project.
- The `"🔥"` and `"⭐"` characters require a terminal that supports Unicode. Replace them with ASCII if the terminal displays encoding errors.

## Core Python Revision Sheet

### Variables and constants

```python
cpu = psutil.cpu_percent(interval=1)
WATCH_FOLDER = os.path.expanduser("~/Downloads")
```

Python variables are created by assignment. Uppercase names are a convention for values intended to be treated as constants.

### Conditions

```python
if event.is_directory:
    return

if confirm != "y":
    print("Cancel")
    return
```

`if` runs code only when its condition is true. `!=` means "not equal".

### Loops

- `for` iterates through a collection.
- `while True` repeats until it is interrupted or explicitly stopped.
- `enumerate()` is useful when both position and value are needed.

### Functions

Functions package reusable behavior:

```python
def get_destination_folder(filename):
    return "Others"
```

Parameters receive input. `return` produces output. A function can also return early to cancel work.

### Classes and methods

A class defines behavior for objects. Methods are functions inside a class and receive `self` as their first parameter. The watchdog handler overrides the `on_created` method provided by its parent class.

### Exceptions

```python
try:
    shutil.move(source, destination)
except OSError as error:
    print(f"Move failed: {error}")
```

Use exceptions for operations that can fail because of missing files, permissions, locked files, or invalid paths. Catch specific exception types whenever possible.

### Common path tools

| Expression | Meaning |
| --- | --- |
| `os.getcwd()` | Current working directory |
| `os.listdir(path)` | Names in a directory |
| `os.path.join(a, b)` | Platform-safe path joining |
| `os.path.isfile(path)` | Whether a path is a file |
| `os.path.isdir(path)` | Whether a path is a directory |
| `os.path.basename(path)` | Final name from a path |
| `os.path.splitext(name)` | Filename and extension |
| `os.path.expanduser(path)` | Expands `~` to the user's home folder |

## Safe Practice Checklist

Before testing an organizer or renamer:

1. Use a temporary test folder, not a folder containing important files.
2. Confirm the input folder path before pressing Enter.
3. Review the rename preview carefully.
4. Keep backups when testing new automation.
5. Test unknown extensions and uppercase extensions.
6. Test duplicate names and files that are currently open.
7. Stop long-running programs with `Ctrl+C`.

## Suggested Improvements for the Next Version

These are natural next steps after understanding the current code:

- Add `pathlib.Path` for a more modern path API.
- Add collision-safe filenames such as `report_1_1.pdf` or a timestamp.
- Validate source and destination paths before changing files.
- Replace bare `except:` with specific exceptions and useful error messages.
- Use the `logging` module instead of only `print()` for long-running automation.
- Add command-line arguments with `argparse` instead of asking for every value interactively.
- Add an undo log for the batch renamer.
- Add CPU/RAM thresholds and warnings to the resource monitor.
- Add tests using temporary directories from `tempfile` and `pathlib`.
- For watchdog downloads, wait for a file to finish copying before moving it.

## Learning Summary

These projects show the progression from direct scripting to reusable automation:

1. Inspect files and move them using functions.
2. Filter and rename files safely with a preview.
3. React to operating-system events with a third-party library.
4. Run a continuous monitoring loop and read system metrics.

The central automation pattern is: **take input -> validate it -> decide what should happen -> perform the operation -> handle failure -> report the result**.
