numerador_media = 0
denominador_media = 4

# for index in range(denominador_media):
#     var = int(input(f"Digite o {index + 1}º numero: "))
#     numerador_media = numerador_media + var
# media = numerador_media/denominador_media

var_1 = int(input("Digite o 1º numero: "))
var_2 = int(input("Digite o 2º numero: "))
var_3 = int(input("Digite o 3º numero: "))
var_4 = int(input("Digite o 4º numero: "))

media = (var_1 + var_2 + var_3 + var_4)/4
aluno = input("Digite o nome do aluno: ")

print(f"A média aritimética das notas do {aluno} é: {media}")