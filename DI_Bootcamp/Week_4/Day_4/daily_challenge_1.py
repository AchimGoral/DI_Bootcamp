# start_str = "7 3Tsih%x i#sM $a #t%ir!"

matrix = [
    ["7","i","3"],
    ["T", "s", "i"],
    ["h", "%" ,"x"],
    ["i"," ","#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    [" ", "r", "!"]
]

decrypt = ""
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if matrix[i][j].isalpha() or matrix[i][j] == " ":
            decrypt += matrix[i][j]

print(decrypt)