from tela.tela_carrinho import TelaCarrinho
from controlador.abstract_controlador import AbstractControlador
from entidade.produto import Produto

class ControladorCarrinho(AbstractControlador):

  def __init__(self, controlador):
    self.__controlador_principal = controlador
    self.__tela_carrinho = TelaCarrinho(self)
    self.__carrinhos = []
    self.__lista_produtos_compra = []
    self.__exibe_tela = True

  def lista(self):
    self.limpa_tela()
    self.__controlador_principal.controlador_produto.lista()
    
  def lista_produtos_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
        self.__tela_carrinho.mostra_produtos_adicionados(produto.codigo, produto.nome, produto.valor,produto.quantidade)

  def adiciona(self):
    existe = False
    dados = self.__tela_carrinho.requisita_dados_adicionar()
    for produto in self.__controlador_principal.controlador_produto.produtos:
      if produto.codigo == dados["codigo"]:
        existe = True
        if dados["quantidade"] <= produto.quantidade:
          produto_novo = Produto(produto.codigo, produto.nome, produto.valor,dados["quantidade"])
          produto.quantidade -= dados["quantidade"]
          self.__lista_produtos_compra.append(produto_novo)   
          break
        else:
          self.__tela_carrinho.quantidade_insuficiente()
    if not existe:
      self.__tela_carrinho.digite_codigo_valido()
      self.adiciona() 

  def remove(self):
    existe = False
    codigo = self.__tela_carrinho.requisita_dado_remover()
    for produto in self.__lista_produtos_compra:
      if produto.codigo == codigo["codigo"]:
        existe = True
        for prod in self.__controlador_principal.controlador_produto.produtos:
          if prod.codigo == produto.codigo:
            prod.quantidade += produto.quantidade
            self.__lista_produtos_compra.remove(produto)
            break
    if not existe:
      self.__tela_carrinho.digite_codigo_valido()
      self.remove()

  def atualiza(self):
    existe = False
    dados = self.__tela_carrinho.requisita_dado_atualizar()
    for produto in self.__lista_produtos_compra:
      if produto.codigo == dados["codigo"]:
        existe = True
        for prod in self.__controlador_principal.controlador_produto.produtos:
          if produto.codigo == prod.codigo:
            if dados["quantidade"] < produto.quantidade:
              prod.quantidade += (produto.quantidade - dados["quantidade"])
              produto.quantidade = dados["quantidade"]
              break
            elif dados["quantidade"] == (prod.quantidade + produto.quantidade):
              prod.quantidade = dados["quantidade"] - (prod.quantidade + produto.quantidade) 
            else:
              self.__tela_carrinho.quantidade_insuficiente()
    if not existe:
      self.__tela_carrinho.digite_codigo_valido()
      self.atualiza()
      
  def limpa_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
      for prod in self.__controlador_principal.controlador_produto.produtos:
        if produto.codigo == prod.codigo:
          prod.quantidade += produto.quantidade
          
    self.__lista_produtos_compra.clear()
    

  def valor_total(self):
    self.limpa_tela()
    total = 0
    for produto in self.__lista_produtos_compra:
      total += produto.valor * produto.quantidade
    self.__tela_carrinho.total_valor_carrinho(total)

  def finaliza_tela(self):
    self.__exibe_tela = False

  def abre_tela_inicial(self):
    opcoes = {1: self.lista,2: self.adiciona,3: self.remove,4: self.atualiza,5: self.limpa_carrinho,6: self.lista_produtos_carrinho, 7: self.valor_total,0: self.finaliza_tela}

    self.__exibe_tela = True
    while self.__exibe_tela:
      opcao = self.__tela_carrinho.mostra_opcoes()
      funcao = opcoes[opcao]
      funcao()
 


  