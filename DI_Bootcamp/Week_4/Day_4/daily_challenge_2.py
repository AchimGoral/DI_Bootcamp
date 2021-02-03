import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

counter = 0
for i in range(20000):
    for j in range(i+1, 20000):
        if list_of_numbers[i] + list_of_numbers[j] ==  target_number:
            counter += 1

print(f"There are {counter} pairs to make up to {target_number}")