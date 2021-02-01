birthday = input("When were you born? please write it in DD MM YYYY: ")
candle_count = int(birthday[-1])
day, month, year = birthday.split(' ')
year = int(year) # checks for birthyear
top_count = int((11-candle_count)/2)
top_count_right = top_count
if candle_count%2 == 0:
    top_count_right += 1    # if there is an even number of candle, add another line to the right, so the lenght will stay the same

# Defining symbols

line = "_"
candle = "i"
space = " "
roof = "^"
bottom = "~"

# Cake-function

def cake():
    print(f"{4*space}{top_count*line}{candle_count*candle}{top_count_right*line}")
    print(f"{3*space}|:H:a:p:p:y:|")
    print(f"{1*space}{2*line}|{11*line}|{2*line}")
    print(f"|{17*roof}|")
    print(f"|:B:i:r:t:h:d:a:y:|")
    print(f"|{17*space}|")
    print(f"{19*bottom}")

# Print
if year%4 == 0: # if leap year -> 2 cakes
    cake()
    print("")
    cake()
else:
    cake()