calculo = 0 
media = 0
media_h = 0
media_m = 0
qtd_h = 0
qtd_m = 0
idade_h = 0
idade_m = 0

for P in range(1,11):
  print("{}ªpessoa".format(P))
  idade = int (input("Insira sua idade:"))
  genero = str(input("Insira seu gênero(M/H): "))
  calculo = calculo + idade
  if (genero == 'H' or genero == 'h'):
      qtd_h = qtd_h + 1
      idade_h = idade_h + idade
  elif (genero == 'M' or genero == 'm'):
      qtd_m = qtd_m + 1
      idade_m = idade_m + idade

media = calculo/10
media_h = idade_h/qtd_h
media_m = idade_m/qtd_m

print("Média geral: {}".format(media))
print("Média homem: {}".format(media_h))
print("Média mulher: {}".format(media_m))