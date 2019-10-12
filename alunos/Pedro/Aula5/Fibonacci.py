def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num - 2) + Fibonacci(num - 1)


num = int(input("Digite o numero que voce quer ver o fibonacci: "))

for x in range(num):
    print(f"{x} - {Fibonacci(x)}")
