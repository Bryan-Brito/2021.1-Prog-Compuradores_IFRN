import random 

valores_aleatorios = []
zero   = []
um     = []
dois   = []
tres   = []
quatro = []
cinco  = []
seis   = []
sete   = []
oito   = []
nove   = []
n = int(input('numero: '))
for i in range(0,n):
    x = random.randint(0,10)
    if x == 0:
        zero.append(x)
    elif x == 1:
        um.append(x)
    elif x == 2:
        dois.append(x)
    elif x == 3:
        tres.append(x)
    elif x == 4:
        quatro.append(x)
    elif x == 5:
        cinco.append(x)
    elif x == 6:
        seis.append(x)
    elif x == 7:
        sete.append(x)
    elif x == 8:
        oito.append(x)
    elif x == 9:
        nove.append(x)
    valores_aleatorios.append(x)
    
 
print(valores_aleatorios)
print('-'*50)
print('Quantidade de números 0: ', len(zero))
print('Quantidade de números 1: ', len(um))
print('Quantidade de números 2: ', len(dois))
print('Quantidade de números 3: ', len(tres))
print('Quantidade de números 4: ', len(quatro))
print('Quantidade de números 5: ', len(cinco))
print('Quantidade de números 6: ', len(seis))
print('Quantidade de números 7: ', len(sete))
print('Quantidade de números 8: ', len(oito))
print('Quantidade de números 9: ', len(nove))