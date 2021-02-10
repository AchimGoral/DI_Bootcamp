# # I/O files

# with open("test.txt", "w") as f:
#     f.write("adam@gmail.com\n")

# with open("test.txt", "a") as f:
#     f.write("Mike@ramsey.com\n")

# with open("test.txt", "a") as f:
#     f.write("Business@gmail.com\n")

# with open("test.txt", "a") as f:
#     f.write("Tom@yahoo.com\n")

# with open("test.txt", "a") as f:
#     f.write("Hello@gmail.com\n")

# with open("test.txt", "r") as f:
#     data = f.readlines()

# for person in data:
#     person = person.strip('\n')
#     print(f"sending email to {person}")

# JSON

import json

# load      read json from a file convert to python
# loads     string: convert a json string to python

# dump      convert from python to json and write to file
# dumps     convert from python to a sjson string

# thing = [
#     {
#         'name': 'bob',
#         'age': 55,
#         'stuff': True
#     },
#     {
#         'nums': [1,2,3],
#         'letters': ['a', 'b', 'c']
#     },
# ]

# with open('jfile.txt', 'w') as f:
#     json.dump(thing, f, indent=2)

# with open('jfile.txt', 'r') as f:
#     thing2 = json.load(f)

# Requests get and post

import requests
import json
import time

# resp = requests.get("http://api.open-notify.org/iss-now")


# data = resp.json()

for _ in range(10):
    resp = requests.get("http://api.open-notify.org/iss-now")
    data = resp.json()
    print(data['iss_position']['latitude'], data['iss_position']['longitude'])
    time.sleep(1)
    