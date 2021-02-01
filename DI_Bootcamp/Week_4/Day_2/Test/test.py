# Lists

my_hobbies = ["Eat", "Sleep", "Code"]

my_hobbies[2] = "Cats"

my_hobbies.append("Coffee")

# my_hobbies.remove(my_hobbies[1])

# thing = my_hobbies.pop(0)

# print (my_hobbies)
# print(thing)

your_hobbies = ["Bed", "Breaks", "Pointing"]

our_hobbies = my_hobbies + your_hobbies
# print(our_hobbies)

numbers = [4, 6, 82, 9]
numbers.sort()
# print(numbers)

name = "Jonathan"
# print(sorted(name))

list1 = [5, 10, 15, 20, 25, 50, 20]
i = list1.index(20)
list1.remove(20)
list1.insert(i, 200)
# print(list1)

# Sets
# Sets are unordered
# Sets cannot contain duplicates
# No append

myset = {"A", "B", "C"}

myset = {"A", "B", "C", "D", "E", "A", "C"}

myset.add("F")
# print(myset)

email = ["jon@gmail.com", "anna@aol.com", "mike@gmail.com", "jon@gmail.com", "bob@yahoo.com", "bob@gmail.com", "anna@aol.com"]
email_set = set(email)
# print("Emails: ", email)
# print("Unique emails: ", email_set)
# print(email[::-1])

# Tuples
# cannot be changed

my_tuple = (5,6,7)

a, b, c = my_tuple
print(a)