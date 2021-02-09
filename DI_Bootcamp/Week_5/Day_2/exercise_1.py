# Exercise_1

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Kitty(Cat):
    def sing(self, sounds):
        return f"{sounds}"

bengal = Bengal("Marry", 12)
chartreux = Chartreux("Louis", 10)
kitty = Kitty("Henry", 8)

my_cats = [bengal, chartreux, kitty]

my_pets = Pets(my_cats)

my_pets.walk()

# Exercise_4

class Family:

    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        born_dict = {}
        for key, value in kwargs.items():
            born_dict[key] = value
        self.members.append(born_dict)
        print(f"Hello {self.members[-1]['name']}, welcome to the Family")

    def is_18(self):
        value = int(input("Choose your family member: "))
        if self.members[value]["age"] < 18:
            print(f"{self.members[value]['name']}, you're too young")
            return False
        else:
            print(f"{self.members[value]['name']}, come and drink")
            return True

    def present_family(self):
        for item in self.members:
            for key, value in item.items():
                print(f"{key}:\t {value}")
            
family_1 = Family([ {'name':'Michael','age':35,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}], "Rogers")

family_1.born(name="Mike", age=0, gender="Male", is_child=True)

family_1.is_18()

family_1.present_family()

# Exercise_5

class Incredibles(Family):

    def __init__(self, members, last_name, power, incredible_name):
        super().__init__(members, last_name)
        self.power = power
        self.incredible_name = incredible_name

    def use_power(self):
        try:
            if self.members['age'] > 18:
                print(f"Your power is: {self.power['power']}")
        except:
            print(f"{self.members['name']} isn't over 18")

    def incredible_presentation(self):
        for item in self.members:
            print(item)
        for item in self.power:
            print(item)
        for item in self.incredible_name:
            print(item)

        
incredible_family = Incredibles([ {'name':'Bob','age':35,'gender':'Male','is_child':False}, {'name':'Helen','age':32,'gender':'Female','is_child':False}, {'name':'Violet','age':12,'gender':'Female','is_child':True}, {'name':'Dashiell','age':8,'gender':'Male','is_child':True}], "Parr", [{'power': 'super-strength'}, {'power': 'invisible'}, {'power': 'force-shield'}, {'power': 'super-speed'}], [{'incredible_name': 'Mr. Incredible'}, {'incredible_name': 'Elastigirl'}, {'incredible_name': 'Vi'}, {'incredible_name': 'Dash'}])

incredible_family.present_family()

incredible_family.incredible_presentation()

incredible_family.born(name="Jack", age=3, gender="Male", is_child=True, incredible_name='Jack-Jack', power='Unknown power')

incredible_family.incredible_presentation()