count_maiusc = []
count_num = []
count_simb = []
count_acento = []
count_spc = 0
while True:
    print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
    senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))
    
    if 10 <= len(senha) <= 15:
    
            for i in senha:
                asc = ord(i)
                
                if 65 <= asc <= 90:
                    count_maiusc.append(i)
                elif 48 <= asc <= 57:
                    count_num.append(i)
                elif asc == 35 or  asc == 36 or asc == 64 or asc == 38:
                    count_simb.append(i)
                elif asc == 193 or asc == 225 or asc == 195 or asc == 227 or asc == 192 or asc == 224 or asc == 194 or asc == 226 or asc == 201 or asc == 233 or asc == 202 or asc == 234 or asc == 205 or asc == 237 or asc == 211 or asc == 243 or asc == 212 or asc == 244 or asc == 213 or asc == 245 or asc == 218 or asc == 250:
                    count_acento.append(i)
                elif i == ' ':
                    count_spc += 1

            print('Numeros', count_num, 'maiusculas', count_maiusc, 'simbolos', count_simb, 'acentos', count_acento, 'Tamanho', len(senha))
            if len(count_acento) > 0 or count_spc > 0 or len(senha) > 15 or len(senha) < 10 or len(count_maiusc) == 0 or len(count_num) > 5 or len(count_num) < 3 or len(count_simb) < 2:
                print('')
                print("=====================")
                print('# SENHA INVÁLIDA!!! #') 
                print("=====================")
                print('')
                count_spc = 0
                count_num = []
                count_acento = []
                count_maiusc = []
                count_simb = []
                continue
            else: break
    else:
        print('')
        print("=====================")
        print('# SENHA INVÁLIDA!!! #') 
        print("=====================")
        print('')
        continue

if len(senha) == 10 and len(count_maiusc) == 1 and len(count_num) == 3 and len(count_simb) == 2:
    print('Senha fraca!')
elif len(senha) == 15 and len(count_maiusc) == 3 and (len(count_num) == 5 and count_num[0] != count_num[1] != count_num[2] != count_num[3] != count_num[4]) and (len(count_simb) == 4 and count_simb[0] != count_simb[1] != count_simb[2] != count_simb[3]):
    print('Senha forte!')
else:
    print('Senha média!')