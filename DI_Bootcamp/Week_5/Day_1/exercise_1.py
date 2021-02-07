# Exercise_1

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age


c1 = Cat("Dona", 15)
c2 = Cat("Marry", 2)
c3 = Cat("Tom", 10)

cats = [c1, c2, c3]

def oldest_cat():
    temp = 0
    name = ""
    for cat in cats:
        if cat.age > temp:
            temp = cat.age
            name = cat.name
    print(f"The oldest cat is {name} and is {temp} years old")

oldest_cat()

# Exercise_2

class Dog:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"goes woof")

    def jump(self, height):
        height *=2
        print(f"jumps {self.height}cm high")

davids_dog = Dog("Rex", 50)
print(davids_dog.name, davids_dog.height)
sarahs_dog = Dog("Teacup", 20)
print(sarahs_dog.name, sarahs_dog.height)

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")

# Exercise_3

class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lines in self.lyrics:
            print(lines)


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

# Exercise_4

class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        self.new_dict = {}


    def add_animal(self, new_animals):
        print(f"Which animal should we add to the zoo --> {new_animals}")
        if new_animals not in self.animals:
            self.animals.append(new_animals)
        print(self.animals)


    def get_animal(self, animals):
        for animal in self.animals:
            print(f"{animal}")


    def sell_animal(self, animal_sold):
        print(f"{animal_sold} gets sold")
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        print(f"Unsorted list of animals: {self.animals}")


    def sort_animals(self):
        new_list = []
        self.animals.sort()
        print(f"Sorted List of animals: {self.animals}")
        for animal in self.animals:
            if not new_list:
                new_list.append([animal])
            else:
                added = False
                for sub_list in new_list:
                    if sub_list[0][0] == animal[0]:
                        sub_list.append(animal)
                        added = True
                if not added:
                    new_list.append([animal])
        for index, sub_list in enumerate(new_list):
            self.new_dict.update({index+1:", ".join(sub_list)})
        print(new_list)


    def get_groups(self):
        for item in self.new_dict.items():
            print(f"list of animals: {item}")



ramat_gan_safari = Zoo("Ramat Gan")
# Adding animals
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Chimpansee")
ramat_gan_safari.add_animal("Orang")
ramat_gan_safari.add_animal("Penguin")
ramat_gan_safari.add_animal("Anaconda")
ramat_gan_safari.add_animal("Python")
# Get a specific animal from the list
ramat_gan_safari.get_animal("Orang")
# Remove animal from the list
ramat_gan_safari.sell_animal("Giraffe")
# Sort the animals and put them in a dict
ramat_gan_safari.sort_animals()
# Print the different dict groups
ramat_gan_safari.get_groups()