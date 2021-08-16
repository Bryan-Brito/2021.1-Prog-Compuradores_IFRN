import random 

valores_aleatorios = []
n = int(input('numero: '))
for i in range(0,n):
    x = random.randint(0,99)
    valores_aleatorios.append(x)

y = sorted(valores_aleatorios)
print(valores_aleatorios)
print('-'*50)
print('Lista ordenada: ', y)
