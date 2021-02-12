from Cardapio import *
from Endereco import *

class Carrinho:

    def __init__(self):

        self.id_venda = id_venda
        self.cardapio = Cardapio()
        self.endereco_entrega = Endereco()
 
    def remover_produto (self):

        produto = None

    def cancelar_pedido (self):

        print ("PEDIDO CANCELADO COM SUCESSO!")
    
    def confirmar_pedido (self):

        confirmacao = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?  ")
        
        if confirmacao = "sim" or "SIM" or "Sim":
          print ("PEDIDO CONFIRMADO! MUITO OBRIAGADE!")
          return True

        else:
          return False