
shifting = int(input("By how many place you want to shift?\t"))

text_input = str(input("Give me your text to encrypt:\t"))

result_text = ""

for letter in text_input:

    result_text += chr(ord(letter) + shifting) #shifts by the amount of shifts be chose

print(f"Your result Text is: {result_text}")

decrypted_text = ""

for letter in result_text:
    decrypted_text += chr(ord(letter) - shifting)

print(f"This the decrypted message: {decrypted_text}")
