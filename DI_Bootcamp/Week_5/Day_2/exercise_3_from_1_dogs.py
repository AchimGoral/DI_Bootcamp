import exercise_1_dogs as ex
import random as rd

class PetDog(ex.Dog):

    def __init__(self, name, age, weight):
        super().__init__(self, name, age, weight)
        self.trained = False


    def train(self):
        self.bark()
        return self.trained = True


    def play(self, *dog_names):
        dogs = ', '.join(dog_names.name)
        print(f"the dogs: {dogs} play together")
        return dog_names.trained = False


    def do_a_trick(self, *dog_names):
        number = rd.randint(0, 3)
        if self.trained = True:
            if number == 0:
                print(f"{dog_names.name} does a barrel roll")
                dog_names.trained = False
            elif number == 1:
                print(f"{dog_names.name} stands on their back legs")
                dog_names.trained = False
            elif number == 2:
                print(f"{dog_names.name} shakes your hand")
                dog_names.trained = False
            else:
                print(f"{dog_names.name} plays dead")
                dog_names.trained = False