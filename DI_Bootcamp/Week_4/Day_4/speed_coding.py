string = input("Give me a sentence: ")
print(f"String: {string}")
character = input("Give me a character to check: ")
print(f"Character: {character}")

counter = 0
for letter in string:
    if letter == character:
        counter += 1

print(f"There are {counter} letters in the sentence")