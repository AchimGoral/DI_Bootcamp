# Exercise_1

print (abs.__doc__)


def abs(number):
    """Take the input value and return a positive number. A complex number will be returned as a positive number"""
    pass

print("")
print (print.__doc__)


def print(input_value):
    """Prints out numbers, strings, dictionaries, lists by writing it in the Terminal. CLinebreak after every print"""
    pass


print("")
print(len.__doc__)

def len(input_value):
    """Cunts the number of items in the input and returns this value as an int"""
    pass

print("")

# Exercise_2

class Currency:

    def __init__(self, currency, value):
        self.value = value
        if self.value > 1:
            self.currency = currency + "s"
        else: 
            self.currency = currency

    
    def __str__(self):
        return f"{self.value} {self.currency}"

    def __int__(self):
        return self.value

    def __repr__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return self.value + other
        elif self.currency == other.currency:
                return self.value + other.value
        else:
            print(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value = self.value + other
            return self
        elif self.currency == other.currency:
            self.value = self.value + other.value
            return self
        else:
            print(f"TypeError: Cannot add between Currency type <{self.currency}> and <{other.currency}>")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)

# Exercise_3

import datetime

def january():
    print(f"The 1. of january is in {datetime.datetime(2022, 1, 1)-datetime.datetime.today().replace(microsecond=0)}")

january()

# Exercise_4

import datetime

def next_holiday():
    x = datetime.datetime.now()
    print(f"Today is the: {x.strftime('%d %m %Y and %H h %M m %S s')}")
    print(f"The next holiday of Purim is in {datetime.datetime(2021, 2, 25)-datetime.datetime.today().replace(microsecond=0)}")

next_holiday()

# Exercise_5

from datetime import datetime

birdthay_input = input("Give my your Birthday in YYYY/MM/DD ")

def birthday(input_value):
    birth = datetime.strptime(input_value, "%Y/%m/%d")
    actual_date = datetime.now()
    minutes_lived = actual_date-birth
    print(f"You're living since {minutes_lived}")

birthday(birdthay_input)

# Exercise_6

def calc_age(seconds):

    earth_year = seconds/(365.25*24*60*60)

    mercury_year = earth_year/0.2408467
    venus_year = earth_year/0.61519726
    mars_year = earth_year/1.8808158
    jupiter_year = earth_year/11.862615
    saturn_year = earth_year/29.447498
    uranus_year = earth_year/84.016846
    neptune_year = earth_year/164.79132

    print(f"You are {earth_year} Earth-years old")
    print(f"On Mercury {mercury_year}, on venus {venus_year}, on mars {mars_year}, on jupiter {jupiter_year}, on saturn {saturn_year}, on uranus {uranus_year} and on neptune {neptune_year} years old")

calc_age(1000000000)

# Exercise_7

from faker import Faker

faker = Faker()

input_value = int(input("How many fake users? "))

new_dict = {}
users = []

def faker_add(amount):
    for _ in range(amount):
        new_dict['name'] = faker.name()
        new_dict['email'] = faker.email()
        new_dict['adress'] = faker.address()
        users.append(new_dict)
    print(users)
        
faker_add(input_value)