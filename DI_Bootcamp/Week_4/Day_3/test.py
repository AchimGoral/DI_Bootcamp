# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])


# inventory = {
#     "apples": 100,
#     "oranges": 500,
#     "bananas": 200
# }

# inventory["oranges"] -= 1

# mykey = inventory.keys()
# myvalues = inventory.values()
# myitems = inventory.items()

# print(mykey)
# print(myvalues)
# print(myitems)

# inventory = {
# 	"apples": 100,
# 	"oranges": 500,
# 	"bananas": 200,
# }


# for name, number in inventory.items():
#     print(f"I have {number} {name} in my inventory")

# List comprehension

# numbers =[i for i in range(1, 1000001)]

# numbers = []
# for i in range(1, 11):
#     numbers.append(i*i)

# numbers = [i*i for i in range (1, 11)]

# print(numbers)

# numbers = {}
# for i in range (100, 111):
#     numbers[i] = i/2

# numbers = { i:i/2 for i in range (100, 111)}

# print(numbers)

# names = [input("What is your name? ") for i in range (0,3)]

# print(names)

numbers = [":)" if i%7 == 0 else i for i in range (1, 101)]