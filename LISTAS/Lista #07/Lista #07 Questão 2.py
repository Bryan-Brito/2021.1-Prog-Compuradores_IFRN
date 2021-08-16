# 1) Faça um programa que leia um valor n, onde n será a quantidade de alunos. 
# 2) Em seguida leia a matricula e as notas (considere 2 notas por aluno) de cada aluno
# 3) e ao término imprima, conforme o modelo abaixo os dados informados anteriormente e a 
#    situação de cada aluno (considere as situações possíveis do IFRN e suas respectivas médias). 
# 4) Após a impressão da lista, o programa deverá exibir qual a maior nota, qual a menor nota, 
#    qual a média dos n alunos e
# 5) quantos alunos ficaram acima da média e o percentual em relação ao total de alunos.

# Tópico 1 
qt_alunos = int(input('Informe a quantidade de alunos: '))

matriculas_alunos = []
nota1_alunos = []
nota2_alunos = []

# Tópico 2
contador_alunos = 1
while contador_alunos <= qt_alunos:
   # Lendo as matrículas e as notas
   mat = int(input('Informe a Matrícula: '))

   # A FAZER: só aceitar notas entre 0 e 10 (inclusive)
   n1 = float(input('Informe a Nota 1: '))
   n2 = float(input('Informe a Nota 2: '))
   if (0 >= n1 >= 10) or (0 >= n1 >= 10):
      print('Tente novamente, valores inválidos')
      n1 = float(input('Informe a Nota 1: '))
      n2 = float(input('Informe a Nota 2: '))
          

   # Adicionando as matrículas e as notas nas listas
   matriculas_alunos.append(mat)
   nota1_alunos.append(n1)
   nota2_alunos.append(n2)

   contador_alunos += 1

# Tópico 3
print('MATRÍCULA        NOTA 1         NOTA 2         MÉDIA       SITUAÇÃO')
for i in range(0, len(matriculas_alunos)): 
   media = ((nota1_alunos[i]*2)+(nota2_alunos[i]*3))/5
   if (media >= 6):
      situacao = 'Aprovado'
   elif (media >= 2):
      situacao = 'Prova Final'
   else:
      situacao = 'Reprovado'
   # A FAZER: Exibir as notas com apenas 1 casa decimal
   print('{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}'.format(matriculas_alunos[i], "%.1f"%nota1_alunos[i], "%.1f"%nota2_alunos[i], "%.1f"%media, situacao))

# Tópico 4
media_turma = 0
maior_nota = 0
menor_nota = nota1_alunos[i] or nota2_alunos[i]
for i in range(0, len(matriculas_alunos)):
   # Obtendo a maior nota
   if nota1_alunos[i] > maior_nota: 
      maior_nota = nota1_alunos[i]
   if nota2_alunos[i] > maior_nota:
      maior_nota = nota2_alunos[i]
   
   # A FAZER: Corrigir a menor nota (está sendo sempre 0)
   # Obtendo a menor nota
   if nota1_alunos[i] < menor_nota: 
      menor_nota = nota1_alunos[i]
   if nota2_alunos[i] < menor_nota:
      menor_nota = nota2_alunos[i]

   # Calcular a média da turma
   media_turma += ((nota1_alunos[i]*2)+(nota2_alunos[i]*3))/5

# A FAZER: Exibir os valores com apenas 1 casa decimal
media_turma = media_turma / qt_alunos
print('Maior Nota: {0}      Menor Nota: {1}'.format("%.1f"%maior_nota, "%.1f"%menor_nota))
print('Média Turma: {0}'.format("%.1f"%media_turma))

# Tópico 5
qt_alunos_acima_media = percentual_acima_media = 0
for i in range(0, len(matriculas_alunos)):
   media = ((nota1_alunos[i]*2)+(nota2_alunos[i]*3))/5
   if (media >= media_turma):
      qt_alunos_acima_media += 1

# A FAZER: Exibir os valores com apenas 1 casa decimal
percentual_acima_media = qt_alunos_acima_media / qt_alunos * 100
print('Alunos Acima da Média: {0} ({1} %)'.format(qt_alunos_acima_media, "%.1f"%percentual_acima_media))