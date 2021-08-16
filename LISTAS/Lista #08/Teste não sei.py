letra_1 = str(input('Digite uma letra: '))
letra_2 = str(input('Digite outra letra: '))

# Exibe a letra digitada, o código ASC e o código binário
asc = ord(letra_1)
print('A letra digitada foi: {0} / ASC: {1} / Binário: {1:b}'.format(letra_1, asc))

# Exibe a letra digitada, o código ASC e o código binário
asc = ord(letra_2)
print('A letra digitada foi: {0} / ASC: {1} / Binário: {1:b}'.format(letra_2, asc))

if (letra_1 == letra_2):
   print('São Iguais...')
else:
   print('São Diferentes...')