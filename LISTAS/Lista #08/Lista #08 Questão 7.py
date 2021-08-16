print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))

for i in senha:
    if 10 <= len(senha) <= 15:
        if senha.count('Á','á','Ã') == 0 or senha.count('ã','À','à') == 0 or senha.count('Â','â','É') == 0 or senha.count('é','Ê','ê') == 0 or senha.count('Í','í','Ó') == 0 or senha.count('ó','Õ','õ') == 0 or senha.count('Ú','ú') == 0:
            if senha.count('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z') >= 1:
                if 3<= senha.count('0,1,2,3,4,5,6,7,8,9') <= 5:
                    if senha.count('#,$,@,$') >= 2:
                        print('Senha válida')     
                    else:
                        print('TENTE NOVAMENTE, NÃO ACEITAMOS OUTRO SÍMBOLO')
                        print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
                        senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))
                else:
                    print('TENTE NOVAMENTE, NÃO ACEITAMOS MAIS NÚMEROS')
                    print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
                    senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))
            else:
                print('TENTE NOVAMENTE, QUEREMOS 1 OU MAIS LETRAS MAIÚSCULAS')
                print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
                senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))
        else:
            print('TENTE NOVAMENTE, NÃO ACEITAMOS ACENTO')
            print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
            senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))
    else:   
        print('TENTE NOVAMENTE, QUANTIDADE INCORRETA')
        print('Insira uma senha, onde deverá conter:\nEntre 10 e 15 caracteres;')
        senha = str(input('Letras maiúsculas e minúsculas,\nE também símbolos especiais '))

for i in senha:
        if len(senha) == 10 and senha.count('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z') == 1 and senha.count('0,1,2,3,4,5,6,7,8,9') == 3 and senha.count('@,#,$,&') == 2:
            print('Senha fraca!')
        elif len(senha) == 15 and senha.count('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z') == 3 and senha.count('0,1,2,3,4,5,6,7,8,9') == 5 and senha.count('@,#,$,&') == 4:
            print('Senha forte!')
        else:
            print('Senha média!')         