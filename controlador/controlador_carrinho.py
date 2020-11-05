from tela.tela_carrinho import TelaCarrinho
from controlador.abstract_controlador import AbstractControlador
from entidade.produto import Produto

class ControladorCarrinho(AbstractControlador):

  def __init__(self, controlador):
    self.__controlador_principal = controlador
    self.__tela_carrinho = TelaCarrinho(self)
    self.__carrinhos = []
    self.__lista_produtos_compra = []


  def lista(self):
    self.limpa_tela()
    self.__controlador_principal.controlador_produto.lista()


  def lista_produtos_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
      self.__tela_carrinho.mostra_produtos_adicionados(produto.codigo, produto.nome, produto.valor,produto.quantidade)


  def adiciona(self):
    existe = False
    produto_dentro_carrinho = False
    dados = self.__tela_carrinho.requisita_dados_adicionar()
    for produto in self.__controlador_principal.controlador_produto.produtos:

      for produto_carrinho in self.__lista_produtos_compra:
        if produto.codigo == produto_carrinho.codigo:
          produto_dentro_carrinho = True
          if produto.quantidade > 0:
            produto_carrinho.quantidade += 1
            produto.quantidade -= 1
            self.__tela_carrinho.avisos("produto_adicionado", "")  
        break


      
      if produto.codigo == dados["codigo"]:
        existe = True
        if dados["quantidade"] <= produto.quantidade and produto_dentro_carrinho == False:
          produto_novo = Produto(produto.codigo, produto.nome, produto.valor,dados["quantidade"])
          produto.quantidade -= dados["quantidade"]
          self.__lista_produtos_compra.append(produto_novo)
          self.__tela_carrinho.avisos("produto_adicionado", "")  
          break
        elif produto.quantidade < 0:
          self.__tela_carrinho.avisos("quantidade_insuficiente", "")

      elif not existe:
        self.__tela_carrinho.digite_codigo_valido()


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


  def limpa_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
      for prod in self.__controlador_principal.controlador_produto.produtos:
        if produto.codigo == prod.codigo:
          prod.quantidade += produto.quantidade
          
    self.__lista_produtos_compra.clear()
    

  def finaliza_compra(self):
    if self.__lista_produtos_compra == []:
      self.__tela_carrinho.avisos("carrinho_vazio", "")

    else:
      total = 0
      for produto in self.__lista_produtos_compra:
        total += produto.valor * produto.quantidade

      opcao = self.__tela_carrinho.confirma_tela("finaliza_compra", str(total))
      #self.__tela_carrinho.total_valor_carrinho(total)
      if opcao == 1:
        self.__tela_carrinho.avisos("compra_finalizada", "")
        self.__controlador_principal.gera_nota_fiscal(self.__lista_produtos_compra)
      elif opcao == 2:
        self.__tela_carrinho.avisos("compra_cancelada", "")
    self.__exibe_tela = False


  def finaliza_tela(self):
    self.limpa_tela()
    self.__exibe_tela = False


  def abre_tela_inicial(self):
    opcoes = {
    1: self.lista,
    2: self.adiciona,
    3: self.remove,
    4: self.atualiza,
    5: self.limpa_carrinho,
    6: self.lista_produtos_carrinho,
    7: self.finaliza_compra,
    0: self.finaliza_tela}

    self.limpa_tela()
    self.__exibe_tela = True
    while self.__exibe_tela:
      opcao = self.__tela_carrinho.mostra_opcoes()
      funcao = opcoes[opcao]
      funcao()
