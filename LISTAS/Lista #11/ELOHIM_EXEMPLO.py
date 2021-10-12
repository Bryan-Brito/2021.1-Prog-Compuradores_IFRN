# Questão 01
#cotação dolar

import requests

url_cotacao  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_cotacao += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_cotacao += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

dict_cotacao = requests.get(url_cotacao, verify=True).json()
print(dict_cotacao)

# O maior valor de compra e de venda do dólar de cada mês (exibir a data e o respectivo valor);
maiorVenda = dict_cotacao['value'][0]
maiorCompra = dict_cotacao['value'][0]
#print(maiorVenda)
#for i in dict_cotacao.items():
n = 0
for i in dict_cotacao['value']:
  teste = dict_cotacao['value'][n]
  if teste['cotacaoVenda'] > maiorVenda['cotacaoVenda']:
    maiorVenda = teste
  if teste['cotacaoCompra'] > maiorCompra['cotacaoCompra']:
    maiorCompra = teste
  n = n+1
#print ('maior venda: '+ maiorVenda['cotacaoVenda'] + " data: " + maiorVenda['dataHoraCotacao'])
print ("maior venda: "+ str(maiorVenda['cotacaoVenda']) + " * data: " + str(maiorVenda['dataHoraCotacao']))
print ("maior compra: "+ str(maiorCompra['cotacaoCompra']) + " * data: " + str(maiorCompra['dataHoraCotacao']))