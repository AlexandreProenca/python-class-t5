list_comprehensions = [item ** 2 for item in range(10)]
dict_comprehensions = {item: item ** 2 for item in range(10)}

print(list_comprehensions)
print(dict_comprehensions)

import string
ascii_uppercase = [str(item).upper() for item in string.ascii_lowercase]
print(ascii_uppercase)

ascii_aplus = ["a" + item for item in string.ascii_lowercase]
print(ascii_aplus)
print("\n-----------------\n")

alphabet = string.ascii_letters
dict_cifra_cesar = {letter: chr(ord(letter) + 3) for letter in alphabet}
dict_cifra_cesar_decoder = {v: k for (k, v) in dict_cifra_cesar.items()}
print(dict_cifra_cesar)
print("-----------------")
print(dict_cifra_cesar_decoder)
