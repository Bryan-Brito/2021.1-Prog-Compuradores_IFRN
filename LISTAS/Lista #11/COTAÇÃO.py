import requests
import os
import library_dict

os.system('cls')

url_cotacao  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_cotacao += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_cotacao += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

# --------------------------------------------------------------------------------
# Dicionário Completo
dict_cotacao_web = requests.get(url_cotacao, verify=True).json()

# --------------------------------------------------------------------------------
# Apenas a parte do dicionário com as cotações
list_cotacao = dict_cotacao_web['value']

# --------------------------------------------------------------------------------
# Convertendo a lista em dicionário (UDF)
#dict_cotacao = library_dict.list_2_dict(list_cotacao)
#print(dict_cotacao)

# --------------------------------------------------------------------------------
# Retirando o dicionário de cada MÊS
dict_mes = library_dict.variavel_mes(list_cotacao)
print(dict_mes)
print('-'*100)
print(dict_mes['Junho'])
print('-'*100)


# dict_max = library_dict.MAXIMO(dict_mes)
# print('-'*100)
# print(dict_max)
# --------------------------------------------------------------------------------
# QUESTÃO 1.a - TRANSFORMAR EM UDF
for mes in range(1, 13):
   print('A FAZER... Questão 1.a')
   # Filtrar o dicionario DICT_COTACAO pela variável MÊS
   # dict_cotacao_mes = ...
   # Obter o maior valor de compra através do dicionário filtrado (DICT_COTACAO_MES)
   # ...
   # Obter o maior valor de venda através do dicionário filtrado (DICT_COTACAO_MES)
   # ...  

# --------------------------------------------------------------------------------
# QUESTÃO 1.b - TRANSFORMAR EM UDF
print('A FAZER... Questão 1.b')
# Ordenar o dicionário DICT_COTACAO pela chave COTACAOCOMPRA
# dict_cotacao_ordenado = ...
# Obter as 10 primeiras ou 10 últimas posições do dicionário DICT_COTACAO_ORDENADO
# ...
# Ordenar o dicionário DICT_COTACAO pela chave COTACAOVENDA
# dict_cotacao_ordenado = ...
# Obter as 10 primeiras ou 10 últimas posições do dicionário DICT_COTACAO_ORDENADO
# ...

# --------------------------------------------------------------------------------
# QUESTÃO 1.c - TRANSFORMAR EM UDF
for mes in range(1, 13):
   print('A FAZER... Questão 1.c')
   # Filtrar o dicionario DICT_COTACAO pela variável MÊS
   # dict_cotacao_mes = ...
   # Calcular o valor da média de COTACAOCOMPRA do DICT_COTACAO_MES
   # ...
   # Calcular o valor da média de COTACAOVENDA do DICT_COTACAO_MES
   # ...  