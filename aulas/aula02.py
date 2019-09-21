# Tipos de dados

# Tipo literal sequencia de caracteres (string)

nome = 'alexandre'          # Variavel do tipo literal
telefone = "923834734834"
sobrenome = """	*********************
	menu
	1) Escolha seu suco
	2) Escolha seu lanche
	**********************
"""
numero = str(2838748274827834) # conversao de tipo
#print(type(nome)) # type verifica o tipo da variavel
#print(dir(nome)) # dir inspeciona o objeto
#print(vars()) # mostra as variaveis de contexto
#help(<classe ou metodo>)
#print(nome)

# Formatação de Strings


nome_completo = 'meu nome é {nome} meu telefone é {telefone}'.format(telefone=telefone, nome=nome)
nome_completo2 = f'meu nome é {nome} meu telefone é {telefone}'

print(nome_completo)
print(nome_completo2)

# https://pyformat.info para maiores informações sobre py format
# https://wiki.python.org.br/TudoSobrePythoneUnicode

# Tipo numerico

numero = 8
fracionario = 8.4
# int()
nome_numero = int('8') # conversao de tipo
f_numero = float(numero)
print(numero)
print(f_numero)


# Booleano
verdadeiro = True, 1
falso = False, 0,'', None


# Função de leitura do teclado
nota1 = int(input('digite a primeira nota')) # para a execusao e aguarda ate que algum valor seja inputado
nota2 = int(input('digite a primeira nota'))
nota3 = int(input('digite a primeira nota'))
nota4 = int(input('digite a primeira nota'))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'{nome} sua media e {media}')
#TUDO QUE VEM DO INPUT É STRINGnota1 = int(input('digite a primeira nota'))

# Função para apresentar resuldado na tela do monitor

print(f'OI {nome}', nome_completo2, sep=';', end=' finalmente visivel')


# Faça um programa que receba 4 notas o nome de uma aluno e imprima o nome e a media das notas

# Estrutura de decisao


#if <condicao logica>:
#	bloco de codigo
#	.
#	.
#	.
#	.

# Faça um programa que receba 4 notas o nome de uma aluno, e calcule a media, se a media for menor que 3 esta reprovado, se a media estiver entre 3 e 7 esta em recuperação se a media for maior que 7 o aluno esta aprovado.
nota1 = int(input('digite a primeira nota')) # para a execusao e aguarda ate que algum valor seja inputado
nota2 = int(input('digite a primeira nota'))
nota3 = int(input('digite a primeira nota'))
nota4 = int(input('digite a primeira nota'))

media = (nota1 + nota2 + nota3 + nota4) / 4


if not media >= 7:
	print('aluno reprovado')
else:
	print('aluno aprovado')

print(f'{nome} sua media e {media}')



