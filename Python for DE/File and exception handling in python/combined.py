# # # Exception handling
# # orders = ["m" ,"c"]

# # print(orders[2]) # index error

# # #similarly  we have  keyerror  zerdiverror typeerror etc


# #to handle :

# # chai_menu = {"masla" : 30 , "ginge" :40}


# # try:
# #     chai_menu["e"]
    
# # except KeyError:
# #     print("key not exixts")

# def serve_chai(flavour):
#     try:
#         print(f"preparing {flavour} chai ...")
#         if flavour == "unknown":
#             raise ValueError("nor knot flavour")
#     except ValueError as e:
#         print("erroe :" ,e)
#     else:
#         print(f"{flavour} chai served")
#     finally:
#         print("Next customer")
        
        
# serve_chai("masala")
# serve_chai("unknown")

# handling muktipole excwotion

# def process_order(item , quantity):
#     try:
#         price = {"masala" : 20}[item]
        
#         cost = price + quantity
        
#         print(f"cost is {cost}")
#     except KeyError:
#         print("not availble chai")
#     except TypeError:
#         print("number de de bhai")
        
# process_order("ginger" ,  2)
# process_order("masala" , "two")


#raise your own error

# def brew_chai(flavour):
#     if flavour not in ["masala" , "ginger" ,"lemon"]:
#         raise ValueError("usported chai"
#                          )
#     print(f"brew {flavour} chai ...")
    
# brew_chai("mint")

#creating own expection
# class outofind(Exception):
#      pass
 
# def make_chai(milk , sugar):
#      if milk ==0 or sugar ==0:
#          raise outofind("missing milk or sugar")
#      print("chai redy")
        

# print(make_chai(0,2))

#mini project 

# class invalidchaierror(Exception) : pass

# def bill(flavour , cups):
#     menu = {"masal" : 20 , "ginger" : 40}
    
#     try:
#         if flavour not  in menu:
#             raise invalidchaierror("not avalable")
#         if not isinstance(cups , int):
#             raise TypeError("number of cups must be an int")
        
#         total = menu[flavour] * cups
        
#         print (f"bill is {total}")
        
#     except Exception as e:
#         print("error is" ,e)
#     finally: print("project done")
    

# bill("mint" ,2)
# bill("masal" , "three")
# bill("ginger" ,3)

#FILE HANDLING
# f = open("ORDER.txt" ,"w")
# try :
#     f.write("file created and wrttin masala")
# finally:
#     f.close()

with open("new.txt" ,"w") as file:
    file.write("moder way to handle file wqiht woth keyword")
