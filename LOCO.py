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
# Descricao:  PROJETO3 - CLASSE LOCOMOTIVA
#
# Licenca: Copyright(c) 2018 Bruno Artagoitia Vicente do Nascimento
#
###############################################################################

import numpy as np

class Loco:
  '''
  Transforma o arquivo texto com a capacidade total + pesos e valores dos itens
  em dados coletados
  '''
  def __init__(self,arquivo):
    self._arquivo = arquivo
    self._dados = open(self._arquivo,"r")
    self._arquivo_dados = self._dados.read()
    self._pesos = np.array([],dtype = np.int32)
    self._valores = np.array([],dtype = np.int32)
    self._strings = np.array([])
    self._string_base = ""
    for s in self._arquivo_dados:
      if (s == "\n") or (s == ","):
        self._strings = np.append(self._strings,self._string_base)
        self._string_base = ""
      else:
        self._string_base += s
        
    self._cap_total = int(self._strings[0])
    self._strings[0] = "x"
    self._w = True
    for num in self._strings:
      if (num != "x"):
        if (self._w == True):
          self._pesos = np.append(self._pesos,int(num))
          self._w = False
        else:
          self._valores = np.append(self._valores,int(num))
          self._w = True
    
  def cap_total(self):
    '''
    Capacidade total
    '''
    return self._cap_total

  def pesos(self):
    '''
    Vetor de pesos
    '''
    return self._pesos

  def valores(self):
    '''
    Vetor de valores
    '''
    return self._valores
