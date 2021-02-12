class Entregador (Pessoa):
  
    def __init__(self, conducao, placa, nome, contato, id, estrelas):

        super().__init__(nome, contato, id, estrelas)
        self.conducao = conducao
        self.placa = placa

    def relatar_problema_entrega (self):

        print("PROBLEMA RELATADO COM SUCESSO. AGUARDE O CONTATO DA EMPRESA. MUITO OBRIGADE! ")

    def confirmar_entrega (self):

        print ("ENTREGA CONFIRMADA COM SUCESSO! MUITO OBRIGADE!")

    def avaliar_cliente (self):

        avaliacao_cliente = input (float) "DIGITE A AVALIAÇÃO DO CLIENTE (0.0 A 5.0 ESTRELAS - DIGITAR APENAS NÚMEROS) ")
        print ("CLIENTE AVALIADO COM SUCESSO!")