n = 1

x = int(input('Insira a quantidade de elementos presentes na lista: '))

lista = []
for i in range(0,x):
    lista.append('none')
print("Lista: ", lista)

i = 1
while (i < x):
    n = int(input('Insira qual número será colocado na lista: '))
    if n == 0:
        print(lista)
    if n == 0:break

    if (len(lista) == x):
        del(lista[0])
    lista.append(n)
    print(lista)