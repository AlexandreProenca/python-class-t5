def MediaGeometricaDeString(string):
    prod = 1
    for num in string.split():
        prod = prod*float(num)
    return prod**(1/len(string.split()))


numbers = input("Digite os numeros para o cálculo da média geométrica: ")
media_geometrica = MediaGeometricaDeString(numbers)

print(media_geometrica)