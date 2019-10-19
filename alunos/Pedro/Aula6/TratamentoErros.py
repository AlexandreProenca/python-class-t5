# x = 10
# if x > 5:
#    raise Exception("X should not exced 6 5")

# import sys
# assert ('linux' in sys.platform), f"Your system isn't linux, is {sys.platform}"

# x = ["oi", ]
# y = ["oi", ]

# print(id(x))
# print(id(y))

# print((x is y))
# print((x == y))

try:
    print(1 / 0)
except ZeroDivisionError:
    print("Deu erro, divisão por zero")

try:
    while 1:
        pass
except KeyError:
    print("Erro de chave")
except KeyboardInterrupt:
    print("Voce saiu")


try:
    x = 1/0
except ArithmeticError:
    print("Deu erro")
else:
    print('That\'s ok')
finally:
    print("Foi")

