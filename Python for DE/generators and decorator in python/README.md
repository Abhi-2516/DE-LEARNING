# Generators and Decorators in Python

This lesson turns the original `combined.py` scratchpad into small, runnable examples. The examples use a tea-stall theme to explain lazy iteration, communication with generators, function wrapping, logging, and access control.

## Learning Path

1. [01_basic_generators.py](01_basic_generators.py): `yield`, `next()`, and iteration
2. [02_infinite_generator.py](02_infinite_generator.py): controlled consumption of an infinite stream
3. [03_generator_send.py](03_generator_send.py): sending values into a generator
4. [04_yield_from_and_close.py](04_yield_from_and_close.py): composing and closing generators
5. [05_basic_decorators.py](05_basic_decorators.py): decorator syntax and `wraps`
6. [06_logging_decorator.py](06_logging_decorator.py): `*args`, `**kwargs`, and return values
7. [07_access_control_decorator.py](07_access_control_decorator.py): a practical authorization wrapper
8. [08_chai_pipeline_project.py](08_chai_pipeline_project.py): combine generators and a decorator in a lazy data pipeline

## Run the Examples

From this directory:

```bash
python 01_basic_generators.py
python 02_infinite_generator.py
python 03_generator_send.py
python 04_yield_from_and_close.py
python 05_basic_decorators.py
python 06_logging_decorator.py
python 07_access_control_decorator.py
python 08_chai_pipeline_project.py
```

See [LEARNING_NOTES.md](LEARNING_NOTES.md) for the concepts, common mistakes, and practice tasks.