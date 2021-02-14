class AnagramChecker:

    def __init__(self):
        self.new_list = []
        with open("text_file.txt", "r") as f:
            self.new_list = f.read().splitlines()
    

    def is_valid_word(self, word):
        for word in self.new_list:
            if word in self.new_list:
                return True
            else: 
                return False
