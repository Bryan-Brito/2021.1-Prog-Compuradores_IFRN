while True:
    print('JOGO DO ROBÔ!')
    X, Y = input('Insira as coordenadas do robô dentro do plano cartesiano (X e Y): ').split()
    X = int(X)
    Y = int(Y)
    
    X2 = int(X)
    Y2 = int(Y)
    count = 0
    
    while True:
        move = input('Para onde o robô deve mover-se? (Cima = U, Baixo = D, Esquerda = L, Direita = R): ')

        if move == 'U' or move == 'u':
            Y2 += 1 
            X2 = X2
            count += 1
        elif move == 'D' or move == 'd':
            Y2 -= 1
            X2 = X2
            count += 1
        elif move == 'L' or move == 'l':
            X2 -= 1
            Y2 = Y2
            count += 1
        elif move == 'R' or move == 'r':
            X2 += 1
            Y2 = Y2
            count += 1
        
        print('Eixo X: ', X2, 'Eixo Y: ', Y2)
        situacao = input('Deseja continuar? (S/N) ')

        if situacao == 'S' or situacao == 's': continue

        elif situacao == 'N' or situacao == 'n':break
    break

quadrante = ''
if X > 0 and Y > 0:
    quadrante = '1º'
elif X > 0 and Y < 0:
    quadrante = '4º'
elif X < 0 and Y > 0:
    quadrante = '2º'
elif X < 0 and Y < 0:
    quadrante = '3º'

quadrante2 = ''
if X2 > 0 and Y2 > 0:
    quadrante2 = '1º'
elif X2 > 0 and Y2 < 0:
    quadrante2 = '4º'
elif X2 < 0 and Y2 > 0:
    quadrante2 = '2º'
elif X2 < 0 and Y2 < 0:
    quadrante2 = '3º'
print('Posição inicial... Eixo X: {0}, Eixo Y: {1} '.format(X, Y))
print('Posição final...   Eixo X: {0}, Eixo Y: {1} '.format(X2, Y2))
print('Quantidade de movimentos válidos: ', count)
print('Quadrante inicial: {0}, Quadrante final: {1}'.format(quadrante, quadrante2))