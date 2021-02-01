# Exercise_1

list_1 = ["1", "2", "50", "76"]
list_2 = ["A", "B", "D", "Z"]

list_1.extend(list_2)
print(list_1)

# Exercise_2

print("Test Data")
number = []
number.append(int(input("Give me your first number:\t")))
number.append(int(input("Give me your second number:\t")))
number.append(int(input("Give me your third number:\t")))

number.sort()
print(f"The highest number is: {number[len(number)-1]}")

# Exercise_3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(0, len(alphabet)):
    for j in range(0, len(vowels)):
        if vowels[j] in alphabet[i]:
            print(f"{vowels[j]} is a vowel")
    print(f"{alphabet[i]} is consonant")

# Exercise_4

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
print(names)
name_asked = input("Pick your name:\t")


if name_asked in names:
    print(f"It's there on Index {names.index(name_asked)}")
else:
    print("Not in the list")

# Exercise_5 ######## Still to do!!!!!

words = []
words_string = input("Give me 7 words seperated by comma:\t")
words = words_string.split(' ')
while len(words) != 7:
    words_string = input("Give me 7 words seperated by comma:\t")
    words = words_string.split(' ')
print(words)
letter = input("Give me a single character:\t")

for i in range(0, len(words)):
    for j in range(0, len(words[i])):
        if letter == words[i][j]:
            print(f"the letter {letter} is in Index {words[i][j].index(letter)}")
        else:
            print("Sorry, no match")


# Exercise_6

million_list = []

for i in range (1, 1000001):
    million_list.append(i)

print(million_list)

######################################

# Exercise_7

values = input("Input comma seperated numbers:\t")
value_list = values.split(',')
value_tuple = tuple(value_list)
print(value_list)
print(value_tuple)

# Exercise_8

import random

games = 0
wins = 0
losses = 0

input_number = int(input("Give me a random number between 0 and 9\nType in '10' if you want to quit:\t"))

while input_number > 0 or input_number < 11:
    random_number = random.randint(0, 9)
    if input_number == 10:
        print("Goodbyen")
        break
    else:
        games += 1
        if input_number == random_number:
            print("Congratulations. You guessed right\n")
            wins += 1
        else:
            print("Sorry. You were wrong. Try again?\n")
            losses += 1

    input_number = int(input("Give me a random number between 0 and 9\nType in '10' if you want to quit:\t"))

print(f"You played {games} games and had {wins} wins and {losses} losses!")

# Exercise_9

#??? The task has a complicated explenation