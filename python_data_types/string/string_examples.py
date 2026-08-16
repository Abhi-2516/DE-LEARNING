# Python String Examples
# This file demonstrates common string operations in Python.

# 1. Creating strings
name = "Python"
course = 'Programming'
message = """This is a multi-line string."""
print("1. Strings:")
print(name, course, message)

# 2. Indexing
text = "Hello World"
print("\n2. Indexing:")
print(text[0])
print(text[6])
print(text[-1])

# 3. Slicing
print("\n3. Slicing:")
print(text[0:5])
print(text[:5])
print(text[6:])
print(text[::-1])

# 4. String length
print("\n4. Length:")
print(len(text))

# 5. Concatenation
first = "Hello"
last = "World"
print("\n5. Concatenation:")
print(first + " " + last)
print((first + " ") * 3)

# 6. Case conversion
print("\n6. Case conversion:")
word = "hitesh"
print(word.upper())
print(word.capitalize())
print(word.title())

# 7. Strip methods
print("\n7. Strip methods:")
value = "   python   "
print(value.strip())
print(value.lstrip())
print(value.rstrip())

# 8. Replace
print("\n8. Replace:")
sentence = "I love Java"
print(sentence.replace("Java", "Python"))

# 9. Split and join
print("\n9. Split and join:")
quote = "Python is easy and fun"
words = quote.split()
print(words)
print("-".join(words))

# 10. Find, index, count
print("\n10. Find and count:")
text2 = "banana"
print(text2.count('a'))
print(text2.find('na'))
print(text2.index('n'))

# 11. Startswith / endswith
print("\n11. Startswith / endswith:")
file_name = "script.py"
print(file_name.startswith("s"))
print(file_name.endswith("py"))

# 12. Checking string properties
print("\n12. String checks:")
value1 = "12345"
value2 = "abc123"
print(value1.isdigit())
print(value2.isalnum())
print("hello".islower())
print("HELLO".isupper())

# 13. Membership test
print("\n13. Membership:")
print('h' in 'hello')
print('z' not in 'hello')

# 14. Formatting with f-string
print("\n14. Formatting:")
name = "Amit"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 15. Formatting with .format()
print("\n15. .format example:")
print("Name: {} | Age: {}".format("Amit", 25))

# 16. Escape sequences
print("\n16. Escape sequences:")
print("Hello\nWorld")
print("Tab\tExample")
print("Quote: \"Python\"")

# 17. Raw strings
print("\n17. Raw strings:")
path = r"C:\Users\Admin\Desktop\file.txt"
print(path)

# 18. Multiline string
print("\n18. Multiline string:")
poem = """Python is fun,
It is simple,
And powerful."""
print(poem)

# 19. Reversing a string
print("\n19. Reverse string:")
word = "python"
print(word[::-1])

# 20. Palindrome check
print("\n20. Palindrome check:")
value = "level"
print(value == value[::-1])

# 21. Remove spaces from a string
print("\n21. Remove spaces:")
text3 = "P y t h o n"
print(text3.replace(" ", ""))

# 22. Iterate over characters
print("\n22. Iteration:")
for ch in "Python":
    print(ch, end=" ")
print()

# 23. Unicode strings
print("\n23. Unicode:")
print("नमस्ते")
print("😊")

# 24. Encode and decode
print("\n24. Encode/Decode:")
text = "Hello"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))

# 25. Example program
print("\n25. Example program:")
student_name = "Hitesh"
message = f"Hello {student_name}! Welcome to Python strings tutorial."
print(message)
print(student_name.upper())
print(student_name.lower())
print(len(student_name))

# 26. Common interview-style exercise
print("\n26. Count vowels:")
text4 = "hello world"
vowels = "aeiou"
count = sum(1 for ch in text4 if ch.lower() in vowels)
print(count)

# 27. Extra example: substring check
print("\n27. Substring check:")
main_text = "Python Programming"
print("Python" in main_text)
print("Java" in main_text)

# End of file
print("\nAll string examples completed.")
