# __init__: called when an object is instantiated

# __repr__: called when you dump an object variable on screen

# __str__: called when you print a variable
# # str is more informal than repr

# class Person:

#     def __init__(self, weight, height, facebook_friends):
#         self.weight = weight
#         self.height = height
#         self.facebook_friends = facebook_friends

#     def __gt__(self, other):
#         if self.facebook_friends > other.facebook_friends:
#             return True
#         return False

# print(dir(Person)) # see all the different methods possible
# p1 = Person(100, 1, 200)
# p2 = Person(50, 2, 199)
# print(p1 > p2) # call dunder __gt__(greater than)

