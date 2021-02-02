# # Exercise_1 + 2

# birthdays = {input("Give me your name: "): ' '.join(input("Give me your birdthay in DD/MM/YYYY: ").split('/')) for i in range (6)}

# print("Welcome. You can look up the birthday of the people in the list!\n")

# for key in birthdays:
#     print(f"{key}")

# print("")
# search_name = input("Please type in the name you're looking for: ")

# for key in birthdays.keys():
#     if search_name == key:
#         print(f"{search_name}s Birthday is at the {birthdays[search_name]}")
#         break
# else:
#     print("Sorry, we don’t have birthday information for")

# # Exercise_3

# birthdays = {input("Give me your name: "): ' '.join(input("Give me your birdthay in DD/MM/YYYY: ").split('/')) for i in range (6)}

# birthdays_new = {input("Give me another name: "): ' '.join(input("Give me another birdthay in DD/MM/YYYY: ").split('/'))}

# birthdays.update(birthdays_new)

# print("Welcome. You can look up the birthday of the people in the list!\n")

# for key in birthdays:
#     print(f"{key}")

# print("")
# search_name = input("Please type in the name you're looking for: ")

# for key in birthdays.keys():
#     if search_name == key:
#         print(f"{search_name}s Birthday is at the {birthdays[search_name]}")
#         break
# else:
#     print("Sorry, we don’t have birthday information for")

# # Exercise_4

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

amount = [200, 300, 450, 250]

i = 0
for key, value in items.items():
    items[key] = {"price": value, "stock": amount[i]}
    i += 1

list_values = []
final_amount = 0

for key_1, value_1 in items.items():
    for key_2, value_2 in value_1.items():
        list_values.append(value_2)

for i in range(0, len(list_values), 2):
    final_amount +=list_values[i]*list_values[i+1]

print(f"The final amount is: {final_amount}$")

# # Exercise_5

brands = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

brands_list = brands.split(',')

print(f"There are {len(brands_list)} brands in the list")

print(sorted(brands_list, reverse=True))

o_counter = 0
for i in range(len(brands_list)):
    if "o" or "O" in brands_list[i]:
        o_counter += 1
        # checking also for capital letters

print(f"{o_counter} manfacturers have the letter 'o' inside their name")

i_counter = 0
for i in range(len(brands_list)):
    if "i" or "I" not in brands_list[i]:
        i_counter += 1
        # checking also for capital letters

print(f"{i_counter} manfacturers have not the letter 'i' inside their name")