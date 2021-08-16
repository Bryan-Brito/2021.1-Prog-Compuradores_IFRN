Xa, Ya, Za = input("Insira os pontos de 'A' presentes no plano cartesiano. X, Y e Z, respectivamente").split()
Xb, Yb, Zb = input("Insira os pontos de 'B' presentes no plano cartesiano. X, Y e Z, respectivamente").split()

Xa = int(Xa)
Ya = int(Ya)
Za = int(Za)
Xb = int(Xb)
Yb = int(Yb)
Zb = int(Zb)

dAB = float(((Xb - Xa)**2 + (Yb - Ya)**2 + (Zb - Za)**2)**(1/2))

print("A distância entre os pontos é:", "%.2f" % dAB)