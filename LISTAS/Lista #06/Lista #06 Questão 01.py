idade = int(input("Insira sua idade: "))

cont = 0
cont_sup = 0

while (cont <= 10):
    cont = cont + 1
    if (idade >= 18):
        cont_sup = cont_sup + 1
    idade = int(input("Insira sua idade: "))    

print("Quantidade de pessoas maiores de idade: ", cont_sup)