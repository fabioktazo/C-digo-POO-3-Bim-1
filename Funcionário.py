class Funcionario (Pessoa):

    def __init__ (self, data_admissao, cargo, cpf_funcionario, nome, contato, id, estrelas):

        super().__init__(nome, contato, id, estrelas)
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.cpf_funcionario = cpf_funcionario

    def liberar_pedido (self):

          confirmar = input ("VOCÊ DESEJA CONFIRMAR O(S) PEDIDO(S)?:  ")

          if confirmar == "sim" or "SIM" or "Sim":
          print ("PEDIDO CONFIRMADO! MUITO OBRIGADE!")
          return True
        
          else:
            return False

    def registrar_entrada (self):

        print ("ENTRADA REGISTRADA COM SUCESSO!")

    def registrar_saida (self):

        print ("SAÍDA REGISTRADA COM SUCESSO!")