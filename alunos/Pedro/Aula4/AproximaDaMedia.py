qtd_numeros = int(input('Digite a quantidade de numeros a ser inserido: '))
lista_numeros = []
lista_diff = []
dict_numeros = {}

for index in range(qtd_numeros):
    lista_numeros += [int(input(f'{index+1}º numero: '))]

media = sum(lista_numeros)/qtd_numeros

for numero in lista_numeros:
    lista_diff += [abs(numero - media)]
    dict_numeros[abs(numero - media)] = numero

menor_erro = min(lista_diff)
num_prox = dict_numeros[menor_erro]

print(f"O numero mais proximo da media é {num_prox} com erro absoluto {menor_erro}")