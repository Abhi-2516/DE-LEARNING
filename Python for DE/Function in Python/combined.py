# # # # # # # # # # Learning function in Python
# # # # # # # # # # fuction helps to remove code duplication and helps us to create an reusable piece of code

# # # # # # # # # def print_order(name , types):
    
# # # # # # # # #     print(f"{name} order chai : {types}")
    
# # # # # # # # # print_order("aman" , "masala")
# # # # # # # # # print_order("hitesh" , "mint")

# # # # # # # # # #funtion ke andrn parameter jata hia or function call krte vkty argument pass krte hein


# # # # # # # # # # create an mointholy reportt for an cafe : spliting the complex task

# # # # # # # # # def fetch_sales():
# # # # # # # # #     print("fething the sale data")

# # # # # # # # # def filter_valid_sales():
# # # # # # # # #     print("filternig valid sales data")
    
# # # # # # # # # def summarize_Data():
# # # # # # # # #     print("sumarzing the data")

# # # # # # # # # def generate_report():
# # # # # # # # #     fetch_sales()
# # # # # # # # #     filter_valid_sales()
# # # # # # # # #     summarize_Data()
    
# # # # # # # # # generate_report()
    


# # # # # # # # # now function to hide implementtaion details

# # # # # # # # def get_inpput():
# # # # # # # #     print("getting user input .....")
# # # # # # # # def valid_inppppppput():
# # # # # # # #     print("validating data")
# # # # # # # # def save_to_db():
# # # # # # # #     print("saved to db")

# # # # # # # # def user_reg():
# # # # # # # #     get_inpput()
# # # # # # # #     valid_inppppppput()
# # # # # # # #     save_to_db()
# # # # # # # #     print("User registration is compelete")
    
# # # # # # # # user_reg()


# # # # # # # #retuning somwthing in funtion

# # # # # # # # def calculate_bills(cups,price_per_cup):
# # # # # # # #     return cups * price_per_cup

# # # # # # # # my_bill = calculate_bills(3,45)

# # # # # # # # print(my_bill)

# # # # # # # #improving teracebiluity

# # # # # # # def vat(price , vat_rate):
# # # # # # #     return price * (100 + vat_rate)/100

# # # # # # # ord = [100,200,300]

# # # # # # # for p in ord:
# # # # # # #     final_amout = vat(p , 10)
# # # # # # #     print(f"original amount is {p} final is : {final_amout}")


    
# # # # # # Student Grading System
# # # # # # You’re building an academic grading system.

# # # # # # Tasks:

# # # # # # Define a function calculate_grade(score) that:

# # # # # # Returns “A” for score ≥ 90

# # # # # # “B” for ≥ 75

# # # # # # “C” for ≥ 60

# # # # # # “D” for ≥ 40

# # # # # # “F” otherwise

# # # # # # Define a second function generate_student_report(name, score) that:

# # # # # # Uses the first function to determine the grade.

# # # # # # Returns a report string like: "Aman has scored 80 and received grade B"

# # # # # # Write clean, reusable code using functions, conditions, and string formatting.


# # # # # # def calculate_grade(score):
# # # # # #     if score >= 90:
# # # # # #         return "A"
# # # # # #     elif score >= 75:
# # # # # #         return "B"
# # # # # #     elif score >= 60:
# # # # # #         return "C"
# # # # # #     elif score >= 40:
# # # # # #         return "D"
# # # # # #     else:
# # # # # #         return "F"
            
# # # # # # def generate_student_report(name , score):
# # # # # #     grade = calculate_grade(score)
# # # # # #     return f"{name} has scored {score} and received grade {grade}"


# # # # # ## Scops in funtion

# # # # # #local - inside an funtion
# # # # # #enclosiog from outer sduntion
# # # # # # global - top level script
# # # # # #built in  like - print def etc


# # # # # def serve_chai():
# # # # #     chai_type = "Masala" # local scope
# # # # #     print(f"Inside function {chai_type}")


# # # # # chai_type = "Lemon"
# # # # # serve_chai()
# # # # # print(f"Outside function: {chai_type}")


# # # # # def chai_counter():
# # # # #     chai_order = "lemon" # Enclosing scope
# # # # #     def print_order():
# # # # #         chai_order = "Ginger"
# # # # #         print("Inner:", chai_order)
# # # # #     print_order()
# # # # #     print("Outer: ", chai_order)

# # # # # chai_order = "Tulsi" # Global
# # # # # chai_counter()
# # # # # print("Global :", chai_order)


# # # # #NOnlocal vs global scopes

# # # # def update_order ():
# # # #     chai_t = "elachi"
    
# # # #     def kit():
# # # #         nonlocal chai_t
# # # #         chai_t = "kesar"
# # # #     kit()
    
# # # # # glocbal scopes

# # # # chaiT = "Plain"
# # # # def front_desk():
# # # #     def kit():
# # # #         global chaiT
# # # #         chaiT = "NORM"
# # # #     kit()
    
# # # # # global is outhisde the fnctiona ndnonlocal is iinside te funtion


# # # # # This function will be tested automatically.
# # # # # Do not change the function name or parameters.
 
# # # # loyalty_points = 0  # global variable
 
# # # # def process_transactions(transactions: list[int]) -> int:
# # # #     # Write your code below this line
# # # #     def apply_bonus():
# # # #         nonlocal total
# # # #         if total > 1000:
# # # #             total += 50  # bonus for high spenders
 
# # # #     total = 0
 
# # # #     for amount in transactions:
# # # #         total += amount
 
# # # #     apply_bonus()
 
# # # #     # update global loyalty_points
# # # #     global loyalty_points
# # # #     loyalty_points += total // 100  # earn 1 point per ₹100
 
# # # #     return total


# # # #handling argument

# # # # chai = "Ginger chai"

# # # # def prepare_chai(order):
# # # #     print("Preparing ", order)


# # # # prepare_chai(chai)
# # # # print(chai)


# # # chai = [1, 2, 3]

# # # def edit_chai(cup):
# # #     cup[1] = 42

# # # edit_chai(chai)
# # # print(chai)


# # # def make_chai(tea, milk, sugar):
# # #     print(tea, milk, sugar)

# # # make_chai("Darjeeling", "Yes", "Low") #positional
# # # make_chai(tea="Green", sugar="Medium", milk="No") #keywords


# # # def special_chai(*ingredients, **extras):
# # #     print("Ingredients", ingredients)
# # #     print("Extras", extras)

# # # special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes")
# # #  #args and kwargsa are clear here
 
# # # # def chai_order(order=[]):
# # # #     order.append("Masala")
# # # #     print(order)

# # # def chai_order(order=None):
# # #     if order is None:
# # #         order = []
# # #     print(order)

# # # chai_order()
# # # chai_order()


# # # This function will be tested automatically.
# # # Do not change the function name or parameters.
 
# # def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
# #     # Write your code below this line
# #     total = 0.0
# #     invoice_lines = [f"Invoice for {customer_name}:"]
 
# #     if items:
# #         invoice_lines.append("Items:")
# #         for item in items:
# #             invoice_lines.append(f"- {item}")
 
# #     if charges:
# #         invoice_lines.append("Charges:")
# #         for label, amount in charges.items():
# #             invoice_lines.append(f"{label.capitalize()}: {amount}")
# #             total += amount
 
# #     invoice_lines.append(f"Total Amount Due: {total}")
# #     return "\\n".join(invoice_lines)


# #haldling multiple inputs in function
# def makechai():
#     return "chai is printin"

# print(makechai())


#ypes of function:

#pure vs impure function , recursdioe , no name fxn -> lmbda function

#pure
# def chai(cups):
#     return cups *20

# #impure -> thery alrter global varibale not recombded
# #recursive:
#     def pur(n):
#         if n ==0:
#             return "aLL CUPS ARE POUR"
#         return pur(n-1)
    
    
#lmbda function

# chai = ["l","k","l","g"]

# strong = list(filter(lambda chai: chai == 'l' , chai))

# print(strong)


#Built in function
#study this with exmaple

## Import in python

