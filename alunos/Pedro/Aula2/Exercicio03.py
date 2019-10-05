var_1 = int(input("Digite o 1º valor: "))
var_2 = int(input("Digite o 2º valor: "))
var_3 = int(input("Digite o 3º valor: "))

maior = var_3
if var_1 > var_2:
    if var_1 > var_3:
        maior = var_1
else:
    if var_2 > var_3:
        maior = var_2

print(f"A maior variável é {maior}")