from datetime import date


def MostrarAnoNascimento(name="Pedro", age=15): # isso é uma função
    """
    :param name: nome do peão
    :param age: idade do peão
    :return: retorna a data de nascimento do cidadão
    """
    born_year = date.today().year - age
    return "meu nome é: " + name + " minha idade é: " + str(age) + " e você nasceu em: " + str(born_year)


input_name = input("Digite seu nome aqui: ")
input_age = input("Digite sua idade: ")

print(input_name)
print(input_age)
if input_age == "":
    if input_name == "":
        frase = MostrarAnoNascimento()
    else:
        frase = MostrarAnoNascimento(name=input_name)
else:
    input_age = int(input_age)
    if input_name == "":
        frase = MostrarAnoNascimento(age=int(input_age))
    else:
        frase = MostrarAnoNascimento(age=int(input_age), name=input_name)

print(frase)

teste = input_name.split()      # isso é um método
print(teste)


def SomarNumeros1(*numeros):    # recebe uma tupla
    return sum(numeros)


def SomarNumeros2(numeros):
    return sum(numeros)


sum1 = SomarNumeros1(1, 2, 3, 4, 5, 6)
sum2 = SomarNumeros2([1, 2, 3, 4, 5, 6])
print(f"{sum1} - {sum2}")


def Execute(func, *param):
    def Void():         # um void nao retorna nada
        pass
    return func(*param)


print(Execute(SomarNumeros1, 1, 2, 3, 4))


def f(x):
    def g(y):
        return x*y
    return g(3)


print(f(2))


def MediaDeString(string):
    valores = [float(num) for num in string.split()]
    return sum(valores)/len(valores)


print(MediaDeString('1 2 3 4 5 6'))
