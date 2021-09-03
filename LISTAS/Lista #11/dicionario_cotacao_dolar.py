import requests

dict_compra = []
dict_venda = []
dict_dataHora = []


url_cotacao  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_cotacao += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_cotacao += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

dict_cotacao = requests.get(url_cotacao, verify=True).json()


dict_value = dict_cotacao.get('value')


for i in range(len(dict_value)):
    dict_compra.append(dict_value[i]['cotacaoCompra'])
    dict_venda.append(dict_value[i]['cotacaoVenda'])
    dict_dataHora.append(dict_value[i]['dataHoraCotacao'])

dict_compra = dict(dict_compra)
dict_venda = dict(dict_venda)
dict_dataHora = dict(dict_dataHora)


dict_dataHora.update('Olá')
    
print('Compra: ', dict_compra)
print('\nVenda:  ', dict_venda)