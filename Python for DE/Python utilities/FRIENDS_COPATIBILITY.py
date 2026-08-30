# """
#  Challenge: Friendship Compatibility Calculator

# Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

# Your program should:
# 1. Ask for two names (friend A and friend B).
# 2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
# 3. Display the percentage with a themed message like:
#    "You're like chai and samosa — made for each other!" or 
#    "Well... opposites attract, maybe?"

# Bonus:
# - Use emojis in the result
# - Give playful advice based on the score range
# - Capitalize and center the final output in a framed box
# """

def friendsscore(name1, name2):
    name1 , name2 = name1.lower() , name2.lower()
    
    score = 0
    
    shared_char = set(name1) & set(name2)
    vowels = set('aeiou')
    
    score += len(shared_char) * 5
    
    score += len(vowels & shared_char) * 10
    
    
    return min(score , 100)


def run_frein():
    print("friendship compatibilyt calculator : ")
    name1 = input("Enter the firs name") 
    name2 = input("Enter the sec name") 
    
    score = friendsscore(name1,name2)
    
    print(f"SCORE IS : {score}")

run_frein()
    
