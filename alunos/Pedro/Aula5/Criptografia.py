import string
alphabet = string.ascii_letters
alphabet_tratado = alphabet + "1" + "2" + "3"


def EncriptarCifraDeCesar1(string):
    crypt = ""
    for ch in string:
        crypt += chr(ord(ch) + 3)
    return crypt


def DecriptarCifraDeCesar1(string):
    decrypt = ""
    for ch in string:
        decrypt += chr(ord(ch) - 3)
    return decrypt


def EncriptarCifraDeCesar2(string):
    crypt = ""
    for ch in string:
        for index, ch_alph in enumerate(alphabet_tratado):
            if ch == ch_alph:
                crypt += alphabet_tratado[index + 3]
    return crypt


def DecriptarCifraDeCesar2(string):
    decrypt = ""
    for ch in string:
        for index, ch_alph in enumerate(alphabet_tratado):
            if ch == ch_alph:
                decrypt += alphabet_tratado[index - 3]
    return decrypt


def EncriptarCifraDeCesar3(dict, string):
    crypt = []
    for ch in string:
        crypt.append(dict[ch])
    return ''.join(crypt)


def DecriptarCifraDeCesar3(dict, string):
    decrypt = ""
    for ch in string:
        decrypt += dict[ch]
    return decrypt


message = input("Digite a mensagem a ser criptografada: ")

criptografia1 = EncriptarCifraDeCesar1(message)
decriptografia1 = DecriptarCifraDeCesar1(criptografia1)

print(criptografia1)
print(decriptografia1)

criptografia2 = EncriptarCifraDeCesar2(message)
decriptografia2 = DecriptarCifraDeCesar2(criptografia2)

print("---------------")
print(criptografia2)
print(decriptografia2)

dict_crypt = {index: ch_alph for index, ch_alph in zip(alphabet, alphabet_tratado[3:])}
dict_decrypt = {ch_alph: index for index, ch_alph in zip(alphabet, alphabet_tratado[3:])}
dict_crypt[" "] = "_"
dict_decrypt["_"] = " "

criptografia3 = EncriptarCifraDeCesar3(dict_crypt, message)
decriptografia3 = DecriptarCifraDeCesar3(dict_decrypt, criptografia3)

print("---------------")
print(criptografia3)
print(decriptografia3)
