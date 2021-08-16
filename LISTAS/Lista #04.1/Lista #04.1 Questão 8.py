a = int(input("digite o lado de A", ))
b = int(input("digite o lado de B", ))
c = int(input("digite o lado de C", ))

if ((a > 0 and b > 0 and c > 0) and (a > c - b) or (a < b + c) and (b > a - c) or (b < a + c) and (c > a - b) or (c < a + b)):
 print("é um triângulo")	
	
if (a == b and b == c) and (a > 0 and b > 0 and c > 0):
			 
     print("Seu triângulo é equilátero")
				
elif ((a != b and b!= c) and (a > 0 and b > 0 and c > 0)):
				
     print("Seu triângulo é escaleno")
					
elif (((a == b and b != c) or (b == a and a!=c) or (b == c and c!=a) or (c == a and a!=b) or (c == b and b!=a)) and (a > 0 and b > 0 and c > 0)):

     print("Seu triângulo é isósceles")						
else:
	 print("Impossível calcular")