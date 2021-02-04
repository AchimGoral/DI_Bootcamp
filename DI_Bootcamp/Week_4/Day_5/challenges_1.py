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
#     return counter, value

# print(count_value(list_value, value))

# # Exercise_8

# new_list = [1, 2, 5, 6, 7]
# print(new_list)

# def sqrroot(input_list):
#     new_sum = 0
#     for item in input_list:
#         new_sum += item**2
#     result = new_sum**(1/2)
#     return result

# print(sqrroot(new_list))

# # Exercise_9 #### Whats wrong?

# new_list_1 = [1, 2, 3, 5, 6]
# new_list_2 = [5, 5, 3, 7, 9]
# new_list_3 = [1, 2, 2, 2, 4]

# def mono(input_list):
#     flag = False
#     for i in range(0, len(input_list)-1, 1):
#         if input_list[i] <= input_list[i+1]:
#             print(input_list[i], input_list[i+1])
#             flag = True
#         else:
#             flag = False
#             break
#     return flag
     

# print(mono(new_list_1))

# # Exercise_10

# word_list = ['Hello', 'how', 'are', 'you?', 'I', 'am ', 'feeling', 'good']

# def find_long(input_list):
#     longest_word = ''
#     for item in input_list:
#         if len(longest_word) < len(item):
#             longest_word = item
#     return longest_word

# print(find_long(word_list))

# # Exercise_11

# mixed_list = [1, 6, 'hello', 95, 'how', 'are', 45, 'you?']

# def sort_list(input_list):
#     numbers = []
#     words = []
#     for item in input_list:
#         if type(item) == str:
#             words.append(item)
#         else:
#             numbers.append(item)
#     return numbers, words

# print(sort_list(mixed_list))

# # Exercise_12

# string_1 = 'radar'
# string_2 = 'hello'

# def palyndrome(input_string):
#     for i in range(int(len(input_string)/2)):
#         if input_string[i] != input_string[len(input_string)-i-1]:
#             return False
#     return True

# print(palyndrome(string_1))

# # Exercise_13

# sentence = input("Give me your sentence ")
# k = int(input("How long to count? "))

# def sum_over_k(sentence, k):
#     sentence_list = sentence.split(' ')
#     counter = 0
#     for item in sentence_list:
#         if len(item) > k:
#             counter += 1
#     return counter

# print(sum_over_k(sentence, k))

# # Exercise_14

# dict_values = {
#     'a': 1, 'b': 8, 'c': 9, 'd': 1
# }

# def average_value(dict_values):
#     new_list = list(dict_values.values())
#     final_sum = 0
#     for item in new_list:
#         final_sum += item/len(new_list)
#     return final_sum

# print(average_value(dict_values))

# # Exercise_15

# a = int(input("Give me the first number: "))
# b = int(input("Give me the second number: "))

# def commondiv(a, b):
#     c = 0
#     if a <= b:
#         c = a    
#     else:
#         c = b
#     print(c)
#     result_list = []
#     for i in range(2, c + 1):
#         if a%i == 0 and b%i == 0:
#             result_list.append(i)
#     return result_list

# print(commondiv(a, b))

# # Exercise_16

# number = int(input("Put in any number: "))

# def prime(number):
#     if number > 1:
#         for i in range(2, number):
#             if number%i == 0:
#                 return False
#             else:
#                 return True
#     else:
#         print("Anything below 2 is not working")

# print(prime(number))

# # Exercise_17

# list_values = [1, 2, 5, 7, 9, 12, 14, 15, 18]
# print(list_values)

# def even_values(list_values):
#     new_list = []
#     for item in list_values:
#         if item%2 == 0:
#             new_list.append(item)
#     return new_list

# print(even_values(list_values))

# # Exercise_18

# new_dict = {"a": 1, "b": True, "c": 'Hello', "e": False, "f": 2.0}

# def keywords(new_dict):
#     int_counter = 0
#     float_counter = 0
#     bool_counter = 0
#     str_counter = 0
#     for item in new_dict.values():
#         if type(item) == int:
#             int_counter += 1
#         elif type(item) == float:
#             float_counter += 1
#         elif type(item) == str:
#             str_counter += 1
#         else:
#             bool_counter += 1
#     return print(f"Int: {int_counter}, Str: {str_counter}, Float: {float_counter}, Bool: {bool_counter}")

# keywords(new_dict)

# Exercise_19

