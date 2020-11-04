from tela.tela_produto import TelaProduto
from entidade.produto import Produto
from controlador.abstract_controlador import AbstractControlador
class ControladorProduto(AbstractControlador):

  def __init__(self):
    self.__produtos = []
    self.__tela_produto = TelaProduto(self)
    self.__exibe_tela = True
    self.__estoque = []
    self.base_dados_produto()

  
  @property
  def produtos (self):
    return self.__produtos

  def adiciona(self):
    dados = self.__tela_produto.requisita_dados_cadastro()
    novo_produto = Produto(dados["codigo"],dados["nome"],dados["valor"],dados["quantidade"])
    self.__produtos.append(novo_produto)
    self.__estoque.append(novo_produto)


  def remove(self):
    codigo = self.__tela_produto.requisita_dado_remover()
    for produto in self.__produtos:
      if produto.codigo == codigo:
        produto_remover = (produto)
        self.__produtos.remove(produto_remover)
        break


  def atualiza(self):
    codigo = self.__tela_produto.requisita_dado_atualizar()
    for produto in self.__produtos:
      if produto.codigo == codigo: 
        dados = self.__tela_produto.atualiza_produto()
        produto.nome = dados["nome"]
        produto.valor = dados["valor"]
        produto.quantidade = dados["quantidade"]
        self.__estoque.append(produto)
        break


  def lista(self):
    for produto in self.__produtos:
      self.__tela_produto.mostra_dados_cadastrados(produto.codigo,produto.nome, produto.valor, produto.quantidade)


  def abre_tela_inicial(self):
    opcoes = {1: self.adiciona,2: self.remove,3: self.atualiza,4: self.lista,5: self.imprime_relatorio,0: self.finaliza_tela}
    
    self.limpa_tela()
    self.__exibe_tela = True
    while self.__exibe_tela:
      opcao = self.__tela_produto.mostra_opcoes()
      funcao = opcoes[opcao]
      funcao()
 

  def finaliza_tela(self):
    self.limpa_tela()
    self.__exibe_tela = False


  def atualiza_estoque(self):
    pass
    

  def imprime_relatorio(self):
    self.__tela_produto.imprime_estoque()
    for produto in self.__estoque:
      self.__tela_produto.mostra_dados_cadastrados(produto.codigo,produto.nome, produto.valor, produto.quantidade)
  

  def base_dados_produto(self):
    produto = Produto(123, "Carrinho", 50, 3)
    self.__produtos.append(produto)

    produto = Produto(456, "Boneca", 30, 5)
    self.__produtos.append(produto)