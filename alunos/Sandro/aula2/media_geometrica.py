# a= int(input("digite valor 1"))
# b= int(input("digite valor 2"))
# c= int(input("digite valor 3"))


def media(a, b, c):
    produto = a*b*c
    inverso_raiz = (produto) ** (1/3)
    return inverso_raiz


res = media(2, 4, 8)
print(res)
