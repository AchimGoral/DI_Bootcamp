n = 1234
result = 0
for i in range(32): # range in bits
    result <<= 1 # bitwise left shift and assignment to operand
    result |= n & 1 # n & 1 checks if the last bit is 1 or 0. if it is 1, it produces a 1
    # result = result OR n & 1
    n >>= 1

print(result)