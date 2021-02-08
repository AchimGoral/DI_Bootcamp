from cprint import cprint

# """"Main class"""
# class Person: # SuperClass

#     def __init__(self, name, age):
#         cprint.err("In the INIT of PERSON class")
#         self.name = name
#         self.age = age
#         cprint.err("finishing the INIT of PERSON class")

#     def info(self):
#         print(f"{self.name} is {self.age} years old")

#     def birthday(self):
#         self.age += 1
#         print("Happy Birthday")

# """"Inheritance"""
# class Man(Person): # SubClass

#     def __init__(self, name, age, favorite_beer):
#         cprint.info("In the INIT of MAN class")
#         super().__init__(name, age)
#         self.favorite_beer = favorite_beer
#         self.gender = "Male"
#         cprint.info("finishing the INIT of MAN class")

#     def birthday(self):
#         super().birthday() 
#         # calling the parent class

#     def drink_beer(self):
#         print("Glug glug glug")


# m1 = Man("Adam", 25, "Corona")
# print(m1.age)



# # Inheritance:
# # class SubClass(SuperClass)

# class Account:

#     def __init__(self, acc_number):
#         self.acc_number = acc_number
#         self.__balance = 0
#         self.__transaction_history = []


#     def deposit(self, amount):
#         if amount > 0 and amount <= 10000:
#             self.__balance += amount

#         self.__transaction_history.append(f"Deposit: {amount}")
    

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             return amount
#         else:
#             print("Insufficient amount")
            

#     def info(self):
#         print(f"Account {self.acc_number} has balance of ${self.__balance}")

# leumi1 = Account("12345")
# leumi1.deposit(1000)
# leumi1.info()
# leumi1.withdraw(300)
# leumi1.info()



# # __shows other prgrammers, that this is protected, although it is not in reality

