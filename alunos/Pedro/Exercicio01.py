denominador_media = 4

# numerador_media = 0
# for index in range(denominador_media):
#     var = int(input(f"Digite a {index + 1}ª nota: "))
#     numerador_media = numerador_media + var

var_1 = int(input("Digite a 1º nota: "))
var_2 = int(input("Digite a 2º nota: "))
var_3 = int(input("Digite a 3º nota: "))
var_4 = int(input("Digite a 4º nota: "))
numerador_media = var_1 + var_2 + var_3 + var_4

media = numerador_media/denominador_media
aluno = input("Digite o nome do aluno: ")

print(f"A média aritimética das notas do {aluno} é: {media}")