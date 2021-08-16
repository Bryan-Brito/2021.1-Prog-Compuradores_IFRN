cpf = input('Insira seu CPF(Somente números): ')

situacao = ' '

while situacao != 'Válido':
      if len(cpf) == 11:
           print('################')
           print('#  CPF válido  #')
           print('################')
      if len(cpf) == 11:break
      else:
           print('################')
           print('# CPF inválido #')
           print('################')
           cpf = input('Insira seu novamente CPF(Somente números): ')
           situacao = 'Inválido'