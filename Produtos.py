class Produtos:

    def __init__ (self, preco_produto, id_produto, tipo_ProdutoSalgado):

        self.preco_produto = preco_produto
        self.id_produto = id_produto
        self.tipo_ProdutoSalgado = True

    def cadastrar_produto (self):

        produto = input ("DIGITE O NOME DO PRODUTO A SER CADASTRADO: ")
        print ("PRODUTO CADASTRADO COM SUCESSO!")

    def alterar_produto (self):

        self.produto = input ("DIGITE O NOVO PRODUTO: ")
        print ("PRODUTO ALTERADO COM SUCESSO!")

    def adicionar_produto_estoque (self):

        produto_estoque = input ("DIGITE O NOME DO PRODUTO A SER ADICIONADO NO ESTOQUE: ")
        print ("PRODUTO ADICIONADO COM SUCESSO!")
    
    def remover_produto_estoque (self):

        produto_estoque = None

sushi_tradicional = Produtos(3.00,1,True)
hosomaki = Produtos(3.00,2,True)
makizushi = Produtos(3.50,3,True)
temaki = Produtos(5.00,4,True)
urumaki = Produtos(3.50, 5, True)
niguiri = Produtos(8.00, 6, True)
sashimi = Produtos(5.00,7, True)
hot_filadelfia = Produtos(4.00,8, True)
tempura = Produtos( 5.00, 9, True)
yakisoba_tradicional = Produtos(47.90, 10, True)
yakisoba_vegano = Produtos(48.00,11, True)
harumaki = Produtos(10.00, 12, True)
moyashi = Produtos (20.00, 13, True)
mochi = Produtos (5.00, 14, False)
manju =Produtos(6.00, 15, False)