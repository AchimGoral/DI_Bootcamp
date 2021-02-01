import random

word = input("Put in a word with 10 characters ")
word_count = int(len(word))

if word_count > 10:
	print("It is more than 10 characters")
elif word_count < 10:
	print("It is less than 10 characters")
else:
	final = ""
	for i in range (0, 10):
		final += word[i]
		print(final)

shuffled = ''.join(random.sample(word, len(word)))
print(shuffled)