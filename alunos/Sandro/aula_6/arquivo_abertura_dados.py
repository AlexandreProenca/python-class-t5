with open("c:/Users/RS5891/Documents/Prevs_VE.prv", 'r') as file:
    line = file.readlines()
    while line != '':
        print(line, end="")
        for l in line:
            print(l)
        line = file.readline()


    print(line)


#   print(reader.read())

