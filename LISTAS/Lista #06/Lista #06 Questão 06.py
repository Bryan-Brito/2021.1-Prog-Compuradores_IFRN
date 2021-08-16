X = int(input("Insira um número positivo: "))

soma_par = 0
soma_impar = 0

while (X != 0):
    if (X % 2 == 0):
        soma_par = soma_par + X
    elif (X % 2 == 1):
        soma_impar = soma_impar + X
    X = int(input("Insira um número positivo: "))
    
print("Soma dos números pares:   ", soma_par)
print("Soma dos números ímpares: ", soma_impar)  