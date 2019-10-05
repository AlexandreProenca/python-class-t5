frutas = ["banana", "maca"]
frutas += ["laranja"]
frutas = ["coco"] + frutas
frutas.append("goiaba")
frutas.insert(1, "pepino")

for fruta in frutas:
    print(fruta)

print("--------------")
frutas.pop(1)
frutas.remove("banana")

for fruta in frutas:
    print(fruta)

print("--------------")
frutas.reverse()
for fruta in frutas:
    print(fruta)

print("--------------")
frutas.sort()

for fruta in frutas:
    print(fruta)

matrix = [[1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]]
print(matrix[1][0:-1])

for el in matrix[1][1:-1]:
    print(el)

print("--------------")
for el in matrix[1][1:-1]:
    if el == 4:
        continue                    #pula para o proximo elemento, se "break", pausa
    print(el)
# tupla é declarada por parenteses

# comprehensions
lista = [x*2 for x in range(1, 10, 3)]

for indice, valor in enumerate(lista):
    print(f"indice {indice} da lista {valor}")
else:                               #caso o lopping ocorra perfeitamente
    print("Execucao feita com sucesso")