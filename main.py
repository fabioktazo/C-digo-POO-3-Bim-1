#Avaliação Prática de POO - 3º Bimestre
#Fabio Koiti Tazo
#Giovanna Souza Régias
#Letícia Sophia Rodrigues da Silva
#2º ano Téc. Informática Matutino Integrado 

from Produtos import *
from Cardapio import *
from Cliente import *
from Pessoa import *
import sys
import os  

class Menu:

  
  def __init__(self):
    self.menu = menu=[]
   
  def Exibir_Menu_um(self):
    global cliente
    print("QUERIDE USUÁRIE, POR FAVOR, PREENCHA AS INFORMAÇÕES ABAIXO PARA A REALIZAÇÃO DO SEU CADASTRO.")
    print ("")
    cliente=Cliente(0,0)
    os.system('clear')
    self.Exibir_Menu_dois()
  
  def Exibir_Menu_dois(self):
    print("1-VISUALIZAR PERFIL\n2-VISUALIZAR CARDÁPIO\n3-SAIR DO SISTEMA")
    a = input("DIGITE O NÚMERO CORRENPONDENTE À AÇÃO DESEJADA: ")
    
    if a== "1":
      cliente.abrir_perfil()
      self.Exibir_Menu_dois() 
    
    elif a== "2":
      os.system('clear')
      self.cardapio = Cardapio()
      self.cardapio.exibir_cardapio()
    
    elif a== "3":
      os.system('clear')
      print("SISTEMA ENCERRADO! MUITO OBRIGADE!")
      sys.exit()
    
    else:
      os.system('clear')
      print("ERRO")
      self.Exibir_Menu_dois
  
  

  def Exibir_Menu_tres (self):
    print("1-REALIZAR NOVO PEDIDO\n2-INSTRUÇÕES DE PAGAMENTO E ENTREGA")
    a = input('Digite o número correspondente: ')
    
    if a== '1':
      os.system('clear')
      self.exibir_cardapio() 
    
    elif a== '2':
      os.system('clear')
      self.remover_produto_cardapio()
    
    elif a== '3':
      os.system('clear')
      print('Encerrado')
    
    else:
      os.system('clear')
      print("ERRO")
      self.Exibir_Menu_dois 
  
  def remover_produto_cardapio (self):
    total=0
    
    for x in range(len(self.cardapio)):
      total=total+self.cardapio[x].preco_produto
    
    os.system('clear')
    print("O TOTAL DA SUA COMPRA É: R$", total)
    print ("OBRIGADE POR COMPRAR CONOSCO!")

menu = Menu()
menu.Exibir_Menu_um()
