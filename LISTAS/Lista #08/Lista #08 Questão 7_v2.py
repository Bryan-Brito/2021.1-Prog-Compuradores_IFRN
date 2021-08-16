print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))

count_maiusc = 0
count_num = 0
count_simb = 0
count_acento = 0
for i in range(len(senha)):
    
    if senha[i] == 'A' or 'B' or 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' or'J' or 'K' or 'L' or 'M' or 'N' or 'O' or 'P' or 'Q' or 'R' or 'S' or 'T' or 'U' or 'V' or 'W' or 'X' or 'Y' or 'Z':
        count_maiusc += 1
    elif senha[i] == 'Á' or 'á' or 'Ã' or 'ã' or 'À' or 'à' or 'Â' or 'â' or 'É' or 'é' or 'Ê' or 'ê' or 'Í' or 'í' or 'Ó' or 'ó' or 'Õ' or 'õ' or 'Ú' or 'ú':
        count_acento += 1
    elif senha[i] == 1 or senha[i] == 2 or senha[i] == 3 or senha[i] == 4 or senha[i] == 5 or senha[i] == 6 or senha[i] == 7 or senha[i] == 8 or senha[i] == 9 or senha[i] == 0:
        count_num += 1
    elif senha[i] == '#' or '$' or '@' or '&':
        count_simb += 1
                        
if len(senha) == 10 and count_maiusc == 1 and count_num == 3 and count_simb == 2:
    print('Senha fraca!')
elif len(senha) == 15 and count_maiusc == 3 and count_num == 5 and count_simb == 4:
    print('Senha forte!')
else:
    print('Senha média!')     

print('Maiusculas', count_maiusc, 'numeros', count_num, 'Simbolos', count_simb, 'Quantidade', len(senha))    