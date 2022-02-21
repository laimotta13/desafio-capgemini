lista1 = input("Digite uma palavra: ")

lista1 = list(lista1)

lista2 = []

i = 0

y = 0

for i in range(0, len(lista1)):
    if y == lista1[i]:
       lista2.append(lista1[i])
       i = i + 1
    else:
        y = y + 1
        
        
        
print(len(lista2))

