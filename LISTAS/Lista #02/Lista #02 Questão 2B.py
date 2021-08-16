c = float(input("Insira aqui a quantia do capital:"))

i = float(input("Insira a taxa a ser cobrada:"))

t = float(input("Por quanto tempo foi cobrado? (Em meses)"))

M = float(c * (1 + i/100) ** t)
print(M)