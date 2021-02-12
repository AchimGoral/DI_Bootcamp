# # Exercise_1

# import json
# import random as rd
# from cprint import cprint


# def get_words_from_file():
#     with open('sowpods.txt', 'r') as f:
#         data = f.readlines()
#         return data


# def get_random_sentence(lenght):
#     data = get_words_from_file()
#     sentence = rd.sample(data, lenght)
#     sentence = map(lambda s: s.strip(), sentence)
#     sent_string = ''
#     sent_string += ' '.join(sentence).title()
#     print(sent_string)


# def main():
#     print("This Programm lets you pick a sentence lenght between 2 and 20 words to print out a randaom sentence")

#     lenght = int(input("Pick a number between 2 and 20: "))

#     while lenght < 2 or lenght > 20:
#         print("Your number is too small or too big. Try again...")
#         lenght = int(input("Pick a number between 2 and 20: "))
    
#     get_words_from_file()

#     get_random_sentence(lenght)

# main()

# Exercise_2

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(data['company']['employee']['payable']['salary'])

data['company']['employee']['birth_date'] = '03/12/1991'

with open('exercise.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)