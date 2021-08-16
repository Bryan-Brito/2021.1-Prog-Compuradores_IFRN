print("Vamos calcular o tipo do triângulo")
A = int(input("Informe o primeiro ângulo"))
B = int(input("Informe o segundo ângulo"))
C = int(input("Informe o terceiro ângulo"))

if (A > 0 and B > 0 and C > 0) and A + B + C == 180:
    if A < 90 and B < 90 and C < 90:
        print("Seu triângulo é acutângulo")
    
    elif A == 90 or B == 90 or C == 90:
        print("Seu triângulo é retângulo")
    
    elif A > 90 or B > 90 or C > 90:
        print("Seu triângulo é obtusângulo")
else:
    print("Impossível calcular")