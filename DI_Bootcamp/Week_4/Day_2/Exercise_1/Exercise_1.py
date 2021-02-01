# # Exercise_1

# my_fav_numbers = {"1", "7", "13", "55"}
# my_fav_numbers.add(8)
# my_fav_numbers.add(15)
# my_fav_numbers.pop()
# print(my_fav_numbers)

# friend_fav_numbers = {"2", "18", "25"}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# # Exercise_2

# No, it is not changeable

# # Exercise_3

# for i in range(0, 21):
#     print(i)

# # Exercise_4

# Float is comma seperated value compared to a int, which can only contain whole numbers
# use the function float(int) or division of integers can create a float

# for i in range (1, 5):
#     print(i + 0.5)
#     print(i + 1)

# # Exercise_5

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# # Exercise_6

# my_name = "Achim"
# your_name = input("What is your name? ")
# while your_name != my_name:
#     your_name = input("What is your name? ")

# # Exercise_7

# my_list = ["A", "B", "C", "D", "E", "F"]
# for i in range (0, len(my_list), 2):
#     print(my_list[i])

# # Exercise_8

# list_of_three = []

# for i in range (3, 31, 3):
#     list_of_three += [i]

# print(list_of_three)

# # Exercise_9

# for i in range (1500, 2701):
#     if i%7 == 0 and i%5 == 0:
#         print(i)

# # Exercise_10

# fruits = input("Favority fruits, separated by spaces ")
# fruits_list = fruits.split()
# fruit_input = input("Type in a fruit ")

# if fruit_input in fruits_list:
#     print("You chose one of your favorite fruits! Enjoy!")
#     fruits_list.insert(len(fruits_list) - 1, "and")
#     new_list = ' '.join(fruits_list)
#     print(new_list)
# else:
#     print("You chose a new fruit. I hope you enjoy it too!")


# # Exercise_11

# topping = []

# while True:
#     ask_topping = input("What topping do you want on your Pizza? 'quit' will leave the menu ")
#     if ask_topping == 'quit':
#         break
#     else:
#         topping.append(ask_topping)
#         print(f"I'll add {ask_topping} on to your Pizza")
# print
# topping_list = ', '.join(topping)
# print(f"You got following items on your pizza: {topping_list}.\nThe total is 10$ + {2.5*len(topping)}$ for the toppings")

# # Exercise_12

# people_count = int(input("How many people are you? "))
# person_ages = []
# price_list = [0, 10, 15]
# ticket_price = []

# for i in range (0, people_count):
#     person_asked = int(input(f"How old are you person {i+1}? "))
#     if person_asked < 3:
#         ticket_price.append(price_list[0])
#     elif person_asked >= 3 and person_asked < 12:
#         ticket_price.append(price_list[1])
#     elif person_asked >= 16 and person_asked <= 21:
#         print("People between 16 and 21 can't see this movie")
#     else:
#         ticket_price.append(price_list[2])

# final_price = 0
# for i in range (0, len(ticket_price)):
#     final_price += ticket_price[i]

# print(f"Your final price is: {final_price}$")

# # Exercise_13

# users = []
# counter = int(input("How many people to add? "))

# for i in range (0, counter):
#     users_asked = int(input("What is your age? "))
#     users.append(users_asked)
# print(users)

# new_list = []

# for i in range (0, counter):
#     if users[i] < 16:
#         continue
#     else:
#         new_list.append(users[i])

# print(new_list)

# # Exercise_14

# family_member = []

# while True:
#     print("1. Add a name\n2. Remove existing name\n3. View family members\n4. Exit")
#     x = int(input("Choose your option with 1, 2, 3 or 4: "))
#     if x < 1 and x > 4:
#         x = int(input("Choose your option with 1, 2, 3 or 4"))
#     elif x == 1:
#         new_name = input("Add your name: ")
#         family_member.append(new_name)
#     elif x == 2:
#         remove_name = input("Which name should be deleted? ")
#         if not family_member:
#             print("No names inside")
#             break
#         else:
#             family_member.remove(remove_name)
#     elif x == 3:
#         family_list = '; '.join(family_member)
#         print(f"These are your members: {family_list}")
#     else:
#         break