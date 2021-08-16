A = int(input("Insira o valor de A:"))
B = int(input("Insira o valor de B:"))
C = int(input("Insira o valor de C:"))

X = (B**2) - 4*A*C

if X < 0:
    print("Impossível de calcular")

elif X == 0:
    print("As raízes são iguais")

else:
    X1 = ((-B) + pow(X, 1/2))/2*A
    X2 = ((-B) - pow(X, 1/2))/2*A
    print("Delta vale:", X)
    print("A primeira raiz é:", "%.2f" % X1)
    print("A segunda raiz é:", "%.2f" % X2)