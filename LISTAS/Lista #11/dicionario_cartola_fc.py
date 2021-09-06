import requests

url_cartola = 'https://api.cartolafc.globo.com/atletas/mercado'

dict_cartola = requests.get(url_cartola, verify=True).json()