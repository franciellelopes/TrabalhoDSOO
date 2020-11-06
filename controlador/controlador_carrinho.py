from tela.tela_carrinho import TelaCarrinho
from controlador.abstract_controlador import AbstractControlador
from entidade.produto import Produto
from tela.nota_fiscal import NotaFiscal

class ControladorCarrinho(AbstractControlador):

  def __init__(self, controlador):
    self.__controlador_principal = controlador
    self.__tela_carrinho = TelaCarrinho(self)
    self.__lista_produtos_compra = []


  def lista(self):
    self.limpa_tela()
    self.__controlador_principal.controlador_produto.lista()


  def lista_produtos_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
      self.__tela_carrinho.mostra_produtos_adicionados(produto.codigo, produto.nome, produto.valor,produto.quantidade)


  def adiciona(self):
    dados = self.__tela_carrinho.requisita_dados_adicionar()
    verifica = self.verifica_duplicidade(dados)
    if not verifica:
      existe = False
      for produto in self.__controlador_principal.controlador_produto.produtos:
        if produto.codigo == dados["codigo"]:
          existe = True
          if dados["quantidade"] <= produto.quantidade:
            produto_novo = Produto(produto.codigo, produto.nome, produto.valor,dados["quantidade"])
            produto.quantidade -= dados["quantidade"]
            self.__lista_produtos_compra.append(produto_novo)
            self.__tela_carrinho.avisos("produto_adicionado")  
            break
          else:
            self.__tela_carrinho.avisos("quantidade_insuficiente")

        if not existe:
          self.__tela_carrinho.avisos("codigo_invalido")

  def verifica_duplicidade(self, dados):
    existe = False
    duplicidade = False
    for produto in self.__controlador_principal.controlador_produto.produtos:
        if produto.codigo == dados["codigo"]:
          existe = True
          for prod in self.__lista_produtos_compra:
            if prod.codigo == dados["codigo"]:
              duplicidade = True
              if dados["quantidade"] <= produto.quantidade:
                prod.quantidade += dados["quantidade"]
                produto.quantidade -= dados["quantidade"]
                self.__tela_carrinho.avisos("produto_adicionado")  
                return duplicidade
              elif dados["quantidade"] == prod.quantidade + produto.quantidade:
                prod.quantidade += produto.quantidade 
                produto.quantidade = 0
                self.__tela_carrinho.avisos("produto_adicionado")  
                return duplicidade
              else:
                self.__tela_carrinho.avisos("quantidade_insuficiente")

        if not existe:
          self.__tela_carrinho.avisos("codigo_invalido")
    

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
      self.__tela_carrinho.avisos("codigo_invalido")


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
              self.__tela_carrinho.avisos("quantidade_insuficiente")
    if not existe:
      self.__tela_carrinho.avisos("codigo_invalido")


  def limpa_carrinho(self):
    self.limpa_tela()
    for produto in self.__lista_produtos_compra:
      for prod in self.__controlador_principal.controlador_produto.produtos:
        if produto.codigo == prod.codigo:
          prod.quantidade += produto.quantidade
          
    self.__lista_produtos_compra.clear()
    

  def finaliza_compra(self):
    if self.__lista_produtos_compra == []:
      self.__tela_carrinho.avisos("carrinho_vazio")

    else:
      total = 0
      for produto in self.__lista_produtos_compra:
        total += produto.valor * produto.quantidade

      opcao = self.__tela_carrinho.confirma_tela("finaliza_compra", str(total))

      if opcao == 1:
        self.__tela_carrinho.avisos("compra_finalizada")
        nota_fiscal = NotaFiscal(self.__lista_produtos_compra)
        nota_fiscal.relatorio_compras()
        self.__controlador_principal.adiciona_nf_cliente(nota_fiscal)
      elif opcao == 2:
        self.__tela_carrinho.avisos("compra_cancelada")
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
