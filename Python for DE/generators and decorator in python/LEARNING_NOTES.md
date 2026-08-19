# Learning Notes: Generators and Decorators

## Generators

A generator function contains `yield`. Calling it returns a generator object; the function body does not run until `next()` or a `for` loop requests a value. Each `yield` pauses execution and remembers the local state.

```python
def numbers():
    yield 1
    yield 2

for number in numbers():
    print(number)
```

Generators are useful for large files, database results, and streams because they produce values lazily instead of storing every result in memory.

### Generator Tools

- `next(generator)` requests one value.
- `for item in generator` keeps requesting values until `StopIteration`.
- `send(value)` resumes a paused generator and makes the value available to its `yield` expression.
- `yield from other_generator()` delegates iteration to another generator.
- `close()` stops a generator when no more values are needed.

An infinite generator must always be consumed with a limit, a condition, or a tool such as `itertools.islice`.

## Decorators

A decorator is a callable that receives a function and returns a replacement function. The `@decorator` syntax is equivalent to reassigning the function:

```python
@log_activity
def brew_chai():
    pass
```

This is equivalent to `brew_chai = log_activity(brew_chai)`. The wrapper can add logging, timing, validation, authorization, caching, or retry behavior.

Use `functools.wraps` so the wrapped function keeps useful metadata such as `__name__` and its docstring. Use `*args` and `**kwargs` when the decorator should work with different function signatures. Always return the wrapped function's result unless intentionally changing the contract.

## Generators vs. Lists

| Choose a generator when... | Choose a list when... |
|---|---|
| the data may be large | you need repeated access |
| values are consumed once | you need indexing or `len()` |
| work should happen on demand | all values are already small |

## Common Mistakes

- Calling `next()` after a generator is exhausted raises `StopIteration`.
- Calling `send()` before the first `yield` raises `TypeError`; prime the generator with `next()` first.
- An infinite generator can hang a program if converted directly with `list()`.
- A decorator wrapper that omits `return` silently discards the original function's result.
- A decorator that omits `wraps` hides the original function metadata.
- Authorization decorators should validate the role before calling the protected function.

## Practice Tasks

1. Write a generator that yields even numbers from 2 through 20.
2. Build an infinite order-number generator and consume only the first five values.
3. Create a generator that receives customer names with `send()` and prints a greeting.
4. Write a decorator that counts how many times a function is called.
5. Write a decorator that rejects a negative quantity before an order is processed.
6. Extend the capstone to skip unknown tea names and yield a summary count.

## What We Learned

Generators provide lazy, stateful iteration. Decorators extend function behavior without changing the function body. Together they support clean data pipelines: generate or transform records on demand, then wrap the pipeline with cross-cutting behavior such as logging or authorization.