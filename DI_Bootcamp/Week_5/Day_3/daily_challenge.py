
def information():
    output_list = []
    temp_list = []
    for _ in range(2):
        temp_2 = []
        temp_2.append(input("What is your name? "))
        temp_2.append(int(input("What is your age? ")))
        temp_2.append(int(input("What is your score? ")))
        temp_list = tuple(temp_2)
        output_list.append(temp_list)
        
    output_list.sort( key = lambda x: (x[0], x[1], x[2]))
    print(output_list)

information()