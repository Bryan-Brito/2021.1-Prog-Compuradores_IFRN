import sys

try:
    X = float(input("Insira o valor de 'X' no plano cartesiano: "))
    Y = float(input("Insira o valor de 'Y' no plano cartesiano: "))
    if X > 0 and Y > 0:
        print("Após a leitura das coordenadas, percebe-se que elas estão no 1º quadrante")
    elif (X < 0) and (Y > 0):
        print("Após a leitura das coordenadas, percebe-se que elas estão no 2º quadrante")
    elif (X < 0) and (Y < 0):
        print("Após a leitura das coordenadas, percebe-se que elas estão no 3º quadrante")
    elif (X > 0) and (Y < 0):
        print("Após a leitura das coordenadas, percebe-se que elas estão no 4º quadrante")

except ValueError:
    print('ERRO: String não pode ser convertido para int/float')


#ValueError: could not convert string to float