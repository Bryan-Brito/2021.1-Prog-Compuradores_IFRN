n = float(input())
notas = int(n)
moedas = float(n-notas)

n100 = notas//100
notas = notas%100
n50 = notas//50
notas = notas%50
n20 = notas//20
notas = notas%20
n10 = notas//10
notas = notas%10
n5 = notas//5
notas = notas%5
n2 = notas//2
notas = notas%2

m1 = moedas//1
moedas = moedas%1
m50 = moedas//0.5
moedas = moedas%0.5
m25 = moedas//0.25
moedas = moedas%0.25
m10 = moedas//0.1
moedas = moedas%0.1
m05 = moedas//0.05
moedas = moedas%0.05
m01 = moedas // 0.01


print("NOTAS:")
print(n100, "nota(s) de R$ 100.00")
print(n50, "nota(s) de R$ 50.00")
print(n20, "nota(s) de R$ 20.00")
print(n10, "nota(s) de R$ 10.00")
print(n5, "nota(s) de R$ 5.00")
print(n2, "nota(s) de R$ 2.00")

print("MOEDAS:")
print(m1, "Moeda(s) de R$ 1,00")
print(m50, "Moeda(s) de R$ 0,50")
print(m25, "Moeda(s) de R$ 0,25")
print(m10, "Moeda(s) de R$ 0,10")
print(m05, "Moeda(s) de R$ 0,05")
print(m01, "Moeda(s) de R$ 0,01")