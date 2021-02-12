import os

class Pessoa:

  def __init__ (self, id, estrelas):
    self.nome = input ("DIGITE O SEU NOME COMPLETO: ")
    self.contato = input ("DIGITE O SEU CONTATO: ")
    self.id = id
    self.estrelas = estrelas
  def abrir_perfil (self):
    os.system('clear')
    print ("PERFIL DE: ", self.nome)
    print ("CONTATO: ", self.contato)
  def enviar_mensagem (self):
    mensagem = input ("DIGITE A MENSAGEM A SER ENVIADA: ")
    print = ("MENSSAGEM ENVIADA COM SUCESSO!")