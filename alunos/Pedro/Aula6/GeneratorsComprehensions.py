def generator():
    n = 1
    print("Essa  uma função Generator")
    yield n

    n += 1
    yield n

    n += 1
    yield n


generator_expression = generator()
print(generator_expression)

for el in generator_expression:
    print(el)

generator_expression2 = (i for i in range(10))
print(generator_expression2)
print(next(generator_expression2))
print(next(generator_expression2))
print(next(generator_expression2))

