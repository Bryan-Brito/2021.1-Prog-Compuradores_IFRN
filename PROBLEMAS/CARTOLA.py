import requests
import json

strURL = 'https://api.cartolafc.globo.com/atletas/mercado'

dic_cartola = requests.get(strURL, verify=True).json()


print(dic_cartola)

print(dic_cartola)
