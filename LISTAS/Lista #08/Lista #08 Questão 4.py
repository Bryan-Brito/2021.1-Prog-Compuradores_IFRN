X = input('Digite um palíndromo: ')

Y = X[::-1]

if X.lower() == Y.lower():
   print("São Palíndromos")
else:
   print("Não São Palíndromos")

print(X)
print(Y)