# # # # # """Basic Object-Oriented Programming (OOP) concepts in Python."""


# # # # # class Animal:
# # # # # 	"""A simple class with an attribute and methods."""

# # # # # 	# Class attribute: shared by all Animal objects.
# # # # # 	kingdom = "Animalia"

# # # # # 	def __init__(self, name, sound):
# # # # # 		# Instance attributes: unique to each object.
# # # # # 		self.name = name
# # # # # 		self.sound = sound

# # # # # 	def speak(self):
# # # # # 		return f"{self.name} says {self.sound}"


# # # # # class Dog(Animal):
# # # # # 	"""Dog inherits from Animal and adds its own behavior."""

# # # # # 	def __init__(self, name, breed):
# # # # # 		super().__init__(name, "Woof")
# # # # # 		self.breed = breed

# # # # # 	# Method overriding (polymorphism).
# # # # # 	def speak(self):
# # # # # 		return f"{self.name} barks: {self.sound}"


# # # # # class BankAccount:
# # # # # 	"""Encapsulation example using a private balance attribute."""

# # # # # 	def __init__(self, owner, opening_balance=0):
# # # # # 		self.owner = owner
# # # # # 		self.__balance = opening_balance

# # # # # 	def deposit(self, amount):
# # # # # 		if amount <= 0:
# # # # # 			raise ValueError("Deposit must be positive")
# # # # # 		self.__balance += amount

# # # # # 	def get_balance(self):
# # # # # 		return self.__balance


# # # # # if __name__ == "__main__":
# # # # # 	# Object creation and method calls.
# # # # # 	animal = Animal("Cat", "Meow")
# # # # # 	dog = Dog("Bruno", "Labrador")
# # # # # 	print(animal.speak())
# # # # # 	print(dog.speak())
# # # # # 	print(f"{dog.name} is a {dog.breed} ({dog.kingdom})")

# # # # # 	account = BankAccount("Asha", 1_000)
# # # # # 	account.deposit(500)
# # # # # 	print(f"{account.owner}'s balance: {account.get_balance()}")


# # # # # lernig 

# # # # #objhect are reral world entiote having their on entity (feartute)

# # # # class chai:
# # # #     origin = "India"
    
# # # # print(chai.origin)

# # # # chai.is_hot =True

# # # # print(chai.is_hot)


# # # #attribute shadowing

# # # class Chai:
# # #     temperature = "hot"
# # #     strength = "Strong"


# # # cutting = Chai()
# # # print(cutting.temperature)

# # # cutting.temperature = "Mild"
# # # cutting.cup = "small"
# # # print("After changing ",cutting.temperature)
# # # print("cup size is  ",cutting.cup)
# # # print("Direct look into the class ", Chai.temperature)

# # # del cutting.temperature
# # # del cutting.cup
# # # print(cutting.temperature)
# # # print(cutting.cup)



# # #self arguemnt in python
# # # class chaicup:
# # #     size = 150
    
# # #     def describe(self):
# # #         return f"a {self.size} ml chai"
        
# # # cup = chaicup()
# # # print(cup.describe())

# # # # init nobject
# # # class ChaiOrder:
    
# # #     def __init__(self, type_, size):
# # #         self.type = type_
# # #         self.size = size

# # #     def summary(self):
# # #         return f"{self.size}ml of {self.type} chai"
    
# # # order = ChaiOrder("Masala", 200)
# # # print(order.summary())

# # # order_two = ChaiOrder("Ginger", 220)
# # # print(order_two.summary())


# # # class SmartDevice:
# # #     brand = "HomeTech" 
 
# # #     def __init__(self, device_name: str, power_status: bool):
# # #         self.device_name = device_name        
# # #         self.power_status = power_status     
# # #         self.brand = "CustomBrand"  # Attribute shadowing
 
# # #     def get_status(self) -> str:
# # #         status = "ON" if self.power_status else "OFF"
# # #         return f"{self.device_name} is {status} - {self.brand}"


# # #inheritance and composition

# # class BaseChai:
# #     def __init__(self , type_):
# #         self.type = type_
        
# #     def prepare(self):
# #         print(f"prepare {self.type} chai........")
        

# # class masala(BaseChai):
# #     def add_spice(self):
# #         print("Adding spices card , ginfer")

   
# # class cguashop:
# #     chai_cls = BaseChai    
     
# #     def __init__(self):
# #         self.chai = self.chai_cls("Regular")
# #     def serve(self):
# #         print(f"serving{self.chai.type} chai in shop")
# #         self.chai.prepare()

# # class fancy(cguashop):
# #     chai_cls = masala


# # shop = cguashop()
# # fancy = fancy()

# # shop.serve()
# # fancy.serve()


# # ways to access the base
# # class Chai:
# #     def __init__(self, type_, strength):
# #         self.type = type_
# #         self.strength = strength


# # # class GingerChai(Chai):
# # #     def __init__(self, type_, strength, spice_level):
# # #         self.type = type_
# # #         self.strength = strength
# # #         self.spice_level = spice_level
        

# # # class GingerChai(Chai):
# # #     def __init__(self, type_, strength, spice_level):
# # #         Chai.__init__(self, type_, strength)
# # #         self.spice_level = spice_level


# # class GingerChai(Chai):
# #     def __init__(self, type_, strength, spice_level):
# #         super().__init__(type_, strength)
# #         self.spice_level = spice_level

# #Method resolution order(mro)

# # class A:
# #     label = "BASE A"

# # class B(A):
# #     label = "B"
    
# # class C(A):
# #     label = "c"
    
# # class D(C,B):
# #     pass

# # cup = D()
# # print(cup.label)
# # print(D.__mro__)
    
    
# # static methid in python

# # class chai_utils:
    
# #     @staticmethod
# #     def clean_indegredients(text):
# #        return  [item.strip() for item in text.split(",")]


# # raw = "water , milk , ginger , honey"

# # cleaned = chai_utils.clean_indegredients(raw)

# # print(cleaned)

# #class methid vs static method
# # class ChaiOrder:
# #     def __init__(self, tea_type, sweetness, size):
# #         self.tea_type = tea_type
# #         self.sweetness = sweetness
# #         self.size = size

# #     @classmethod
# #     def from_dict(cls, order_data):
# #         return cls(
# #             order_data["tea_type"],
# #             order_data["sweetness"],
# #             order_data["size"],
# #         )
    
# #     @classmethod
# #     def from_string(cls, order_string):
# #         tea_type, sweetness, size = order_string.split("-")
# #         return cls(tea_type, sweetness, size)
    
# # class ChaiUtils:
# #     @staticmethod
# #     def is_valid_size(size):
# #         return size in ["Small", "Medium", "Large"]


# # print(ChaiUtils.is_valid_size("Medium"))

# # order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

# # order2 = ChaiOrder.from_string("Ginger-Low-Small")

# # order3 = ChaiOrder("Large", "Low", "Large")

# # print(order1.__dict__)
# # print(order2.__dict__)
# # print(order3.__dict__)

# # property decporator
# class Tealef:
#     def __init__(self , age):
#       self._age = age
      
#     @property
#     def age(self):
#         return self._age + 2
    
#     @age.setter
#     def age(self, age):
#         if 1<= age <=5:
#             self._age = age
            
#         else:
#             raise ValueError("Tea leaf must be between 1 and 5")
        
# leaf   = Tealef(8)
# print(leaf.age)
# 3




# class Engine:
#     def __init__(self, horsepower: int):
#         self.horsepower = horsepower
 
#     def get_engine_info(self):
#         return f"{self.horsepower} HP Engine"
 
 
# class Vehicle:
#     total_vehicles = 0  # class variable
 
#     def __init__(self, brand: str, model: str, engine: Engine):
#         self.brand = brand
#         self.model = model
#         self.engine = engine
#         self._rental_price = 0  # for property demo
#         Vehicle.total_vehicles += 1
 
#     @staticmethod
#     def get_vehicle_type():
#         return "Generic Vehicle"
 
#     @classmethod
#     def get_total_vehicles(cls):
#         return cls.total_vehicles
 
#     @property
#     def rental_price(self):
#         return self._rental_price
 
#     @rental_price.setter
#     def rental_price(self, price: int):
#         if price >= 0:
#             self._rental_price = price
 
#     def get_details(self):
#         return f"{self.brand} {self.model} - {self.engine.get_engine_info()}"
 
 
# class Car(Vehicle):
#     def __init__(self, brand: str, model: str, engine: Engine, seats: int):
#         super().__init__(brand, model, engine)
#         self.seats = seats
 
#     def get_details(self):
#         return f"{super().get_details()} - Seats: {self.seats}"