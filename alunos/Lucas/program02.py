# Faça um Programa que peça as 4 notas bimestrais e mostre a média, mas com um IF no meio

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
numero4 = float(input('Digite o quarto número: '))

media = (numero1 + numero2 + numero3 + numero4) / 4

print(f'A média é {media}.')

if media >= 7:
    print('Aprovado!')

elif media >= 3:
    print('Recuperação!')

else:
    print('Reprovado!')






