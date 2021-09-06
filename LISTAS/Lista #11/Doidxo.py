import requests

#Criando listas para armazenar os dados obtidos do dicionário
compra_cotacao = venda_cotacao = data_cotacao = compra_january = venda_january = data_january = compra_february = venda_february = data_february = []
compra_march = venda_march = data_march = compra_april = venda_april = data_april = compra_may = venda_may = data_may = []
compra_june = venda_june = data_june = compra_july = venda_july = data_july = compra_august = venda_august = data_august = []
compra_setember = venda_setember = data_setember = compra_october = venda_october = data_october = []
compra_november = venda_november = data_november = compra_december = venda_december = data_december = []

#Adquirindo o docionário da Cotação geral
url_cotacao  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_cotacao += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_cotacao += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

dict_cotacao = requests.get(url_cotacao, verify=True).json()
cotacao_value = dict_cotacao.get('value')

for i in range(len(cotacao_value)):
    compra_cotacao.append(cotacao_value[i]['cotacaoCompra'])
    venda_cotacao.append(cotacao_value[i]['cotacaoVenda'])
    data_cotacao.append(cotacao_value[i]['dataHoraCotacao'])

url_january  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_january += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_january += '@dataInicial=\'01-01-2020\'&@dataFinalCotacao=\'01-31-2020\'&$format=json'

dict_january = requests.get(url_january, verify=True).json()
cotacao_january = dict_january.get('value')

for i in range(len(cotacao_january)):
    compra_january.append(cotacao_january[i]['cotacaoCompra'])
    venda_january.append(cotacao_january[i]['cotacaoVenda'])
    data_january.append(cotacao_january[i]['dataHoraCotacao'])

url_february  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_february += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_february += '@dataInicial=\'02-01-2020\'&@dataFinalCotacao=\'02-29-2020\'&$format=json'

dict_february = requests.get(url_february, verify=True).json()
cotacao_february = dict_february.get('value')

for i in range(len(cotacao_february)):
    compra_february.append(cotacao_february[i]['cotacaoCompra'])
    venda_february.append(cotacao_february[i]['cotacaoVenda'])
    data_february.append(cotacao_february[i]['dataHoraCotacao'])

url_march  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_march += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_march += '@dataInicial=\'03-01-2020\'&@dataFinalCotacao=\'03-31-2020\'&$format=json'

dict_march = requests.get(url_march, verify=True).json()
cotacao_march = dict_march.get('value')

for i in range(len(cotacao_march)):
    compra_march.append(cotacao_march[i]['cotacaoCompra'])
    venda_march.append(cotacao_march[i]['cotacaoVenda'])
    data_march.append(cotacao_march[i]['dataHoraCotacao'])

url_april  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_april += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_april += '@dataInicial=\'04-01-2020\'&@dataFinalCotacao=\'04-30-2020\'&$format=json'

dict_april = requests.get(url_april, verify=True).json()
cotacao_april = dict_april.get('value')

for i in range(len(cotacao_april)):
    compra_april.append(cotacao_april[i]['cotacaoCompra'])
    venda_april.append(cotacao_april[i]['cotacaoVenda'])
    data_april.append(cotacao_april[i]['dataHoraCotacao'])

url_may  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_may += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_may += '@dataInicial=\'05-01-2020\'&@dataFinalCotacao=\'05-31-2020\'&$format=json'

dict_may = requests.get(url_may, verify=True).json()
cotacao_may = dict_may.get('value')

for i in range(len(cotacao_may)):
    compra_may.append(cotacao_may[i]['cotacaoCompra'])
    venda_may.append(cotacao_may[i]['cotacaoVenda'])
    data_may.append(cotacao_may[i]['dataHoraCotacao'])

url_june  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_june += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_june += '@dataInicial=\'06-01-2020\'&@dataFinalCotacao=\'06-30-2020\'&$format=json'

dict_june = requests.get(url_june, verify=True).json()
cotacao_june = dict_june.get('value')

for i in range(len(cotacao_june)):
    compra_june.append(cotacao_june[i]['cotacaoCompra'])
    venda_june.append(cotacao_june[i]['cotacaoVenda'])
    data_june.append(cotacao_june[i]['dataHoraCotacao'])

url_july  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_july += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_july += '@dataInicial=\'07-01-2020\'&@dataFinalCotacao=\'07-31-2020\'&$format=json'

dict_july = requests.get(url_july, verify=True).json()
cotacao_july = dict_july.get('value')

for i in range(len(cotacao_july)):
    compra_july.append(cotacao_july[i]['cotacaoCompra'])
    venda_july.append(cotacao_july[i]['cotacaoVenda'])
    data_july.append(cotacao_july[i]['dataHoraCotacao'])

url_august  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_august += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_august += '@dataInicial=\'08-01-2020\'&@dataFinalCotacao=\'08-31-2020\'&$format=json'

dict_august = requests.get(url_august, verify=True).json()
cotacao_august = dict_august.get('value')

for i in range(len(cotacao_august)):
    compra_august.append(cotacao_august[i]['cotacaoCompra'])
    venda_august.append(cotacao_august[i]['cotacaoVenda'])
    data_august.append(cotacao_august[i]['dataHoraCotacao'])

url_setember  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_setember += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_setember += '@dataInicial=\'09-01-2020\'&@dataFinalCotacao=\'09-30-2020\'&$format=json'

dict_setember = requests.get(url_setember, verify=True).json()
cotacao_setember = dict_setember.get('value')

for i in range(len(cotacao_setember)):
    compra_setember.append(cotacao_setember[i]['cotacaoCompra'])
    venda_setember.append(cotacao_setember[i]['cotacaoVenda'])
    data_setember.append(cotacao_setember[i]['dataHoraCotacao'])

url_october  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_october += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_october += '@dataInicial=\'10-01-2020\'&@dataFinalCotacao=\'10-31-2020\'&$format=json'

dict_october = requests.get(url_october, verify=True).json()
cotacao_october = dict_october.get('value')

for i in range(len(cotacao_october)):
    compra_october.append(cotacao_october[i]['cotacaoCompra'])
    venda_october.append(cotacao_october[i]['cotacaoVenda'])
    data_october.append(cotacao_october[i]['dataHoraCotacao'])

url_november  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_november += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_november += '@dataInicial=\'11-01-2020\'&@dataFinalCotacao=\'11-30-2020\'&$format=json'

dict_november = requests.get(url_november, verify=True).json()
cotacao_november = dict_november.get('value')

for i in range(len(cotacao_november)):
    compra_november.append(cotacao_november[i]['cotacaoCompra'])
    venda_november.append(cotacao_november[i]['cotacaoVenda'])
    data_november.append(cotacao_november[i]['dataHoraCotacao'])

url_december  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url_december += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url_december += '@dataInicial=\'12-01-2020\'&@dataFinalCotacao=\'12-31-2020\'&$format=json'

dict_december = requests.get(url_december, verify=True).json()
cotacao_december = dict_december.get('value')

for i in range(len(cotacao_december)):
    compra_december.append(cotacao_december[i]['cotacaoCompra'])
    venda_december.append(cotacao_december[i]['cotacaoVenda'])
    data_december.append(cotacao_december[i]['dataHoraCotacao'])

print('Novembro: ', compra_cotacao)