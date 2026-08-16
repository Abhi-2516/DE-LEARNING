#LOOP is generally used to iterate or acess something again and again

# tea token dispenser problem to print token number 1 -10

# for token in range (1,11):
#     print(f"Serving chai with token #{token}")


#batch priont for an tea dispenser

# for batch in range (1,5):
#     print(f"bathc is {batch}")

#Generate Multiplication Table
# You are developing a feature in an educational app that displays multiplication tables.

# Tasks:

# Write a function named multiplication_table that takes a single integer argument number.

# Using a for loop and range(), generate the multiplication table for number from 1 to 10.

# Return a list of strings in the following format:

# "number x i = result"

# (Example: "3 x 4 = 12")

# #solution 
# def multiplication_table(number: int) -> list[str]:
#     result = []
#     for i in range(1, 11):
#         result.append(f"{number} x {i} = {number * i}")
#     return result

# looping thoroug list

# orders = ["abhi" , "sonu" ,"hitesh"]

# for name in orders:
#     print(f"order is ready for {name}")

# def mark_completed_tasks(tasks: list[str]) -> list[str]:
#     # Write your code below this line
#     completed = []
#     for task in tasks:
#         completed.append(f"Completed: {task}")
#     return completed

##Important : Use of Enumerate ?
# you are creating a tea menu board Each item must be numbered  task is to poront menu otems with number using enumerate

# menu = ["green" , "leamon" , " spiced" , "mint"]


# for idx , itm in enumerate(menu , start=1):
#     print(f"{idx} : {itm} chai")

# Numbered Task List
# You’re improving the UX of a task management app by numbering the user’s task list automatically.



# Tasks:

# Define a function generate_numbered_tasks that takes a list of task names.

# Use the enumerate() function to loop through the list with numbering starting from 1.

# Format each task as "1. Task Name" and return the final list.


# # This function will be tested automatically. 
# # Do not change the function name or parameters.
# def generate_numbered_tasks(tasks: list[str]) -> list[str]:
#     # Write your code below this line
#     numbered_tasks = []
#     for index, task in enumerate(tasks, start=1):
#         numbered_tasks.append(f"{index}. {task}")
#     return numbered_tasks


# #preparing order sumary 
# names = ["abhi" , "sam" , "ram","hitesh"]
# bills = [100,2000,500,1400]

# # we study zipa bout here

# for name , amount in zip (names,bills):
#     print(f"{name}  paid : {amount} paisa")
#     print(f"{name}  paid : {bills} rupees")
#     print(f"{name}  paid : {bills} rupees")
#     print(f"{name}  paid : {bills} rupees")


# Student Scores Report
# You’re building a simple student report generator that combines names and scores.

# Tasks:

# Define a function generate_score_report that takes two lists — one with student names and one with their scores.

# Use the zip() function to pair each student with their score.

# Return a list of strings in the format "Name scored X marks"

# # This function will be tested automatically. 
# # Do not change the function name or parameters.
# def generate_score_report(names: list[str], scores: list[int]) -> list[str]:
#     # Write your code below this line
#     ans = []
#     for name , score in zip(names, scores):
#         ans.append(f"{name} scored {score} marks")
#     return ans



# while loop 

# temp = 40

# while (temp <= 100):
#     print(f"cur temp {temp}")
#     temp = temp +15;

# print("tea is ready to boiled")

# ATM Withdrawal Simulator
# Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. Your task is to simulate how the system should handle each request based on the account balance.

# Tasks:

# Use a while loop to iterate through the list named withdrawals.

# For every withdrawal:

# ✅ If the current balance is enough:

# Subtract the amount.

# Append a success message: "Withdrawn: {amount}"

# ❌ If not enough:

# Append a message: "Insufficient funds for requested amount: {amount}"

# After all withdrawals:

# Append the final balance as: "Remaining Balance: balance"

# Return a list containing all the messages.





# # This function will be tested automatically. 
# # Do not change the function name or parameters.
# def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
#     # Write your code below this line
#     result = []
#     index = 0
#     while index < len(withdrawals):
#         amount = withdrawals[index]
#         if amount <= balance:
#             balance -= amount
#             result.append(f"Withdrawn: {amount}")
#         else:
#             result.append(f"Insufficient funds for requested amount: {amount}")
#         index += 1
#     result.append(f"Remaining Balance: {balance}")
#     return result


#break , skip , continue in pythoon

# flavours = ["ginger" , "leamon" , "out of stock" , "discontionued" , "tulsi" ]

# for flav in flavours:
#     if flav == "out of stock":
#         continue
#     if flav == "discontinued":
#         print(f"{flav}  item found")
#         break


#WALRUS operator (:=)

# value  = 13 
# if (reminder := value%5):
#     print(f"remainde is {reminder}")


#use dictinary in place of reapered cases

users = [
    {"id" : 1, "total" : 100, "coupen" : "P20"},
    {"id" : 2, "total" : 150, "coupen" : "F10"},
    {"id" : 3, "total" : 80, "coupen" : "P50"}
    
]
discount = {
    "P20" : (0.2,0),
    "F10" : (0.5,0),
    "P50" : (0,10),
}

for user in users:
    percent, fixed = discount.get(user["coupen"] ,(0,0))
    discount_amount = user["total"] * percent + fixed
    
    print(f"{user["id"]} paid {user["total"]} got discount {discount_amount}")

