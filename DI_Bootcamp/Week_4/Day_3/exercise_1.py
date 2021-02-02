# Exercise_1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = {keys[i]:values[i] for i in range (0, len(keys))}
print(dictionary)

# Exercise_2

family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}

price_list = [0, 10, 15]
price = 0

for name, age in family.items():
    if age < 3:
        print(f"{name} has to pay {price_list[0]}$")
    elif age >=3 and age < 12:
        print(f"{name} has to pay {price_list[1]}$")
        price += price_list[1]
    else:
        print(f"{name} has to pay {price_list[2]}$")
        price += price_list[2]

print(f"The family has to pay {price}$")

# Exercise_3

brand = {
    "name": "Zara", 
    "creation_date": 1975,
    "creator_name": [
        "Amancio", "Ortega", "Gaona"],
    "type_of_clothes": [
        "men", "women", "children", "home"],
    "international_competitors": [
        "Gap", "H&M", "Benetton"],
    "number_stores": 7000, 
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"],
    },
}

brand["number_stores"] = 2
competitors = brand["international_competitors"]

for competitor in competitors:
    print(f"{competitor} is a competitor")

brand["country_creation "] = "Spain"

print(brand)
print("")

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

print(brand)
print("")

del brand["creation_date"]

print(brand)
print("")

print(brand["international_competitors"][-1])
print("")

for color in brand["major_color"]["US"]:
    print(color)
print("")

number = 0
for numbers in brand.keys():
    number += 1
print(number)
print("")

for keys in brand.keys():
    print(keys)
print("")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000,
}

brand.update(more_on_zara)
print(brand)
print("")

print(brand["number_stores"])

# Exercise_4

users = [ "Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {users[i]: i for i in range(0, len(users))}
print(disney_users_A)

disney_users_B = dict(enumerate(users))
print(disney_users_B)

users = sorted(users)
disney_users_C = {users[i]: i for i in range (0, len(users))}
print(disney_users_C)

disney_users_D = {users[i]: i for i in range(0, len(users)) if "i" in users[i]}
print(disney_users_D)

disney_users_E = {users[i]: i for i in range(0, len(users)) if "M" and "P" in users[i][0]}
print(disney_users_E)