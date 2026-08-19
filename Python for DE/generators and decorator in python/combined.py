# # # # # generator mean we are generating a things and we get only one value at a time

# # # # # yield is a keyword you in  generators it resposnsible for pasuns and executing the sentence and mail thig in generator


# # # # def srve_chai():
# # # #     yield "chup  1 : m"
# # # #     yield "chup  1 : m"
# # # #     yield "chup  1 : m"
# # # #     yield "chup  1 : m"
    
# # # # stall = srve_chai()
# # # # print(next(stall))
# # # # print("next wala done")

# # # # for cup in stall:
# # # #     print(cup)z
    

# # # #infinite generators
# # # # def infinte_chai():
# # # #     count = 1
# # # #     while True:
# # # #         yield f"Refil #{count}"
# # # #         count = count +1
# # # # refill = infinte_chai()

# # # # for _ in range (5):
# # # #     print(next(refill))


# # # # send value for genrators

# # # # def chai_customer():
# # # #     print ("welcome")
# # # #     order = yield
# # # #     while True:
# # # #         print(f"prepe: {order}")
# # # #         order = yield # if not this it will run infinte time
        
# # # # stall =chai_customer()
# # # # next(stall)

# # # # stall.send ("mask")


# # # #yiled from and close generator

# # # # def  local_chai():
# # # #     yield "masala"
# # # #     yield "gigner"

# # # # def imported_Chai():
# # # #     yield "matcha"
# # # #     yield "oolong"
    
# # # # def fuul():
# # # #     yield from local_chai()
# # # #     yield from imported_Chai()
    
# # # # for chai in fuul():
# # # #     print(chai)
    
# # # # def chai_stall():
# # # #     try:
# # # #         pass
# # # #     except:
# # # #         pass



# # # ## Decorators in Python

# # # # way of decoration
# # # from functools import wraps
# # # def my_decorator(func):
# # #     @wraps(func)
# # #     def wrapper():
# # #         print("Before function runs")
# # #         func()
# # #         print("After function runs")
# # #     return wrapper

# # # @my_decorator
# # # def greet():
# # #     print("Hello from decorators class from chaicode")


# # # greet()
# # # print(greet.__name__)



# # # bulding an loging decorator

# # from functools import wraps

# # def log_activity(func):
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         print(f"🚀 Calling: {func.__name__}")
# #         result = func(*args, **kwargs)
# #         print(f"✅ Finished: {func.__name__}")
# #         return result
# #     return wrapper

# # @log_activity
# # def brew_chai(type, milk="no"):
# #     print(f"Brewing {type} chai and milk status {milk}")

# # brew_chai("Masala")

# from functools import wraps

# def require_admin(func):
#     @wraps(func)
#     def wrapper(user_role):
#         if user_role != "admin":
#             print("Access denied: Admins only")
#             return None
#         else:
#             return func(user_role)
#     return wrapper

# @require_admin
# def acess_tea_inventory(role):
#     print("Access granted to tea inventory")

# acess_tea_inventory("user")
# acess_tea_inventory("admin")