import random 

valores_aleatorios = []
primeiro   = []
segundo    = []
terceiro   = []
quarto     = []
n = int(input('numero: '))
for i in range(0,n):
    x = random.randint(0,99)
    if 0 <= x <= 24:
        primeiro.append(x)
    elif 25 <= x <= 49:
        segundo.append(x)
    elif 50 <= x <= 74:
        terceiro.append(x)
    elif 75 <= x <= 99:
        quarto.append(x)
    valores_aleatorios.append(x)
    
 
print(valores_aleatorios)
print('-'*50)
print('Quantidade de números no primeiro quartil: ', len(primeiro))
print('Quantidade de números no segundo quartil : ', len(segundo))
print('Quantidade de números no terceiro quartil: ', len(terceiro))
print('Quantidade de números no quarto quartil  : ', len(quarto))