# --------------------------------------------------------------------------------
# Converte a lista de cotacoes em um dicionário
from os import X_OK


def list_2_dict(lista_valores):
   dict_retorno = {}

   for i in range(len(lista_valores)):
      data   = lista_valores[i]
      data   = data ['dataHoraCotacao'][0:10]
      venda  = data ['cotacaoVenda']
      compra = data ['cotacaoCompra']
      dict_retorno[data] = { 'cotacaoVenda': venda, 'cotacaoCompra': compra}

   return dict_retorno

# --------------------------------------------------------------------------------
# Separando o dicionário por MÊS
def variavel_mes(mes_var):
    dict_mes_jan = []
    dict_mes_fev = []
    dict_mes_mar = []
    dict_mes_abr = []
    dict_mes_mai = []
    dict_mes_jun = []
    dict_mes_jul = []
    dict_mes_ago = []
    dict_mes_set = []
    dict_mes_out = []
    dict_mes_nov = []
    dict_mes_dez = []
    dict_mes     = {}
    for i in range(len(mes_var)):
      linha  = mes_var[i]
      data  =  linha['dataHoraCotacao'][0:10]

      if data[0:7] == '2020-01':
        dict_mes_jan.append(linha) 
      elif  data[0:7] == '2020-02':
        dict_mes_fev.append([linha]) 
      elif  data[0:7] == '2020-03':
        dict_mes_mar.append([linha])     
      elif  data[0:7] == '2020-04':
        dict_mes_abr.append([linha]) 
      elif  data[0:7] == '2020-05':
        dict_mes_mai.append([linha]) 
      elif  data[0:7] == '2020-06':
        dict_mes_jun.append([linha]) 
      elif  data[0:7] == '2020-07':
        dict_mes_jul.append([linha]) 
      elif  data[0:7] == '2020-08':
        dict_mes_ago.append([linha]) 
      elif  data[0:7] == '2020-09':
        dict_mes_set.append([linha]) 
      elif  data[0:7] == '2020-10':
        dict_mes_out.append([linha]) 
      elif  data[0:7] == '2020-11':
        dict_mes_nov.append([linha]) 
      elif  data[0:7] == '2020-12':
        dict_mes_dez.append([linha])

    venda_jan  = dict_mes_jan[0]
    compra_jan = dict_mes_jan
    x = 0
    compra = 0
    venda = 0
    for i in range(len(dict_mes_jan)):
        dict_lista = dict_mes_jan[i]        
        if dict_lista['cotacaoVenda'] > venda_jan['cotacaoVenda']:
            venda_jan = dict_lista
        if dict_lista['cotacaoCompra'] > compra_jan[i]['cotacaoCompra']:
            compra = dict_lista
        x = x + 1
        print('Compra: ', compra)
        print('Venda: ', venda)
    
    dict_jan = [compra, venda_jan]
      
#    dict_mes.update({'Janeiro': dict_mes_jan})
#    dict_mes.update({'Fevereiro': dict_mes_fev})
#    dict_mes.update({'Março': dict_mes_mar})
#    dict_mes.update({'Abril': dict_mes_abr})
#    dict_mes.update({'Maio': dict_mes_mai})
#    dict_mes.update({'Junho': dict_mes_jun})
#    dict_mes.update({'Julho': dict_mes_jul})
#    dict_mes.update({'Agosto': dict_mes_ago})
#    dict_mes.update({'Setembro': dict_mes_set})
#    dict_mes.update({'Outubro': dict_mes_out})
#    dict_mes.update({'Novembro': dict_mes_nov})
#    dict_mes.update({'Dezembro': dict_mes_dez})
   
    return dict_jan

# # --------------------------------------------------------------------------------
# # Adicionando uma função MAX à biblioteca

# def MAXIMO(dict_ex):
#    dict_max = {}
#    lista_ex = {}
#    lista_ex = dict_ex
#    lista_compra = {}
#    lista_venda = {}
#    compra = []
#    venda = []
#    janeiro_compra  = []
#    janeiro_venda   = []
#    fevereiro_compra= []
#    fevereiro_venda = []
#    marco_compra    = []
#    marco_venda     = []
#    abril_compra    = []
#    abril_venda     = [] 
#    maio_compra     = []
#    maio_venda      = []
#    junho_compra    = []
#    junho_venda     = []
#    julho_compra    = []
#    julho_venda     = []
#    agosto_compra   = []
#    agosto_venda    = []
#    setembro_compra = []
#    setembro_venda  = []
#    outubro_compra  = []
#    outubro_venda   = []
#    novembro_compra = []
#    novembro_venda  = []
#    dezembro_compra = []
#    dezembro_venda  = []
#    for i in range(len(lista_ex)):
#       dict_lista = lista_ex[i]
#       data       = lista_ex[i]['dataHoraCotacao']
#       compra     = dict_lista['cotacaoCompra']
#       venda      = dict_lista['cotacaoVenda']
     
#       if data[0:7] == '2020-01':
#          janeiro_compra.append([data, compra])
#          janeiro_venda.append([data, venda])
#       elif data[0:7] == '2020-02':
#          fevereiro_compra.append([data, compra])
#          fevereiro_venda.append([data, venda])
#       elif data[0:7] == '2020-03':
#          marco_compra.append([data, compra])
#          marco_venda.append([data, venda])
#       elif data[0:7] == '2020-04':
#          abril_compra.append([data, compra])
#          abril_venda.append([data, venda])
#       elif data[0:7] == '2020-05':
#          maio_compra.append([data, compra])
#          maio_venda.append([data, venda])
#       elif data[0:7] == '2020-06':
#          junho_compra.append([data, compra])
#          junho_venda.append([data, venda]) 
#       elif data[0:7] == '2020-07':
#          julho_compra.append([data, compra])
#          julho_venda.append([data, venda]) 
#       elif data[0:7] == '2020-08':
#          agosto_compra.append([data, compra])
#          agosto_venda.append([data, venda])
#       elif data[0:7] == '2020-09':
#          setembro_compra.append([data, compra])
#          setembro_venda.append([data, venda])
#       elif data[0:7] == '2020-10':
#          outubro_compra.append([data, compra])
#          outubro_venda.append([data, venda])
#       elif data[0:7] == '2020-11':
#          novembro_compra.append([data, compra])
#          novembro_venda.append([data, venda])
#       elif data[0:7] == '2020-12':
#          dezembro_compra.append([data, compra])
#          dezembro_venda.append([data, venda])
#       compra = 0
#       venda = 0

#    janeiro_compra_max   = max(janeiro_compra)
#    janeiro_venda_max    = max(janeiro_venda)
#    fevereiro_compra_max = max(fevereiro_compra)
#    fevereiro_venda_max  = max(fevereiro_venda)
#    marco_compra_max     = max(marco_compra)
#    marco_venda_max      = max(marco_venda)
#    abril_compra_max     = max(abril_compra)
#    abril_venda_max      = max(abril_venda)
#    maio_compra_max      = max(maio_compra)
#    maio_venda_max       = max(maio_venda)
#    junho_compra_max     = max(junho_compra)
#    junho_venda_max      = max(junho_venda)
#    julho_compra_max     = max(julho_compra)
#    julho_venda_max      = max(julho_venda)
#    agosto_compra_max    = max(agosto_compra)
#    agosto_venda_max     = max(agosto_venda)
#    setembro_compra_max  = max(setembro_compra)
#    setembro_venda_max   = max(setembro_venda)
#    outubro_compra_max   = max(outubro_compra)
#    outubro_venda_max    = max(outubro_venda)
#    novembro_compra_max  = max(novembro_compra)
#    novembro_venda_max   = max(novembro_venda)
#    dezembro_compra_max  = max(dezembro_compra)
#    dezembro_venda_max   = max(dezembro_venda)

#    lista_compra.update(janeiro_compra_max)
#    lista_venda.update(janeiro_venda_max)
#    lista_compra.update(fevereiro_compra_max)
#    lista_venda.update(fevereiro_venda_max)
#    lista_compra.update(marco_compra_max)
#    lista_venda.update(marco_venda_max)
#    lista_compra.update(abril_compra_max)
#    lista_venda.update(abril_venda_max)
#    lista_compra.update(maio_compra_max)
#    lista_venda.update(maio_venda_max)
#    lista_compra.update(junho_compra_max)
#    lista_venda.update(junho_venda_max)
#    lista_compra.update(julho_compra_max)
#    lista_venda.update(julho_venda_max)
#    lista_compra.update(agosto_compra_max)
#    lista_venda.update(agosto_venda_max)
#    lista_compra.update(setembro_compra_max)
#    lista_venda.update(setembro_venda_max)
#    lista_compra.update(outubro_compra_max)
#    lista_venda.update(outubro_venda_max)
#    lista_compra.update(novembro_compra_max)
#    lista_venda.update(novembro_venda_max)
#    lista_compra.update(dezembro_compra_max)
#    lista_venda.update(dezembro_venda_max)

#    dict_max.update({'Valores máximos de COMPRA': lista_compra})
#    dict_max.update({'Valores máximos de VENDA': lista_venda})

   
#    return dict_max