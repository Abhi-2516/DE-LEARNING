# """
#  Challenge: Simple Bill Splitter

# Write a Python script that helps split a bill evenly between friends.

# Your program should:
# 1. Ask how many people are in the group.
# 2. Ask for each person's name.
# 3. Ask for the total bill amount.
# 4. Calculate each person's share of the bill.
# 5. Display how much each person owes in a clean, readable format.

group = int(input("How many people in the group : "))

friends =[]

for i in range (1, group+1):
    name = input(f"Enter the name of {i} Friends : ")
    friends.append(name)

amount= int(input("Enter the bill amount : "))


bill_per = round(amount/group ,2)

print("\n" + "*" * 40)
for i in friends:
    print(f"{i} owes {bill_per : .2f}")

print("\n" + "*" * 40)

# Example:
# Total bill: ₹1200  
# People: Aman, Neha, Ravi

# Each person owes: ₹400

# Final output:
#   Aman owes ₹400  
#   Neha owes ₹400  
#   Ravi owes ₹400

# Bonus:
# - Round to 2 decimal places
# - Print a decorative summary box
# """



