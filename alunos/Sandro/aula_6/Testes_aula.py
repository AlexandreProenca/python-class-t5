#tratamento de erros e exceçoes-BaseException/exception
#print(ZeroDivisionError(0/0))
print('erro')

x = 10
if x == 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

nome = ("paulo",)
carro = ("paulo", )
print(id(nome))
print(id(carro))

#tratar exceção atraves do try

try:
    print(0/0)
    print('erro')
except KeyError:
    print("não há divisão por zero")

print('Aqui.')