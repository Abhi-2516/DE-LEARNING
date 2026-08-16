# Project 5: While Loops

## 📋 Project Description

Demonstrates condition-based iteration using while loops. Includes temperature monitoring, ATM simulation, and user input validation.

## 🎯 Learning Objective

Learn to create loops that execute based on conditions rather than a count, and handle scenarios where iteration count is unknown.

## 💡 Concept Breakdown

### While Loop Syntax

```python
while condition:
    # Code executes while condition is True
    # MUST modify condition to avoid infinite loop!
```

### Key Difference from For Loop

| For Loop | While Loop |
|----------|-----------|
| Count-based | Condition-based |
| Known iterations | Unknown iterations |
| `for i in range(10):` | `while x < 10:` |
| Less error-prone | More error-prone (infinite loops) |

## 🔑 Key Concepts

| Concept | Explanation | Example |
|---------|-------------|---------|
| **Condition** | Expression that's checked each loop | `while balance > 0:` |
| **True/False** | Condition must be boolean | `temp <= 100` |
| **Update** | Must change condition inside loop | `temp = temp + 15` |
| **Infinite Loop** | Never-ending loop (bug!) | Missing update |

## 📊 Common Patterns

### Basic Count Pattern
```python
count = 0
while count < 10:
    print(count)
    count += 1  # Must update!
```

### While True with Break
```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Exit loop
    process(user_input)
```

### Input Validation
```python
age = -1  # Invalid initial value
while age < 0 or age > 120:
    age = int(input("Enter valid age: "))
    # Loop continues until valid
```

## 🚀 How to Run

```bash
python while_loops.py
```

## 💻 Try It Yourself

1. Create a guessing game
2. Validate user input
3. Process until sentinel value
4. Implement countdown timer
5. Create ATM-like system

## ⚠️ Common Mistakes

### ❌ Infinite Loop (No Update)
```python
# WRONG - Infinite loop!
count = 0
while count < 10:
    print("Help!")
    # count never changes!

# CORRECT
count = 0
while count < 10:
    print(count)
    count += 1  # Update condition
```

### ❌ Wrong Condition
```python
# WRONG - Loop exits immediately
x = 10
while x > 20:  # x is 10, not > 20!
    print(x)
    x += 1
# Output: Nothing!

# CORRECT
while x < 20:
    print(x)
    x += 1
```

### ❌ Off-by-One Error
```python
# WRONG - Skips last iteration
x = 1
while x < 10:  # Stops at 9
    print(x)
    x += 1

# CORRECT - Include last value
while x <= 10:  # Includes 10
    print(x)
    x += 1
```

### ❌ Break in Nested Loop
```python
# WRONG - break only exits inner loop
while True:
    while True:
        if condition:
            break  # Only breaks inner!
    # Still in outer loop!

# CORRECT - Use flag or function
def inner_loop():
    while True:
        if condition:
            return True
    return False

if inner_loop():
    break
```

## 📝 Extended Examples

### Example 1: Guessing Game
```python
def guessing_game(secret: int, max_attempts: int = 5):
    attempts = 0
    while attempts < max_attempts:
        guess = int(input("Guess the number: "))
        if guess == secret:
            print("Correct!")
            return True
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")
        attempts += 1
    print("Game over!")
    return False
```

### Example 2: Input Validation
```python
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 150:
                return age
            print("Please enter age between 0 and 150")
        except ValueError:
            print("Invalid input. Enter a number.")
```

### Example 3: ATM Withdrawal
```python
def atm_session(balance: int):
    while True:
        amount = int(input("Withdraw amount (0 to exit): "))
        if amount == 0:
            print(f"Remaining balance: ${balance}")
            break
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn: ${amount}, Balance: ${balance}")
        else:
            print("Insufficient funds")
```

### Example 4: Process Until Sentinel
```python
def sum_until_negative():
    total = 0
    while True:
        num = int(input("Enter number (-1 to stop): "))
        if num == -1:
            break
        total += num
    print(f"Total: {total}")
```

## 🔄 Real-World Applications

- ✅ User input validation
- ✅ Game loops
- ✅ Server request handling
- ✅ File processing
- ✅ Sensor monitoring
- ✅ Data collection
- ✅ Authentication attempts

## 📊 While vs For Loop Decision

**Use While when:**
- Iteration count is unknown
- Condition-based termination
- Input-dependent loops
- Event-driven processing

**Use For when:**
- Know exact iteration count
- Processing collections
- Iterating through ranges
- Number of items is fixed

## 💡 Pro Tips

1. **Always initialize condition variables**
   ```python
   count = 0  # Initialize before loop
   while count < 10:
       print(count)
       count += 1
   ```

2. **Update condition inside loop**
   ```python
   while True:
       action()  # Perform action
       if should_exit():
           break  # Update condition
   ```

3. **Use meaningful conditions**
   ```python
   # Good
   while user_input != "quit":
   
   # Bad
   while True:
   ```

4. **Add safety limits**
   ```python
   max_attempts = 5
   attempts = 0
   while attempts < max_attempts:
       # Prevents infinite attempts
       attempts += 1
   ```

## 🎯 Next Steps

- [ ] Run the program
- [ ] Create guessing game
- [ ] Implement input validation
- [ ] Build ATM simulator
- [ ] Learn about loop control (break, continue)

## 📚 Related Concepts

- **Break Statement:** Exit loop early
- **Continue Statement:** Skip iteration
- **For Loops:** Alternative to while
- **Try-Except:** Error handling in loops

---

**Difficulty Level:** ⭐⭐⭐ (Intermediate)  
**Time to Complete:** 20-30 minutes  
**Prerequisites:** For loops, conditionals
