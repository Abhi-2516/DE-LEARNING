# Python Strings

A string in Python is a sequence of characters. It is one of the most important and widely used data types.

## 1. What is a string?

In Python, a string is created by placing text inside single quotes, double quotes, or triple quotes.

```python
name = 'Python'
city = "Delhi"
message = '''This is a multi-line string.'''
```

Strings are:
- ordered
- indexed
- immutable
- iterable

## 2. String creation

```python
s1 = "Hello"
s2 = 'World'
s3 = """This is a string with triple quotes"""
s4 = str(12345)
```

## 3. Indexing and slicing

Each character in a string has an index.

```python
text = "Python"
print(text[0])    # P
print(text[1])    # y
print(text[-1])   # n
print(text[0:3])  # Pyt
print(text[:3])   # Pyt
print(text[3:])   # hon
print(text[::-1]) # nohtyP
```

### Important notes
- Indexing starts from 0.
- Negative indexing starts from the end.
- Slicing syntax is: `string[start:end:step]`

## 4. String immutability

Strings cannot be changed after creation.

```python
name = "Alice"
# name[0] = 'K'  # This will raise TypeError
new_name = 'K' + name[1:]
print(new_name)
```

Because strings are immutable, Python creates a new string when you modify it.

## 5. Concatenation and repetition

```python
first = "Hello"
last = "World"
print(first + " " + last)  # Hello World
print(("Hi " * 3))        # Hi Hi Hi
```

## 6. Common string methods

### Length

```python
text = "Python"
print(len(text))  # 6
```

### Case conversion

```python
name = "hitesh"
print(name.upper())      # HITESH
print(name.capitalize()) # Hitesh
print(name.title())      # Hitesh
```

### Strip / trim spaces

```python
text = "   hello world   "
print(text.strip())      # hello world
print(text.lstrip())     # hello world   
print(text.rstrip())     #    hello world
```

### Replace

```python
text = "I love Python"
print(text.replace("Python", "Java"))
```

### Find and count

```python
text = "banana"
print(text.count('a'))    # 3
print(text.find('na'))    # 2
print(text.index('a'))    # 1
```

### Check start/end

```python
text = "python.txt"
print(text.startswith("py"))  # True
print(text.endswith("txt"))   # True
```

### Split and join

```python
sentence = "Python is easy"
words = sentence.split()
print(words)   # ['Python', 'is', 'easy']

joined = "-".join(words)
print(joined)  # Python-is-easy
```

## 7. Membership operators

```python
text = "hello world"
print('h' in text)       # True
print('python' in text)  # False
```

## 8. String comparison

```python
print("apple" == "apple")   # True
print("apple" < "banana")   # True
print("A" < "a")            # True
```

Python compares strings lexicographically using Unicode values.

## 9. Escape sequences

```python
print("Hello\nWorld")      # newline
print("Hello\tWorld")      # tab
print("He said \"Hi\"")  # quote inside string
print("C:\\Users\\Name") # backslashes
```

Common escape sequences:
- `\n` = newline
- `\t` = tab
- `\\` = backslash
- `\"` = double quote
- `\'` = single quote

## 10. Raw strings

```python
path = r"C:\Users\Name\Desktop"
print(path)
```

Raw strings do not process escape sequences.

## 11. Multiline strings

```python
poem = """Python is fun,
It is easy to learn,
And powerful for coding."""
print(poem)
```

## 12. Formatting strings

### Old style: `%`

```python
name = "Amit"
print("Hello %s" % name)
```

### `format()` method

```python
print("My name is {} and I am {} years old".format("Amit", 25))
```

### f-strings (recommended)

```python
name = "Amit"
age = 25
print(f"My name is {name} and I am {age} years old")
```

## 13. Built-in string functions

```python
text = "python programming"
print(text.isalpha())     # False (contains space)
print(text.isdigit())     # False
print(text.islower())     # True
print(text.isupper())     # False
print(text.istitle())     # False
```

Common checks:
- `isalpha()`
- `isdigit()`
- `isalnum()`
- `isspace()`
- `islower()`
- `isupper()`
- `istitle()`

## 14. Reversing a string

```python
text = "python"
reverse = text[::-1]
print(reverse)  # nohtyp
```

## 15. Checking palindrome

```python
word = "level"
print(word == word[::-1])  # True
```

## 16. String iteration

```python
for ch in "Python":
    print(ch)
```

## 17. Unicode and ASCII

Python strings support Unicode by default.

```python
text = "नमस्ते"
print(text)

emoji = "😊"
print(emoji)
```

This means Python can handle many international languages and symbols.

## 18. Strings vs bytes

```python
text = "Hello"
byte_data = text.encode('utf-8')
print(byte_data)  # b'Hello'

plain_text = byte_data.decode('utf-8')
print(plain_text)  # Hello
```

- `str` = text data
- `bytes` = raw binary data

## 19. Regular expressions with strings

Python has the `re` module for advanced pattern matching.

```python
import re
pattern = r"\d+"
text = "My age is 25 and my number is 9876"
print(re.findall(pattern, text))
```

## 20. String performance and memory

Strings are efficient for text storage, but repeated concatenation can be slower because strings are immutable.

Better approach:

```python
parts = ["Python", "is", "great"]
result = " ".join(parts)
print(result)
```

## 21. Useful interview examples

### Count vowels

```python
text = "hello world"
vowels = "aeiou"
count = sum(1 for ch in text if ch.lower() in vowels)
print(count)
```

### Remove spaces

```python
text = "   p y t h o n   "
print(text.replace(" ", ""))
```

### Find duplicate characters

```python
text = "programming"
seen = set()
duplicates = set()
for ch in text:
    if ch in seen:
        duplicates.add(ch)
    else:
        seen.add(ch)
print(duplicates)
```

## 22. Best practices

- Prefer `f-strings` for formatting
- Use `join()` instead of repeated `+` concatenation
- Use `strip()` when cleaning user input
- Be careful with indexing and slicing
- Use `lower()` or `upper()` for case-insensitive comparisons

## 23. Summary

Strings are a core Python data type. They are:
- ordered
- immutable
- indexable
- sliceable
- highly useful for text processing

Mastering strings helps in data parsing, web development, automation, and problem solving.

## 24. Quick example program

```python
name = "Hitesh"
message = f"Hello {name}! Welcome to Python programming."
print(message)

print(name.upper())
print(name.lower())
print(name[::-1])
print(len(name))
```

## 25. Final note

Whenever you work with text in Python, remember that strings are incredibly versatile. Efficient use of string methods and formatting can make your code cleaner and easier to read.
