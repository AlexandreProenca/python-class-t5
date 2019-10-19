with open("teste.txt", "r") as file:
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()


with open("teste.txt", "rb") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='\n')
        line = file.readline()

print(lines[1], "----------")

with open("escrita.txt", "a") as file:
    file.write("Pedro\nSandro\n")
