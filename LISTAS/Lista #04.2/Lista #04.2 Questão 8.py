print("Vamos calcular seu IMC (Índice de Massa Corporal)")

idade = int(input("Insira sua idade:"))
peso = float(input("Insira o seu peso:", ))
altura = float(input("Insira sua altura:", ))

IMC = peso/altura**2

if idade >= 18:
    print("Calculando...")
    if 18.5 <= IMC <= 24.9:
        print("Peso normal")

    elif 25 <= IMC <= 29.9:
       print("Sobrepeso")

    elif 30 <= IMC <= 34.9:
       print("Obesidade grau I")

    elif 35 <= IMC <= 39.9:
       print("Obesidade grau II")

    elif IMC >= 40:
       print("Obesidade grau III ou Mórbida")

    elif IMC < 18.5:
       print("Abaixo do peso")

else:
    print("Só podemos calcular IMC em adultos")