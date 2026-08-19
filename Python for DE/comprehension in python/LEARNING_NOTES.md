# Learning Notes: Comprehensions

## What Is a Comprehension?

A comprehension creates a new collection from an iterable in one expression. It can transform each value, filter values, or do both.

The general list shape is:

```python
[expression for item in iterable if condition]
```

Read it as: “for each item, include the expression when the condition is true.” The `if` part is optional.

## Four Main Forms

| Form | Result | Best use |
|---|---|---|
| List comprehension | `list` | Ordered transformed or filtered values |
| Set comprehension | `set` | Unique values |
| Dictionary comprehension | `dict` | Key-value mappings |
| Generator expression | `generator` | Lazy, memory-efficient processing |

```python
squares = [number**2 for number in numbers]
unique_names = {name.lower() for name in names}
prices = {item["name"]: item["price"] for item in items}
total = sum(amount for amount in amounts if amount > 0)
```

## Important Details

- Comprehensions do not modify the original iterable.
- Sets remove duplicates and do not guarantee list-like order.
- Dictionary keys must be unique; a later value replaces an earlier value for the same key.
- A generator expression produces values when requested instead of creating them all immediately.
- `list(generator)` consumes the generator. It cannot be restarted afterward.
- Use `round()` when decimal output needs a defined precision. Use `int()` only when truncating decimals is intentional.

## Nested Comprehensions

The order follows normal nested loops:

```python
flattened = [item for group in groups for item in group]
```

This is equivalent to:

```python
flattened = []
for group in groups:
    for item in group:
        flattened.append(item)
```

Use a normal loop when the comprehension becomes difficult to read, contains several conditions, or needs error handling.

## Choosing the Right Form

- Need duplicates and order? Use a list comprehension.
- Need unique values? Use a set comprehension.
- Need lookup by key? Use a dictionary comprehension.
- Need one-pass processing of large data? Use a generator expression.
- Need multiple side effects? Use a normal `for` loop; comprehensions should create data, not perform actions.

## Common Mistakes

### Replacing the input parameter

A function should process its argument, not overwrite it with sample data. Keep sample data inside the `if __name__ == "__main__":` block.

### Confusing transformation and filtering

```python
[number * 2 for number in numbers if number > 3]
```

`number * 2` transforms the value; `number > 3` filters the input.

### Hiding complicated logic

Prefer a named helper function or a regular loop when the expression needs nested business rules. Shorter code is not automatically clearer code.

## Practice Tasks

1. Create a list of usernames in lowercase, excluding empty strings.
2. Build a set of domains from a list of email addresses.
3. Create a dictionary mapping product names to stock quantities.
4. Use a generator expression to sum only positive transactions.
5. Extend the inventory project to return products priced between ₹200 and ₹800.

## What We Learned

You learned how to transform, filter, deduplicate, map, flatten, and lazily process data with Python comprehensions. The inventory project combines list, set, dictionary, and generator expressions in one practical workflow.
