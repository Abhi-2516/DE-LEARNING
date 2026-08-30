# """
#  Challenge: Password Strength Checker & Suggestion Tool

# Build a Python script that checks the strength of a password based on:
# 1. Length (at least 8 characters)
# 2. At least one uppercase letter
# 3. At least one lowercase letter
# 4. At least one digit
# 5. At least one special character (e.g., @, #, $, etc.)

# Your program should:
# - Ask the user to input a password.
# - Tell them what's missing if it's weak.
# - If the password is strong, confirm it.
# - Suggest a strong random password if the input is weak.

# Bonus:
# - Hide password input using `getpass` (no echo on screen).
# """

import string
import random
import getpass


def check_password_Strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short min 8 cHAR NEEDED")
    if not any(c.islower() for c in password):
        issues.append("Missaing lower case letter") 
    if not any(c.isupper() for c in password):
            issues.append("Missaing upper case letter")    
    if not any(c.isdigit() for c in password):
            issues.append("Missaing digit case letter") 
    if not any(c in string.punctuation for c in password):
           issues.append("Missaing punctuation , special char letter")
    
    return issues


def generate_Stringpasswoird(length = 12): 
    chars = string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(length))        


password = getpass.getpass("entrer a pass : ") # user enter the pass but not visible on screen thats the main use of get pass

issues= check_password_Strength(password)

if not issues:
    print("string password yopu are good to go")
else:
    print("weak pass word")
    for i in issues:
        
       print(i)

suggestion = generate_Stringpasswoird()
print("suggesting an strong password : ")
print(suggestion)