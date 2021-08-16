lista_1 = [100, 50, 20, 10, 5, 2, 1]
lista_2 = [] 

while True:
   valor_saque = int(input("\nValor do Saque: "))

   if (valor_saque > 0):
      valor_auxiliar = valor_saque
      lista_auxiliar = [0, 0, 0, 0, 0, 0, 0]
      posicao        = 0

      while posicao < len(lista_auxiliar):
         cedulas        = valor_auxiliar // lista_1[posicao]
         valor_auxiliar = valor_auxiliar % lista_1[posicao]
         lista_auxiliar[posicao] = cedulas
         posicao += 1
      
      lista_2.append(lista_auxiliar)

      print("\nValor do Saque: R$ {0:.2f}".format(valor_saque))
      print('-'*80)

      for i in range(len(lista_auxiliar)):
         str_modelo = '{0:>3} Cédulas de R${1:>8.2f} .....{0:>3} x R${1:>8.2f} = R${2:>8.2f}'
         print(str_modelo.format(lista_auxiliar[i], lista_1[i], lista_auxiliar[i]*lista_1[i]))

      print('-'*80)

      continuar = ''
      while True:
         continuar = input('Fazer novo saque (S/N)? ').upper()
         if continuar == 'N' or continuar == 'S': break

      if continuar == 'S': continue

      print('='*80)

      for i in range(len(lista_1)):
         soma = 0
         for j in range(len(lista_2)):
            soma += lista_2[j][i]
         str_modelo = '{0:>3} Cédulas de R${1:>8.2f} .....{0:>3} x R${1:>8.2f} = R${2:>8.2f}'   
         print(str_modelo.format(soma, lista_1[i], soma*lista_1[i]))

      print('='*80)

      if continuar == 'N': break
   else:
      print('Impossível sacar valor NEGATIVO...')
print('oi', lista_2)


#1. Vai armazenar a quantidade de cédulas de cada operação;
#2. Vai calcular a quantidade de cédulas que serão utilizadas no saque;
#3. Vai printar, com o método .format, a tabela contendo as cédulas que foram sacadas;
#4. Irá verificar se o que o usuário digitou é válido;
#5. Irá verificar se é desejo do usuário fazer outra operação;
#6. Irá imprimir a quantidade de cédulas retiradas do caixa ao final da operação;
#7. Irá encerrar a operação.