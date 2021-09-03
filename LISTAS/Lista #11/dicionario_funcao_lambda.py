# --------------------------------------------------------------------------------
# Exemplos de usos 'avançados' de funções para tratamento de dados
# Criado por..: Galileu Batista (2019)
# Alterado por: Charles Freitas (2021) 
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# Importando as bibliotecas necessárias
import requests
import functools

# --------------------------------------------------------------------------------
# Criando um dicionário com os dados do mercado do Cartola FC fazendo uma 
# requisição a API do Cartola FC
url_cartola  = 'https://api.cartolafc.globo.com/atletas/mercado'
dict_cartola = requests.get(url_cartola, verify=True).json()


# --------------------------------------------------------------------------------
# Exibindo as chaves (keys) do dicionário 
#keys_cartola = dict_cartola.keys()
#print('-'*80)
#print(keys_cartola)
#print('-'*80)

# --------------------------------------------------------------------------------
# Cria dicionários a partir do dicionário dict_cartola
dict_atletas  = dict_cartola['atletas']
dict_clubes   = dict_cartola['clubes']
dict_posicoes = dict_cartola['posicoes']
dict_status   = dict_cartola['status']


# --------------------------------------------------------------------------------
# EXEMPLO #01
# Obtendo o maior pontuador do Cartola FC
maiorPontuador  = max(dict_atletas, key=lambda a: a['jogos_num'] * a['media_num'])
str_textomodelo = 'O maior pontuado do cartola é {0}, com {1} pontos'
str_nome        = maiorPontuador.get('apelido')
int_pontos      = maiorPontuador.get('jogos_num') * maiorPontuador.get('media_num')
print('\nEXEMPLO #01')
print(str_textomodelo.format(str_nome, int_pontos))
print('-'*80)


# --------------------------------------------------------------------------------
# EXEMPLO #02
# Exibindo os 3 maiores pontuadores do Cartola FC
# Usa sorted para classificar o conjunto, tendo por base a pontuação em ordem 
# descrente. Depois escolhe os três primeiros.
maioresPontuadores = sorted(dict_atletas,
                            key=lambda a: a['jogos_num'] * a['media_num'],
                            reverse=True)[0:3]

print('\nEXEMPLO #02')
print ('Os maiores pontuadores são: \n {0}'.format(maioresPontuadores))
print('-'*80)


# --------------------------------------------------------------------------------
# EXEMPLO #03
# Exibindo os três maiores pontuadores do cartola - apenas os apelidos e pontos
# Usa MAP() para mapear cada um dos elementos da lista de maiores pontuadores.
# De cada dicionario do atleta, extrai somente o apelido e a pontuacao.
maioresPontApelidos = tuple(map(lambda a: a['apelido'] + " -> " +
                                         str(a['jogos_num'] * a['media_num']),
                               maioresPontuadores))
print('\nEXEMPLO #03')
print ('Os maiores pontuadores são: {0}'.format(maioresPontApelidos))
print('-'*80)


# --------------------------------------------------------------------------------
# EXEMPLO #04
# Quais os atletas de um determinado time
# Usa FILTER() para obter o ID do time, no dicionário de clubes
# Usa FILTER() na lista de atletas, para filtar somente os com id do time
# Usa MAP() para obter somente o apelido
str_nomeClube = 'Flamengo'.upper()
int_idClube   = tuple(filter(lambda c: c['nome'].upper() == str_nomeClube, dict_clubes.values()))[0]['id']
atletasClube  = tuple(filter(lambda a: a['clube_id'] == int_idClube, dict_atletas))
atletasClubeApelidos = list(map(lambda a: a['apelido'], atletasClube))
print('\nEXEMPLO #04')
print('O id do {0} é {1}'.format(str_nomeClube, int_idClube))
print('Os Atletas do {0}: {1}'.format(str_nomeClube, atletasClubeApelidos))
print('-'*80)


# --------------------------------------------------------------------------------
# EXEMPLO #05
# Obtendo a pontuação total de um time.... (soma dos pontos dos seus atletas)
# Usa REDUCE() para somar o total de pontos dos atletas. Lembrar que a primeira
# chamada a REDUCE() recebe os primeiro dois elementos da sequencia; a partir de
# entao, recebe o resultado parcial e o elemento seguinte.
# Uma alternativa para evitar o if na funcao seria mapear a tupla de atletas
# numa tupla com os seus pontos.
totalPontosClube = functools.reduce(lambda total, a: (a['jogos_num'] * a['media_num']) +
                                                  (total if type(total) != dict else
                                                   total['jogos_num'] * total['media_num']),
                                    atletasClube)
print('\nEXEMPLO #05')
print('Os jogadores do {0} já fizeram {1} pontos!!!'.format(str_nomeClube, totalPontosClube))
print('-'*80)