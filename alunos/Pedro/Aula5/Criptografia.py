def EncriptarCifraDeCesar(string):
    crypt = ""
    for ch in string:
        crypt = crypt + chr(ord(ch) + 3)
    return crypt


def DecriptarCifraDeCesar(string):
    decrypt = ""
    for ch in string:
        decrypt = decrypt + chr(ord(ch) - 3)
    return decrypt


message = input("Digite a mensagem a ser criptografada: ")
criptografia = EncriptarCifraDeCesar(message)
decriptografia = DecriptarCifraDeCesar(criptografia)

print(criptografia)
print(decriptografia)