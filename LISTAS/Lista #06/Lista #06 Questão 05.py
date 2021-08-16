M = 0
m = 0
soma = 0
num = 1
quant = 0
while num != 0:
  num = float(input("Digite o numero:"))  
  if num > M:
       M = num 
  if num < m:
       m > num
  if m == 0:
       m = num  
print("Maior número: {} \n menor número:{}".format(M, m))