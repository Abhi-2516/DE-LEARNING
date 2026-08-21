# Object-Oriented Programming in Python

A structured OOP reference built from the concepts studied in `combined.py`. Each numbered file is independent and runnable with Python.

## Learning path

| File | Focus |
| --- | --- |
| `01_classes_and_objects.py` | Classes, objects, attributes, and methods |
| `02_attributes_and_methods.py` | Instance state, class state, and shadowing |
| `03_constructors_and_class_methods.py` | `__init__`, alternate constructors, and class state |
| `04_encapsulation_and_properties.py` | Validation, properties, and controlled mutation |
| `05_inheritance_and_method_overriding.py` | Reuse, `super()`, and overriding |
| `06_polymorphism_and_abstraction.py` | Abstract interfaces and polymorphism |
| `07_composition.py` | Has-a relationships and object collaboration |
| `08_class_static_methods_and_mro.py` | Static methods, class methods, and MRO |
| `09_dunder_methods_and_dataclasses.py` | Python data-model methods and dataclasses |

## How to run

From this directory:

```text
python 01_classes_and_objects.py
python 06_polymorphism_and_abstraction.py
```

Run all examples in PowerShell:

```powershell
Get-ChildItem -Filter '*.py' | Where-Object { $_.Name -ne 'combined.py' } | ForEach-Object { python $_.FullName }
```

## Core mental model

A **class** defines a reusable type. An **object** is an instance of that type. Attributes represent state, while methods represent behavior. Good object-oriented design keeps related state and behavior together and exposes a small, meaningful public interface.

For detailed explanations, definitions, design guidance, and revision questions, see [`LEARNING_NOTES.md`](LEARNING_NOTES.md).
