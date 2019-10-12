#Valor (float)
#Desconto1 = (float)
#Desconto2 = (float)
input('File Duplo: 1\nAlcatra: 2\nPicanha: 3')
TipoCarne= int(input("Qual a carne comprada:"))
Quantidade =float(input("Qual a quantidade comprada:"))
ModoPagamento = int(input("Se pagar com cartão Tabajara digite 1, outra forma de pagamento digite 2:"))
if TipoCarne == 1:
        Carne =str("File Duplo") ;Valor = float(5.8)
elif TipoCarne == 2:
    Carne = str("Alcatra"); Valor = float(6.8)
elif TipoCarne == 3:
   Carne = str("Picanha"); Valor = float(7.8)

if ModoPagamento ==1:
    ModoPagamentodescricao = "Cartão Tabajara"
    Else: ModoPagamentodescricao = "Outro modo"

if ModoPagamento == 1:
    Desconto1 = (0.05)
Else: Desconto1 = (0)

if Quantidade > 5:
    Desconto2 = (0.9)
    Else: Desconto2 = (0)

ValorTotal=Valor * Quantidade
print (f'Compra de Carne:')
print (f'Tipo de Carne= {Carne}')
print (f'Quantidade= {Quantidade}')
print (f'Valor total da Compra= {ValorTotal}')
print (f'Tipo de pagamento= {ModoPagamentodescricao}')
print (f'Desconto= {Desconto1*Valor*Quantidade+Desconto2}')
print (f'VAlor final da Compra= {ValorTotal-Desconto1*Valor*Quantidade+Desconto2}')