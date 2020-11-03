from entidade.produto import Produto
from entidade.carrinho import Carrinho
from tela.abstract_tela import AbstractTela

class TelaCarrinho(AbstractTela):

  def __init__(self, controlador_carrinho):
    self.__controlador = controlador_carrinho

  def mostra_opcoes(self):
    print("------ REALIZAR COMPRA ------")
    print("1 - Listar produtos disponíveis")
    print("2 - Adicionar produto")
    print("3 - Remover produto")
    print("4 - Atualizar quantidade")
    print("5 - Limpar carrinho")
    print("6 - Listar produtos do carrinho")
    print("7 - Finalizar compra")
    print("0 - Voltar")
    
    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1,2,3,4,5,6,7,0])
    return opcao

  def requisita_dado_adicionar(self):
    print("------ ADICIONAR PRODUTO NO CARRINHO------")
    codigo = int(input("Codigo do produto: "))
    quantidade = int(input("Quantidade: "))
    return {"codigo": codigo, "quantidade": quantidade}
   

  def mostra_produtos_adicionados(self, codigo: int, nome: str, valor: float, quantidade: int):
    print("Codigo: ", codigo)
    print("Nome: ", nome)
    print("Valor: ", valor)
    print("Quantidade: ", quantidade)

  def requisita_dado_remover(self):
    print("------REMOVER PRODUTO DO CARRINHO------")
    codigo = int(input("Digite o codigo do produto: "))
    return {"codigo": codigo}

  def total_valor_carrinho(self, total: float):
    print("Valor total a pagar: ", total)

  def requisita_dado_atualizar(self):
    print("------ATUALIZAR QUANTIDADE DO PRODUTO------")
    codigo = int(input("Digite o codigo do produto que deseja atualizar a quantidade: "))
    quantidade = int(input("Digite a quantidade do produto que deseja atualizar: "))
  
    return {"codigo": codigo, "quantidade": quantidade}

  def avisos(self):
    pass