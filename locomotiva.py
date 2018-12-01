###############################################################################
# Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
# Centro de Informatica -- CIn (http://www.cin.ufpe.br)
# Bacharelado em Sistemas de Informacao
# IF969 -- Algoritmos e Estruturas de Dados
#
# Autor:    Bruno Artagoitia Vicente do Nascimento
# Email:    bavn@cin.ufpe.br
# Data:        2018-12-20
#
# Descricao:  PROJETO3 - UTILITARIO LOCOMOTIVA
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

'''
Este utilitario recebe na linha de comando um arquivo texto conforme espscificado e
calcula o valor total possível para a dada locomotiva
'''

import sys
from LOCO import Loco
from KNAPSACK import Knapsack

argumento = sys.argv
arquivo_texto = argumento[1]

dados = Loco(arquivo_texto)

W = dados.cap_total()
w = dados.pesos()
v = dados.valores()

mochila = Knapsack(W,w,v)
maior_valor = float(mochila.MaiorValor())
lista_de_itens = mochila.Escolhidos()
lista_string = []
for n in range(len(lista_de_itens) - 1,-1,-1):
  lista_string.append(str(lista_de_itens[n]))

print("   ##")
print("  ####")
print(" ######              ###########")
print(" ######               #########")
print("  ####                #########")
print("###############################")
print("## RESOLVE CARGAS LOCOMOTIVA ##")
print("###############################")
print("###############################")
print("  #####        ######    ######")
print("   ###          ####      #### ")
print("\n")
print("O maior valor monetario possivel com os itens dados e: R$","%.2f"%maior_valor)
print("Os itens sao:")
for item in lista_string:
  print("Item:",item)
