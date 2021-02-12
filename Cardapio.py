from Produtos import *
from Cliente import *
from Pessoa import *
from main import *
import sys
import os 

class Cardapio:
  def exibir_cardapio (self):
    
    
    #vocês não digitaram self aqui(self.cardapio), então cardápio é uma variável e não um atributo
    #a variável não vao conseguir ser usada fora da função
    cardapio = ["SUSHI TRADICIONAL", "HOSOMAKI", "MAKIZUSHI", "TEMAKI", "URUMAKI", "NIGUIRI", "SASHIMI", "HOT FILADÉLFIA", "TEMPURÁ", "YAKISOBA TRADICIONAL", "YAKISOBA VEGANO", "HARUMAKI", "MOYASHI", "MOCHI", "MANJU"]

    self.cardapio = cardapio
    

    for x in range(len(cardapio)):
      print(x+1,'-',cardapio[x])  
    
    print("16 - ENCERRAR PEDIDOS E PROSSEGUIR")
    a = input("DIGITE O NÚMERO CORRESPONDENTE AO SEU PEDIDO (OBS.: VOCÊ PODERÁ ESCOLHER MAIS DE UM PEDIDO DESDE SELECIONE UM DE CADA VEZ): ")
    
    if a== '1':
      os.system('clear')
      #estão tentando acessar um atributo que não existe :x, vocês não declaram cardápio como um atributo no construtor
      self.cardapio.append(sushi_tradicional)#chamou de cardapio1 pq?
      self.exibir_cardapio() 
    
    elif a== '2':
      os.system('clear')
      self.cardapio.append(hosomaki)
      self.exibir_cardapio()
    
    elif a== '3':
      os.system('clear')
      self.cardapio.append(makizushi)
      self.exibir_cardapio()
    
    elif a== '4':
      os.system('clear')
      self.cardapio.append(temaki)
      self.exibir_cardapio()
    
    elif a== '5':
      os.system('clear')
      self.cardapio.append(urumaki)
      self.exibir_cardapio()
    
    elif a== '6':
      os.system('clear')
      self.cardapio.append(niguiri)
      self.exibir_cardapio()
    
    elif a== '7':
      os.system('clear')
      self.cardapio.append(sashimi)
      self.exibir_cardapio()
    
    elif a== '8':
      os.system('clear')
      self.cardapio.append(hot_filadelfia)
      self.exibir_cardapio()
    
    elif a== '9':
      os.system('clear')
      self.cardapio.append(tempura)
      self.exibir_cardapio()
    
    elif a== '10':
      os.system('clear')
      self.cardapio.append(yakisoba_tradicional)
      self.exibir_cardapio()
    
    elif a== '11':
      os.system('clear')
      self.cardapio.append(yakisoba_vegano)
      self.exibir_cardapio()
    
    elif a== '12':
      os.system('clear')
      self.cardapio.append(harumaki)
      self.exibir_cardapio()
    
    elif a== '13':
      os.system('clear')
      self.cardapio.append(moyashi)
      self.exibir_cardapio()
    
    elif a== '14':
      os.system('clear')
      self.cardapio.append(mochi)
      self.exibir_cardapio()
    
    elif a== '15':
      os.system('clear')
      self.cardapio.append(manju)
      self.exibir_cardapio()
    
    elif a== '16':
      os.system('clear')
      menu = Menu()
      menu.remover_produto_cardapio()

    
    else:
      os.system('clear')
      print("ERRO")
      self.exibir_cardapio() 
  

  global cardapio     