hattb = [2, 3, 4, 2, 1]
iattb = [4, 2, 3, 2, 1]
lista = []
for i in range(0,5):
    lista.append(hattb[i]-iattb[i])
print(lista)

for i in range(0,5):
    if lista[i]>=0:
        lista[i] = hattb[i]-lista[i]
    else:
        lista[i] = hattb[i]

cont = 0
for i in lista:
    cont+=i

total = 0
for i in iattb:
    total+=i

porc = cont*100/total
print(lista)
print(cont)
print(porc,"%")