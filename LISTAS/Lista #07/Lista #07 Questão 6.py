import random 

variancia = 0
desvio = 0
media = 0
valores_aleatorios = []
n = int(input('numero: '))
for i in range(0,n):
    x = random.randint(0,99)
    valores_aleatorios.append(x)
    media = media + x

    z = len(valores_aleatorios)

    if z%2 == 0:
        n1 = (z/2)-1
        n2 = z/2
    else:
        m1 = z/2
    
for i in range(0,n):

    variancia = variancia + ((valores_aleatorios[i] - (media/n))**2)
    print("%.1f"%variancia)

variancia_2 = variancia/(n-1)
desvio = variancia_2**(1/2)

m1 = int(m1)
n1 = int(n1)
n2 = int(n2)
print(valores_aleatorios)
print('-'*50)
print('Média dos valores dos elementos do vetor: ', "%.1f"%float(media/n))

if z%2 == 0:
    print('Mediana é: ', valores_aleatorios[n1], valores_aleatorios[n2])
else:
    print('Mediana é: ', valores_aleatorios[m1])

print('A variância é: ', variancia_2)
print('Imprimindo o desvio referente ao valor: ', "%.1f"%desvio)