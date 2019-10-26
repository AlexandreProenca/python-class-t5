with open("c:/Users/RS5891/Documents/Prevs_VE.prv", 'r') as reader:
    file = reader.readlines()

with open("copia.txt",'w') as writer:
    for line_ap in (file):
        writer.write(line_ap)





#   print(reader.read())

