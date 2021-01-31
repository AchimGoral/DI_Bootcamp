# Exercise_1

print("Hello World\nHello World\nHello World\nHello World\nI love Python\nI love Python\nI love Python\nI love Python\n")

# Exercise_2

month = int(input("Which month are we now? "))

if  month < 1 or month > 12:
	print("It has to be lower than 12 or higher than 1")
else:
	if month >= 3 and month <= 5:
		print("Spring runs from March to May")
	elif month >= 6 and month <= 8:
		print("Summer runs from June to August")
	elif month >= 9 and month <= 11:
		print("Autumn runs from September to November")
	else:
		print("Winter runs from December to February")