def contagemRegressiva(n):
    if n == 0:
        print('Decolar!')
    else:
        print(n)
        contagemRegressiva(n-1)

contagemRegressiva(5)


def potencia(num, exp):
    if exp == 1:
        return num
    else:
        return potencia(num, exp - 1) * num


retorno = potencia(num=7, exp=3)
print(retorno)

num = 2
exp = 8
result = 1
for i in range(num, exp):
    result *= i

else:
    print(result)