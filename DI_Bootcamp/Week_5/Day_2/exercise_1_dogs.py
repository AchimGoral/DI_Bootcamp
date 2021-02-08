# Exercise_2

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    
    def bark(self):
        return("bark, bark, bark")

    
    def run_speed(self):
        running_speed = self.weight/(self.age*10)
        return running_speed


    def fight(self, other_dog):
        running_speed = self.run_speed()
        if running_speed*self.weight > other_dog.run_speed()*other_dog.weight:
            print(f"{self.name} is winning")
        else:
            print(f"{other_dog.name} is winning")


d1 = Dog("Bla", 10, 50)
d2 = Dog("Blub", 8, 60)
d3 = Dog("Rex", 15, 100)

d1.fight(d2)
d3.fight(d1)
d2.fight(d3)



# Exercise_3
# See exercise_3_from_1.py