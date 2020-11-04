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
    for produto in self.__lista_produtos_compra:
        self.__tela_carrinho.mostra_produtos_adicionados(produto.codigo, produto.nome, produto.valor,produto.quantidade)

  def adiciona(self):
    dados = self.__tela_carrinho.requisita_dados_adicionar() 
    for produto in self.__controlador_principal.controlador_produto.produtos:
      if produto.codigo == dados["codigo"]:
        if dados["quantidade"] <= produto.quantidade:
          produto_novo = Produto(produto.codigo, produto.nome, produto.valor,dados["quantidade"])
          self.__lista_produtos_compra.append(produto_novo)    
          break
        else:
          self.__tela_carrinho.quantidade_insuficiente()

  def remove(self):
    codigo = self.__tela_carrinho.requisita_dado_remover()
    for produto in self.__lista_produtos_compra:
      if produto.codigo == codigo["codigo"]:
        self.__lista_produtos_compra.remove(produto)
        break

  def atualiza(self):
    dados = self.__tela_carrinho.requisita_dado_atualizar()
    for produto in self.__lista_produtos_compra:
      if produto.codigo == dados["codigo"]:
        for prod in self.__controlador_principal.controlador_produto.produtos:
          if dados["quantidade"] <= prod.quantidade:
            produto.quantidade = dados["quantidade"]
            break
          else:
            self.__tela_carrinho.quantidade_insuficiente()

  def limpa_carrinho(self):
    self.__lista_produtos_compra.clear()
    
  def finaliza_compra(self):
    self.valor_total()
    for item in self.__carrinhos:
      for produto in self.__controlador_principal.controlador_produto.produtos:
        if item.codigo == produto.codigo:
          produto.quantidade -= item.quantidade
          
  def valor_total(self):
    total = 0
    for produto in self.__lista_produtos_compra:
      valor = produto.valor
      total += valor
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
 


  