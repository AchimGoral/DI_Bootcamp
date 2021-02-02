# Exercise_1

x = int(input('Enter the Number: ')) 

sum_final = 0

for i in range(1, x):
    if x%i == 0:
        sum_final += i
if sum_final == x:
    print(f"{x} is a perfect number")
else:
    print(f"Sorry, {x} isn't perfect number")



#  Exercise_2

input_sentense = input("Put your sentence in: ")
print(f"Your sentence: {input_sentense}")

list_sentence = input_sentense.split(' ')
list_sentence.reverse()

conc_sentence = ' '.join(list_sentence)

print(f"your reversed sentence: {conc_sentence}")