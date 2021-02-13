class AnagramChecker:

    def __init__(self):
        self.new_list = []
        with open("text_file.txt", "r") as f:
            self.new_list = f.read().splitlines()
        print(self.new_list)