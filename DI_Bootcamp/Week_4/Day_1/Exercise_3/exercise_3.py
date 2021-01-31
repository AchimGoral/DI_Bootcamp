# # Exercise_1

# If you wnat to call your porgram, teh shell will check for any executable programs in you computer.
# Is the file in your path, it can be executed from this place.

# # Exercise_2

# alias seems only to be working in bash console

# Exercise_3

# 1. True
# 2. True
# 3. False
# 4. False
# 5. True
# 6. False
# 7. x is True
# 	 y is False
#    a = 5
#    b = 10

# # Exercise_4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# Exercise_5

tries = int(input("How many times you want to try? "))
longest = 0 # stores the longest length of a sentence to compare

for i in range (0, tries):

	sentence = input("Put your longest sentence without A ")

	if "A" in sentence:
		print("That was wrong. There was an A")
		break
	elif len(sentence) < longest:
		print(f"Your sentence was shorter than {longest} characters")
	else:
		longest = len(sentence)
		print(f"Congratulations your sentence is {longest} characters long")