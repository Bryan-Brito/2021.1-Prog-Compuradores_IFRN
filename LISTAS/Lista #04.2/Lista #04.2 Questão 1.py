X = int(input("Insira um valor"))

Y = X%2

if X > 0 and Y == 0:
    print("Seu número é par e positivo")
elif X < 0 and Y == 0:
    print("Seu número é par e negativo")
elif X > 0 and Y == 1:
    print("Seu número é ímpar e positivo")
elif X < 0 and Y == 1:
    print("Seu número é ímpar e negativo")
elif X == 0:
    print("Seu número é nulo")