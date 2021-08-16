#faixa_etaria = [ [], [], [], [], [] ]
faixa_15 =    []
faixa_16_30 = []
faixa_31_45 = []
faixa_46_60 = []
faixa_60 =    []


i = 0

while (i < 15):
    idade = int(input('Insira sua idade: '))
    
    if idade <= 15:
        faixa_15.append(idade)
    elif 16 <= idade <= 30:
        faixa_16_30.append(idade)
    elif 31 <= idade <= 45:
        faixa_31_45.append(idade)
    elif 46 <= idade <= 60:
        faixa_46_60.append(idade)
    elif idade > 60:
        faixa_60.append(idade)
    
    i += 1

print('Faixa etária até 15 anos: {0} \n Quantidade de idades referentes à essa faixa: {1} \n E a porcentagem da quantidade da faixa é: {2} %' .format(faixa_15, len(faixa_15), float(len(faixa_15)/15)))
print('-'*60) 
print('Faixa etária até 15 anos: {0} \n Quantidade de idades referentes à essa faixa: {1} \n E a porcentagem da quantidade da faixa é: {2} %' .format(faixa_16_30, len(faixa_16_30), float(len(faixa_16_30)/15)))
print('-'*60)
print('Faixa etária até 15 anos: {0} \n Quantidade de idades referentes à essa faixa: {1} \n E a porcentagem da quantidade da faixa é: {2} %' .format(faixa_31_45, len(faixa_31_45), float(len(faixa_31_45)/15)))
print('-'*60)
print('Faixa etária até 15 anos: {0} \n Quantidade de idades referentes à essa faixa: {1} \n E a porcentagem da quantidade da faixa é: {2} %' .format(faixa_46_60, len(faixa_46_60), float(len(faixa_46_60)/15)))
print('-'*60)
print('Faixa etária até 15 anos: {0} \n Quantidade de idades referentes à essa faixa: {1} \n E a porcentagem da quantidade da faixa é: {2} %' .format(faixa_60, len(faixa_60), float(len(faixa_60)/15)))
print('-'*60)