# Exercise_1

sentence = "Hello world"

for i in range (1,5):
	print(sentence)

# Exercise_2

num = (99^3)*8

print(num)

# Exercise_3

1. False
2. True
3. False string and int
4. Type error  because of comparison between string and int
False because of capital letters

# Exercise_4

computer_brand = input("What is your favorite computer brand? ")

# computer_brand = "razer"

print(f"I have a {computer_brand} computer")

# Exercise_5

name = "Achim"
age = 29
shoe_size = "9"

info = f"My name is {name} and I am {age} years old, but my shoesize is {shoe_size}, so still smaller than my age"

print(info)

# Exercise_6

a = int(input("Choose variable a "))
b = int(input("Choose variable b "))

if a > b:
	print("Hello World")

else:
	print("Bye World")

# Exercise_7

i = int(input("Pick a number "))

if i%2 == 0:
	print("The number is even")

else:
	print("The number is odd")

# Exercise_8

my_name = "Achim"
your_name = input("What is your name? ")

if my_name != your_name:
	print(f"What an unlucky person you are {your_name}. My name is {my_name}.")

else:
	print(f"Hey {your_name}. Today is your lucky day, because you're named after me")

# Exercise_9

inches = float(input("What is your height in inches? "))
centimeter = 2.54*inches
height = 145

print(f"You are {inches}in tall, or {centimeter}cm.")
if centimeter > height:
	print(f"Congratulations, you are above {height}cm and can ride")

else:
	print(f"You have to be at least {height}cm tall to ride")