import requests

url_cotacao  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_cotacao += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_cotacao += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

dict_cotacao = requests.get(url_cotacao, verify=True).json()

print(dict_cotacao)