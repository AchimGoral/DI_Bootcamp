# # # Exercise_1

# def insert_text():
#     item = input("What do you want want to put inside? ")
#     pos = int(input("Where do you want to put it? "))
#     list_items.insert(pos, item)

# list_items = ["Hello", "how", "are", "you"]
# print(list_items)
# insert_text()
# print(list_items)

# # Exercise_2

# test_text= "Hello there, how are you?"

# def count_spaces(text):
#     counter = text.count(' ')
#     return counter

# print(count_spaces(test_text))

# # Exercise_3

# test_text= "Hello there, how are you Jonathan?"

# def count_upper_and_lower(text):
#     upper = 0
#     lower = 0
#     undefined = 0
#     for letter in text:
#         if letter.isupper():
#             upper += 1
#         elif letter.islower():
#             lower += 1
#         else:
#             undefined += 1
#     print(f"Upper letters: {upper}")
#     print(f"Lower letters: {lower}")
#     print(f"Other letters or spaces: {undefined}")

# count_upper_and_lower(test_text)

# # Exercise_4

# list_values = [52, 62, 12, 45, 65]
# print(list_values)

# def max_value(values):
#     temp = 0
#     for item in values:
#         if item > temp:
#             temp = item
#     print(f"Highest value is: {temp}")

# max_value(list_values)

# # Exercise_5

# fact_input = int(input("Choose your factorial number: "))

# def factorial_calc(factorial):
#     result = 1
#     for n in range(factorial, 0, -1):
#         result *= n
#     return result

# print(factorial_calc(fact_input))

# # Exercise_6

# my_list = [5, 6, 9, 4, 2, 5]

# def sum_func(values):
#     result = 0
#     for item in values:
#         result += item
#     return result

# print(sum_func(my_list))

# # Exercise_7

# list_value = ['a', 'b', 'c', 'a', 'd', 'b', 'b']
# print(list_value)
# value = input("Which value to look for? ")

# def count_value(input_list, value):
#     counter = 0
#     for item in input_list:
#         if value == item:
#             counter += 1
#     return counter

# print(count_value(list_value, value))

# Exercise_8

