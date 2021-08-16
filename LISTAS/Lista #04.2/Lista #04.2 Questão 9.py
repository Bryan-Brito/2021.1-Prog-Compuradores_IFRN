salario = float(input("Insira seu salário bruto"))

if salario <= 1100:
    INSS = salario*(7.5/100)
    print("INSS pago: R$0,00")
elif 1100.01 <= salario <= 2203.48:
    INSS = salario - 16.500
    print("INSS pago: R$16,50")
elif 2203.49 <= salario <= 3305.22:
    INSS = salario - 82.604
    print("INSS pago: R$82.60")
elif 3305.23 <= salario <= 6433.57:
    INSS = salario - 148.708
    print("INSS pago: R$148.71")

if INSS <= 1903.98:
    print("Imposto de renda:", INSS)
elif 1903.99 <= INSS <= 2826.65:
    print("Imposto de renda:", INSS - 142.80)
elif 2826.66 <= INSS <= 3752.05:
    print("Imposto de renda:", INSS - 354.80)
elif 3751.06 <= INSS <= 4664.68:
    print("Imposto de renda:", INSS - 636.13)
elif INSS > 4664.68:
    print("Imposto de renda:", INSS - 869.36) 