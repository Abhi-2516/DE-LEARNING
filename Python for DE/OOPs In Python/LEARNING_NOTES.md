# Python OOP Professional Notes

## 1. What OOP solves

Object-oriented programming models a system as collaborating objects. Each object owns state and provides behavior that operates on that state. This is useful when a domain contains entities with identity, rules, and repeated behavior.

Use OOP when objects have meaningful state and behavior together. Prefer simple functions and data structures when the problem is primarily a short transformation pipeline.

## 2. Classes and objects

A class is a blueprint and an object is a concrete instance. `__init__` initializes an object after Python creates it. `self` is the instance passed to an instance method; it is not a reserved keyword, but `self` is the standard name.

```python
class Chai:
    category = "Beverage"

    def __init__(self, tea_type):
        self.tea_type = tea_type

    def describe(self):
        return f"{self.tea_type} chai"
```

## 3. Attributes and lookup

- Instance attributes belong to one object: `order.size`.
- Class attributes are shared through the class: `Chai.category`.
- If an instance attribute has the same name as a class attribute, it shadows the class value for that instance.
- Python generally looks up an attribute on the instance, then its class, then base classes.
- `obj.__dict__` shows most instance attributes; `Class.__dict__` shows the class namespace.

Avoid mutable class attributes such as `items = []` when each object should have its own list. Create them in `__init__` instead.

## 4. Methods

Instance methods receive `self` and work with object state. `@classmethod` receives `cls` and is useful for alternate constructors or class-level behavior. `@staticmethod` receives neither automatically and is suitable for a utility logically grouped with a class.

## 5. Encapsulation and properties

Python uses conventions rather than strict access control:

- `name` is public.
- `_name` means internal or protected by convention.
- `__name` triggers name mangling and discourages accidental access.

A property provides attribute-style access while allowing validation or computed values. Keep invariants in one place, usually a property setter or a domain method. For example, an account should reject negative balances rather than trusting every caller.

## 6. Inheritance

Inheritance expresses an **is-a** relationship. A subclass receives behavior from a base class and can extend or override it. Use `super()` to cooperate with the next implementation in the method resolution order instead of naming a parent directly.

Inheritance is helpful for a stable shared interface. Do not use it only to avoid a few duplicated lines; composition is often clearer.

## 7. Polymorphism and abstraction

Polymorphism means code can use different objects through the same interface. `checkout()` in `06_polymorphism_and_abstraction.py` accepts any payment method that implements `pay()`.

`abc.ABC` and `@abstractmethod` define an interface that subclasses must implement. Python also supports duck typing: if an object provides the required behavior, its exact class may not matter.

## 8. Composition

Composition expresses a **has-a** relationship. A `Vehicle` has an `Engine`. It keeps components replaceable and usually creates less coupling than a deep inheritance tree. In real systems, composition is often the default design choice.

## 9. MRO and multiple inheritance

The method resolution order determines where Python searches for methods and attributes. Inspect it with `SomeClass.__mro__` or `SomeClass.mro()`. Cooperative multiple inheritance requires each class to call `super()` consistently.

## 10. Dunder methods and dataclasses

Dunder methods customize Python protocols:

- `__str__`: user-friendly display.
- `__repr__`: debugging representation.
- `__eq__`: equality behavior.
- `__lt__`: less-than comparison.
- `__len__`, `__iter__`, and `__contains__`: collection protocols.

`@dataclass` generates common methods for data-focused classes. `frozen=True` makes the generated instance immutable by convention and prevents normal field reassignment.

## Design checklist

1. Give each class one clear responsibility.
2. Keep invariants close to the state they protect.
3. Prefer descriptive public methods over direct mutation.
4. Favor composition when the relationship is not genuinely `is-a`.
5. Keep inheritance shallow and interfaces small.
6. Add type hints and docstrings to public APIs.
7. Make invalid states difficult to create.
8. Test behavior through the public interface.

## Revision questions

1. What is the difference between a class attribute and an instance attribute?
2. Why can a property be safer than exposing a raw field?
3. When is composition clearer than inheritance?
4. How does overriding support polymorphism?
5. What does `super()` follow in a multiple-inheritance hierarchy?
6. Which dunder method would you implement to make an object printable?

## Common mistakes

- Defining per-object mutable data at class level.
- Forgetting `self` in an instance method.
- Repeating parent initialization instead of using `super()`.
- Treating `_field` as truly private; it is only a convention.
- Building large inheritance trees for unrelated behavior.
- Allowing public mutation to bypass validation.
