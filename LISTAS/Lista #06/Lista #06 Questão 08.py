X = int(input("Digite o numero:"))

soma = 0
X1 = 1
X2 = 1

fib = [0,1,1]
for Z in range(2, X):
  cont = X1 + X2
  X1 = cont
  X2 = (cont - X2)
  fib.append(cont)

print("Fibonacci: ", fib)