from tela.tela_carrinho import TelaCarrinho
from controlador.controlador_produto import ControladorProduto
from controlador.abstract_controlador import AbstractControlador
class ControladorCarrinho(AbstractControlador):

  def __init__(self):
    self.__tela_carrinho = TelaCarrinho(self)
    self.__carrinhos = []
    self.__exibindo_tela = True
    self.__controlador_produto = ControladorProduto(self)
    
  def inicia (self):
    self.abre_tela_inicial()

  def lista(self):
    self.__controlador_produto.lista()

  def lista_produtos_carrinho(self):
    for carrinho in self.__carrinhos:
      self.__tela_carrinho.__mostra_produtos_adicionados(carrinho.codigo, carrinho.nome, carrinho.valor, carrinho.quantidade)

  def adiciona(self):
    codigo = self.__tela_carrinho.requisita_dado_adicionar() 
    for produto in self.__produtos:
      if produto.codigo == codigo:
        self.__carrinhos.append(produto)

  def remove(self):
    codigo = self.__tela_carrinho.requisita_dado_remover()
    for produto in self.__carrinhos:
      if produto.codigo == codigo:
        produto_remover = (produto)
        self.__carrinhos.remove(produto_remover)
        break

  def atualiza(self):
    dados = self.__tela_carrinho.requisita_dado_atualizar()
    for produto in self.__carrinhos:
      if produto.codigo == dados.codigo:
        produto.quantidade = dados["quantidade"]

  def limpar_carrinho(self):
    for produto in self.__carrinhos:
      self.__carrinhos.remove(produto)
    
  def valor_total(self):
    total = 0
    for produto in self.__carrinhos:
      valor = produto.valor
      total += valor
    self.__tela_carrinho.total_valor_carrinho(total)

  def finaliza_tela(self):
    self.__exibindo_tela = False

  def abre_tela_inicial(self):
    opcoes = {1: self.lista,2: self.adiciona,3: self.remove,4: self.atualiza,5: self.limpa_carrinho,6: self.lista_produtos_carrinho, 7: self.valor_total,0: self.finaliza_tela}

    while self.__exibindo_tela:
      opcao = self.__tela_carrinho.mostra_opcoes()
      funcao = opcoes[opcao]
      funcao()
 


  