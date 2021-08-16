print("Vamos calcular as raízes de uma equação de segundo grau utilizando o teorema de Bhaskara")

a = float(input("Coloque um valor para 'a'"))

b = float(input("Coloque um valor para 'b'"))

c = float(input("Coloque um valor para 'c'"))

delta = (b**2 - 4 * a * c)

if a == 0:
 print("O valor de 'a' deve ser diferente de 0")
elif delta<0:
 print("Sem raízes")
else:
 x1 = (- b + (delta)**(1/2))/(2*a)
 x2 = (- b - (delta)**(1/2))/(2*a)
 print("A primeira raiz é:", round(x1))
 print("E a segunda raiz é:", round(x2))