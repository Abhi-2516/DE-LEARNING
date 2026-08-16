# # notifcation sytem if kettle is bolied
# # if statement - verify true or false

# kt_boiled = True

# if kt_boiled:
#     print("Kettle is boiled, you can make tea now.")
# else:
#     print("Kettle is not boiled yet, please wait.")


# # A snack system if Customer aski for cookies or samosa it confirm the order or else say not available

# snack = input("Enter you prefered snack ").lower()


# print(f"user says:{snack}")


# if snack == "cookies" or snack =="samosa":
#     print(f"best choise")
# else:
#     print("no product")


# A tea stall has different price for different article

# cup_type = input("Enter your cup type : ").lower()

# if cup_type == "small":
#     print("Price is ╣$10 ")
# elif cup_type == "medium":
#     print("price is : $15")
# elif cup_type == "large":
#     print("price is : $20")
# else:
#     print("Unknown cup size")

# smart thermo stats

# device_Status = 'active'
# temp = 38

# if device_Status == 'active':
#     if(temp > 35):
#         print("ALert")
#     else:
#         print("Normal temp")
# else:
#     print("Device is offline")

# delivery fees calculator

# order_amonnt = int(input("Enter a amount"));

# del_fees = 0 if order_amonnt >300 else 30
# print('del fees is' , del_fees)

#Train steat booking system

seat_type = input("Enter your seat type sleeper /ac/general/luxry").lower()

match seat_type:
    case "sleeper":
        print("you got an seat to sleep")
    case "ac":
        print("You got an AC with your seat")
    case "general":
        print("no seat sit anywhere you got")
    case "luxry":
        print("YOU got full compart along woth personal washroom")









