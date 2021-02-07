# Exercise_1

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(self):
        temp = 0
        if self.age > temp:
            temp = self.age
        print(f"The oldest cat is {self.name} and is {self.age} years old")

c1 = Cat("Dona", 15)
c2 = Cat("Marry", 2)
c3 = Cat("Tom", 10)
c1.oldest_cat()
c2.oldest_cat()
c3.oldest_cat()

# # Exercise_2

# class Dog:

#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"goes woof")

#     def jump(self, height):
#         height *=2
#         print(f"jumps {self.height}cm high")

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name, davids_dog.height)
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)

# if davids_dog.height > sarahs_dog.height:
#     print(f"{davids_dog.name} is bigger")
# else:
#     print(f"{sarahs_dog.name} is bigger")

# # Exercise_3

# class Song:

#     def __init__(self, lyrics):
#         self.lyrics = lyrics

#     def sing_me_a_song(self):
#         for lines in self.lyrics:
#             print(lines)


# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# # Exercise_4

# class Zoo:

#     def __init__(self, zoo_name):
#         self.animals = []
#         self.name = zoo_name
#         self.new_dict = {}


#     def add_animal(self, new_animals):
#         print(f"Which animal should we add to the zoo --> {new_animals}")
#         if new_animals not in self.animals:
#             self.animals.append(new_animals)
#         print(self.animals)


#     def get_animal(self, animals):
#         for animal in self.animals:
#             print(f"{animal}")


#     def sell_animal(self, animal_sold):
#         print(f"{animal_sold} gets sold")
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#         print(f"Unsorted list of animals: {self.animals}")


#     def sort_animals(self):
#         self.animals.sort()
#         print(f"Sorted List of animals: {self.animals}")
#         for i in range(len(self.animals)):
#             case = {i+1: self.animals[i]}
#             self.new_dict.update(case)
#         print(self.new_dict)


#     def get_groups(self):
#         for item in self.new_dict.items():
#             print(f"list of animals: {item}")



# ramat_gan_safari = Zoo("Ramat Gan")
# # Adding animals
# ramat_gan_safari.add_animal("Giraffe")
# ramat_gan_safari.add_animal("Chimpansee")
# ramat_gan_safari.add_animal("Orang")
# ramat_gan_safari.add_animal("Penguin")
# ramat_gan_safari.add_animal("Anaconda")
# ramat_gan_safari.add_animal("Python")
# # Get a specific animal from the list
# ramat_gan_safari.get_animal("Orang")
# # Remove animal from the list
# ramat_gan_safari.sell_animal("Giraffe")
# # Sort the animals and put them in a dict
# ramat_gan_safari.sort_animals()
# # Print the different dict groups
# ramat_gan_safari.get_groups()