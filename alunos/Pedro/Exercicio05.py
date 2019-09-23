var_1 = int(input("Digite o 1º valor: "))
var_2 = int(input("Digite o 2º valor: "))
var_3 = int(input("Digite o 3º valor: "))

if var_1 > var_2:
    if var_1 > var_3:
        maior = var_1
        if var_2 > var_3:
            meio = var_2
            menor = var_3
        else:
            meio = var_3
            menor = var_2
    else:
        maior = var_3
        if var_1 > var_2:
            meio = var_1
            menor = var_2
        else:
            meio = var_2
            menor = var_1
else:
    if var_2 > var_3:
        maior = var_2
        if var_1 > var_3:
            meio = var_1
            menor = var_3
        else:
            meio = var_3
            menor = var_1
    else:
        maior = var_3
        if var_1 > var_2:
            meio = var_1
            menor = var_2
        else:
            meio = var_2
            menor = var_1

print(f"A ordem crescente é {menor}, {meio}, {maior}")