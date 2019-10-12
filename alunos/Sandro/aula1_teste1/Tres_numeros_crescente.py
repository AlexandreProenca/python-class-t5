numero1= int(input("inserir o valor do numero 1:"))
numero2= int(input("inserir o valor do numero 2:"))
numero3= int(input("inserir o valor do numero 3:"))
if numero1 > numero2 and numero1> numero3:
    maior1 = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior1 = numero2
else:
    maior1 = numero3

if numero1 < numero2 and numero1 < numero3:
    maior3 = numero1
elif numero2 < numero1 and numero2 < numero3:
    maior3 = numero2
else:
   maior3 = numero3

if numero1 > numero2 and numero1< numero3:
    maior2 = numero1
elif numero2 > numero1 and numero2 < numero3:
    maior2 = numero2
else:
    maior2 = numero3


print (f'os numeros inseridos de forma crescente são:{maior3},{maior2},{maior1}')
