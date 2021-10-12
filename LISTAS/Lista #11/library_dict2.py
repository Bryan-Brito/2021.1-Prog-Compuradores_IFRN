# --------------------------------------------------------------------------------
# Converte a lista de cotacoes em um dicionário
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
   janeiro   = []
   fevereiro = []
   marco     = []
   abril     = []
   maio      = []
   junho     = []
   julho     = []
   agosto    = []
   setembro  = []
   outubro   = []
   novembro  = []
   dezembro  = []
   dict_mes     = {}
   for i in range(len(mes_var)):
      dict_lista = mes_var[i]
      data       = dict_lista['dataHoraCotacao']

      if data[0:7] == '2020-01':
         janeiro.append([dict_lista])
      elif  data[0:7] == '2020-02':
         fevereiro.append([dict_lista])
      elif  data[0:7] == '2020-03':
         marco.append([dict_lista])
      elif  data[0:7] == '2020-04':
         abril.append([dict_lista])
      elif  data[0:7] == '2020-05':
         maio.append([dict_lista])
      elif  data[0:7] == '2020-06':
         junho.append([dict_lista])
      elif  data[0:7] == '2020-07':
         julho.append([dict_lista])
      elif  data[0:7] == '2020-08':
         agosto.append([dict_lista])
      elif  data[0:7] == '2020-09':
         setembro.append([dict_lista])
      elif  data[0:7] == '2020-10':
         outubro.append([dict_lista])
      elif  data[0:7] == '2020-11':
         novembro.append([dict_lista])
      elif  data[0:7] == '2020-12':
         dezembro.append([dict_lista])
      
   dict_mes.update({'Janeiro': janeiro})
   dict_mes.update({'Fevereiro': fevereiro})
   dict_mes.update({'Março': marco})
   dict_mes.update({'Abril': abril})
   dict_mes.update({'Maio': maio})
   dict_mes.update({'Junho': junho})
   dict_mes.update({'Julho': julho})
   dict_mes.update({'Agosto': agosto})
   dict_mes.update({'Setembro': setembro})
   dict_mes.update({'Outubro': outubro})
   dict_mes.update({'Novembro': novembro})
   dict_mes.update({'Dezembro': dezembro})
   
   return dict_mes

# --------------------------------------------------------------------------------
# Adicionando uma função MAX à biblioteca

def MAXIMO(dict_ex):
   dict_max = {}
   lista_ex = {}
   lista_ex = dict_ex
   lista_compra = {}
   lista_venda = {}
   compra = []
   venda = []
   janeiro_compra  = dict_ex
   janeiro_venda   = dict_ex
   fevereiro_compra= dict_ex
   fevereiro_venda = dict_ex
   marco_compra    = dict_ex
   marco_venda     = dict_ex
   abril_compra    = dict_ex
   abril_venda     = dict_ex 
   maio_compra     = dict_ex
   maio_venda      = dict_ex
   junho_compra    = dict_ex
   junho_venda     = dict_ex
   julho_compra    = dict_ex
   julho_venda     = dict_ex
   agosto_compra   = dict_ex
   agosto_venda    = dict_ex
   setembro_compra = dict_ex
   setembro_venda  = dict_ex
   outubro_compra  = dict_ex
   outubro_venda   = dict_ex
   novembro_compra = dict_ex
   novembro_venda  = dict_ex
   dezembro_compra = dict_ex
   dezembro_venda  = dict_ex
   x               = 0
   for i in dict_ex['Janeiro']:
      dict_lista = dict_ex['Janeiro'][0][0]     
      if dict_lista['cotacaoVenda'] > janeiro_venda['Janeiro'][0][0]['cotacaoVenda']:
         janeiro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > janeiro_compra['Janeiro'][0][0]['cotacaoCompra']:
         janeiro_buy = dict_lista
      x = x + 1
   
   x = 0
   for i in lista_ex['Fevereiro']:
      dict_lista = lista_ex['Fevereiro'][0][0]     
      if dict_lista['cotacaoVenda'] > fevereiro_venda['Fevereiro'][0][0]['cotacaoVenda']:
         fevereiro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > fevereiro_compra['Fevereiro'][0][0]['cotacaoCompra']:
         fevereiro_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Março']:
      dict_lista = lista_ex['Março'][0][0]     
      if dict_lista['cotacaoVenda'] > marco_venda['Março'][0][0]['cotacaoVenda']:
         marco_sell = dict_lista
      if dict_lista['cotacaoCompra'] > marco_compra['Março'][0][0]['cotacaoCompra']:
         marco_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Abril']:
      dict_lista = lista_ex['Abril'][0][0]    
      if dict_lista['cotacaoVenda'] > abril_venda['Abril'][0][0]['cotacaoVenda']:
         abril_sell = dict_lista
      if dict_lista['cotacaoCompra'] > abril_compra['Abril'][0][0]['cotacaoCompra']:
         abril_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Maio']:
      dict_lista = lista_ex['Maio'][0][0]     
      if dict_lista['cotacaoVenda'] > maio_venda['Maio'][0][0]['cotacaoVenda']:
         maio_sell = dict_lista
      if dict_lista['cotacaoCompra'] > maio_compra['Maio'][0][0]['cotacaoCompra']:
         maio_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Junho']:
      dict_lista = lista_ex['Junho'][0][0]  
      if dict_lista['cotacaoVenda'] > junho_venda['Junho'][0][0]['cotacaoVenda']:
         junho_sell = dict_lista
      if dict_lista['cotacaoCompra'] > junho_compra['Junho'][0][0]['cotacaoCompra']:
         junho_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Julho']:
      dict_lista = lista_ex['Julho'][0][0]    
      if dict_lista['cotacaoVenda'] > julho_venda['Julho'][0][0]['cotacaoVenda']:
         julho_sell = dict_lista
      if dict_lista['cotacaoCompra'] > julho_compra['Julho'][0][0]['cotacaoCompra']:
         julho_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Agosto']:
      dict_lista = lista_ex['Agosto'][0][0]    
      if dict_lista['cotacaoVenda'] > agosto_venda['Agosto'][0][0]['cotacaoVenda']:
         agosto_sell = dict_lista
      if dict_lista['cotacaoCompra'] > agosto_compra['Agosto'][0][0]['cotacaoCompra']:
         agosto_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Setembro']:
      dict_lista = lista_ex['Setembro'][0][0]    
      if dict_lista['cotacaoVenda'] > setembro_venda['Setembro'][0][0]['cotacaoVenda']:
         setembro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > setembro_compra['Setembro'][0][0]['cotacaoCompra']:
         setembro_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Outubro']:
      dict_lista = lista_ex['Outubro'][0][0]    
      if dict_lista['cotacaoVenda'] > outubro_venda['Outubro'][0][0]['cotacaoVenda']:
         outubro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > outubro_compra['Outubro'][0][0]['cotacaoCompra']:
         outubro_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Novembro']:
      dict_lista = lista_ex['Novembro'][0][0]     
      if dict_lista['cotacaoVenda'] > novembro_venda['Novembro'][0][0]['cotacaoVenda']:
         novembro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > novembro_compra['Novembro'][0][0]['cotacaoCompra']:
         novembro_buy = dict_lista
      x = x + 1

   x = 0
   for i in lista_ex['Dezembro']:
      dict_lista = lista_ex['Dezembro'][0][0]     
      if dict_lista['cotacaoVenda'] > dezembro_venda['Dezembro'][0][0]['cotacaoVenda']:
         dezembro_sell = dict_lista
      if dict_lista['cotacaoCompra'] > dezembro_compra['Dezembro'][0][0]['cotacaoCompra']:
         dezembro_buy = dict_lista
      x = x + 1


   lista_compra.update({'Janeiro': janeiro_buy})
   lista_venda.update({'Janeiro': janeiro_sell})
   lista_compra.update({'Fevereiro': fevereiro_buy})
   lista_venda.update({'Fevereiro': fevereiro_sell})
   lista_compra.update({'Março': marco_buy})
   lista_venda.update({'março': marco_sell})
   lista_compra.update({'Abril': abril_buy})
   lista_venda.update({'Abril': abril_sell})
   lista_compra.update({'Maio': maio_buy})
   lista_venda.update({'Maio': maio_sell})
   lista_compra.update({'Junho': junho_buy})
   lista_venda.update({'Junho': junho_sell})
   lista_compra.update({'Julho': julho_buy})
   lista_venda.update({'Julho': julho_sell})
   lista_compra.update({'Agosto': agosto_buy})
   lista_venda.update({'Agosto': agosto_sell})
   lista_compra.update({'Setembro': setembro_buy})
   lista_venda.update({'Setembro': setembro_sell})
   lista_compra.update({'Outubro': outubro_buy})
   lista_venda.update({'Outubro': outubro_sell})
   lista_compra.update({'Novembro': novembro_buy})
   lista_venda.update({'Novembro': novembro_sell})
   lista_compra.update({'Dezembro': dezembro_buy})
   lista_venda.update({'Dezembro': dezembro_sell})

   dict_max.update({'Valores máximos de COMPRA': lista_compra})
   dict_max.update({'Valores máximos de VENDA': lista_venda})

   return dict_max