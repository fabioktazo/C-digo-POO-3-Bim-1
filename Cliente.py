from Pessoa import*
from Endereco import*

class Cliente (Pessoa):
  
  def __init__(self, id, estrelas):

      super().__init__(id, estrelas)
      self.cpf = input ("DIGITE O SEU CPF: ")
      self.endereco = Endereco()
      self.forma_pagamento = 0 
  
  def cancelar_pedido (self):

      print ("SEU PEDIDO FOI CANCELADO COM SUCESSO!")
  
  def confirmar_pedido (self):

      resposta = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?  ")
        
      if confirmar == "sim" or "SIM" or "Sim":
        
          print ("PEDIDO CONFIRMADO! MUITO OBRIGADE!")
          return True
        
      else:
          return False
  
  def informar_atraso (self):
      print ("ALERTA DE ATRASO ENVIADO COM SUCESSO!")
  
  def avaliar_entregador (self):
    avaliacao_entregador = input (float ("DIGITE A AVALIAÇÃO DO ENTREGADOR (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) "))
    return avaliacao_entregador
  
  def avaliar_restaurante (self):
    avaliacao_restaurante = input (float ("DIGITE A AVALIAÇÃO DO RESTAURANTE (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) "))
    return avaliacao_restaurante