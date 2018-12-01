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
# Descricao:  PROJETO3 - CLASSE KNAPSACK
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np

class Knapsack:
  '''
  Algoritmo que resolve o problema da mochila.
  Argumentos: <capacidade total>,<vetor de pesos>,<vetor de valores>
  '''
  def __init__(self,cap_total,v_pesos,v_valores):
    self._cap_total = cap_total
    self._v_pesos = v_pesos
    self._v_valores = v_valores
    self._numero_itens = len(self._v_pesos)
    self._matriz_solucoes = np.zeros(((self._numero_itens + 1),(self._cap_total + 1)),dtype = np.int32)
    
  def MaiorValor(self):
    '''
    Algoritmo em programação dinamica que resolve o "Knapsack Problem"
    '''
    for j in range(1,self._numero_itens + 1):
      for w in range(1,self._cap_total + 1):
        if (self._v_pesos[j - 1] <= w):
          if ((self._v_valores[j - 1] + self._matriz_solucoes[j - 1][w - self._v_pesos[j - 1]]) > self._matriz_solucoes[j - 1][w]):
            self._matriz_solucoes[j][w] = self._v_valores[j - 1] + self._matriz_solucoes[j - 1][w - self._v_pesos[j - 1]]
            
          else:
            self._matriz_solucoes[j][w] = self._matriz_solucoes[j - 1][w]

        else:
          self._matriz_solucoes[j][w] = self._matriz_solucoes[j - 1][w]
    return self._matriz_solucoes[self._numero_itens][self._cap_total]

  def Escolhidos(self):
    '''
    Retorna lista de elementos que estao na solucao.
    '''
    self._elemento = self._numero_itens
    self._peso = self._cap_total
    self._v_pesos_e = np.array([0],dtype = np.int32)
    self._v_valores_e = np.array([0],dtype = np.int32)
    self._itens_escolhidos = np.array([],dtype = np.int16)
    self._saida = np.array([],dtype = np.int16)
    for p in self._v_pesos:
      self._v_pesos_e = np.append(self._v_pesos_e,p)
    for v in self._v_valores:
      self._v_valores_e = np.append(self._v_valores_e,v)
    while (self._elemento > 0):
      if (self._matriz_solucoes[self._elemento][self._peso] - self._matriz_solucoes[self._elemento - 1][self._peso - self._v_pesos_e[self._elemento]] == self._v_valores_e[self._elemento]):
        self._itens_escolhidos = np.append(self._itens_escolhidos,self._elemento)
        self._peso = self._peso - self._v_pesos_e[self._elemento]
        self._elemento -= 1
      else:
        self._elemento -= 1
    return self._itens_escolhidos