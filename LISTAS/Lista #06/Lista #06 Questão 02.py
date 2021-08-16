num_par = [[]]
for num in range(1, 11, 1):
    num = float(input("Digite o {} numero:". format(num)))
    calculo = num % 2
    if (calculo == 0):
      num_par[0].append(num)

print("Números pares inseridos: ", num_par)