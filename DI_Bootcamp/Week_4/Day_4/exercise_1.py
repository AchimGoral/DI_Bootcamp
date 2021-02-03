# Exercise_1

def display_message():
    print("I am learning how to build, call and use functions")

display_message()

# Exercise_2

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Alice in wonderland")

# Exercise_3

def describe_city(city, country = "Iceland"):
    print(f"{city} is in {country}")

describe_city("Reykjavik")
describe_city("Rome", "Italy")
describe_city("London", "Great Britain")

# Exercise_4

import random

def number_compare (number):
    random_num = random.randint(1, 101)
    if random_num == number:
        print("Success")
    else:
        print(f"{random_num} is not equal to {number}")

number = int(input("Give me a number between 0 and 100 "))

number_compare(number)

# Exercise_5

def make_shirt(text, size = "L"):
    python = "I love Python"
    if size == "L" or size == "M":
        print(f"Your shirt has the size of {size} and the text of: '{python}'")
    else:
        print(f"Your shirt has the size of {size} and the text of: '{text}'")

make_shirt("S", "My shirt")

size = "M"
text = "Hello there General Kenobi"
make_shirt(text, size)

make_shirt(text)

# Exercise_6

magic = ["Harry Houdini", "David Blaine", "David Copperfield", "Chris Angel"]

def show_magicians(list_input):
    for name in list_input:
        print(f"There is {name}")

show_magicians(magic)

def make_great(list_input):
    list_output = []
    for name in list_input:
        list_output.append(f"the Great {name}")
    return list_output

magic = make_great(magic)
show_magicians(magic)

# Exercise_7

def get_age(year, month, day):

    current_year = 2021
    current_month = 2
    current_day = 3

    if current_month >= month:
        if current_day <= day:
            age = current_year - year + 1
        else:
            age = current_year - year
    else:
        age = current_year - year + 1
    return age

def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth.split("/")
    year, month, day = int(year), int(month), int(day)
    age = get_age(year, month, day)
    if gender == "m":
        if age > 67:
            return True
        return False
    elif gender == "f":
        if age > 62:
            return True
        return False
    else:
        print("Your gender is unknown")

gender = input("Give me your gender: m or f ")
date_of_birth = input("Give me your birthday: YYYY/MM/DD ")

if can_retire(gender, date_of_birth):
    print("You can retire")
else:
    print("You can't retire")

# Exercise_8

def calculate(number):
    sum_number = int(number) + int(2*number) + int(3*number) + int(4*number)
    return sum_number

x = input("Give me a number x between 1 and 9: ")
while x < "1" and x > "9":
    x = input("Give me a number x between 1 and 9: ")

print(calculate(x))