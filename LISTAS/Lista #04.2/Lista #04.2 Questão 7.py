print("Vamos criar uma lista numérica em ordem decrescente")

X = int(input("Insira o primeiro valor:"))
Y = int(input("Insira o segundo valor:"))
Z = int(input("Insira o terceiro valor:"))

if X > Y > Z:
    print("A ordem decrescente dos números é:", X, Y, Z)

elif X > Z > Y:
    print("A ordem decrescente dos números é:", X, Z, Y)

elif Y > X > Z:
    print("A ordem decrescente dos números é:", Y, X, Z)

elif Y > Z > X:
    print("A ordem decrescente dos números é:", Y, Z, X)

elif Z > X > Y:
    print("A ordem decrescente dos números é:", Z, X, Y)

elif Z > Y > X:
    print("A ordem decrescente dos números é:", Z, Y, X)