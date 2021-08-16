ano = int(input("Informe o ano"))

X = ano%4
if X == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")