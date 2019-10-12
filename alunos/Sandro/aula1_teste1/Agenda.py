print("""
      Cadastrar contato digite 1
      lista contato digite 2
      monstrar contato digite 3
      atualizar contato digite 4
      excluir contato digite 5
      Sair digite 6
      """)
dictionary = {}
option = int(input("Digite sua opção"))
while(option !=6):
    if option == 1:
        name = str(input("Digite o nome:"))
        telefone =int(input("Digite o telefone:"))
        dictionary[name]= telefone
    if option == 2:
        print (dictionary)#imprimir com for
    if option == 3:
        name = str(input("Digite o nome para consultar:"))
        print(dictionary[name])
    if option == 4:
        name = str(input("Digite o nome a atualizar na lista:"))
        telefone =int(input("Digite o novo telefone:"))
        dictionary[name]= telefone
    if option == 5:
        name = str(input("Digite o nome a excluir da lista:"))
        del dictionary[name]
    option = int(input("Digite sua opção"))
print ("Encerrado acesso a Lista")