# Exercise_1

import random

def get_random_temp(season):
    if season == "winter":
        degree = round(random.uniform(-10, 16), 2)
    elif season == "spring" or season == "autumn":
        degree = round(random.uniform(0, 25), 2)
    elif season == "summer":
        degree = round(random.uniform(16, 41), 2)
    else:
        print("What kind of season is that? Whatever, take a random degree")
        degree = round(random.uniform(-273.15, 200), 2)
    return degree

def main():
    season = input("Choose your season:\nwinter\nspring\nsummer\nautumn: ")
    degree = get_random_temp(season)
    print(f"The temperature right now is {degree} degree Celsius.")
    if degree < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif degree >= 0 and degree < 16:
        print("Wuite chilly here! Don't forgat ya coat man man")
    elif degree >= 16 and degree < 24:
        print("Still not really summer. Get your pullover")
    elif degree >= 24 and degree < 32:
        print("Better get rid of your pollover now")
    elif degree >=32 and degree < 41:
        print("SUMMER is here")
    else:
        print("Better bring a fire exstinguisher...")

main()

# Exercise_2

import random

def throw_dice():
    return random.randint(1, 7)

def throw_until_doubles():
    counter = 0

    while True:
        first = throw_dice()
        second = throw_dice()
        counter += 1
        if first == second:
            return counter

def main():
    result_list = []
    for throws in range(0, 101):
        counter = throw_until_doubles()
        result_list.append(counter)
    
    result_counter = 0
    for results in result_list:
        result_counter += results

    average = round((result_counter/100), 2)
    print(f"The total throws are {result_counter}")
    print(f"The average throws are {average}")

main()