class Farm:

    def __init__(self, name):
        self.name = name
        self.new_dict = {}

    def add_animal(self, animal, amount=1):
        if animal not in self.new_dict:
            self.new_dict[animal] = amount
        else:
            self.new_dict[animal] += amount

    def get_info(self): 
        print("Macdonald's farm\n")
        for dic_item in self.new_dict.items():
            print(f'{dic_item[0]}: {dic_item[1]}')
        print("")
        print("\tE-I-E-I-O!")

    def get_animal_types(self):
        new_list = []
        for key in self.new_dict.keys():
            new_list.append(key)
        new_list.sort()
        print(new_list)

    def




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())

macdonald.get_animal_types()