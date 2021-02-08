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
        print(f"{self.name}'s farm\n")
        for key, value in self.new_dict.items():
            print(f'{key}: {value}')
        print("\n\tE-I-E-I-O!")

    def get_animal_types(self):
        new_list = []
        for key in self.new_dict.keys():
            new_list.append(key)
        new_list.sort()
        return new_list

    def get_short_info(self):
        list_items = self.get_animal_types()
        animal_string = ', '.join(list_items) + '.'
        print(f"McDonald’s farm has {animal_string}")




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('ox')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 5)

print(macdonald.get_info())

macdonald.get_animal_types()

macdonald.get_short_info()