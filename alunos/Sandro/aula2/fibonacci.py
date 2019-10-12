def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2: # Condição de saída do recursão
        return 1# Retorna um valor ao invéz de chamar a função
    else:
        return fibonacci(num-1) + fibonacci(num-2)# Bloco de codigo que vai se repetir até atingir a condição para sair da recursão

print(fibonacci(8))