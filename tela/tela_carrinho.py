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


  def requisita_dados_adicionar(self):
    print("------ ADICIONAR PRODUTO NO CARRINHO------")
    codigo = self.le_numero_inteiro("Codigo do produto: ", [])
    quantidade = self.le_numero_inteiro("Quantidade: ",[])
    return {"codigo": codigo, "quantidade": quantidade}


  def mostra_produtos_adicionados(self, codigo: int, nome: str, valor: float, quantidade: int):
    print("Codigo: ", codigo)
    print("Nome: ", nome)
    print("Valor: ", valor)
    print("Quantidade: ", quantidade)


  def requisita_dado_remover(self):
    print("------REMOVER PRODUTO DO CARRINHO------")
    codigo = self.le_numero_inteiro("Digite o codigo do produto: ", [])
    return {"codigo": codigo}


  def digite_codigo_valido(self):
    print("---------------------------------------")
    print("Digite um codigo valido")
    print("---------------------------------------")


  def total_valor_carrinho(self, total: float):
    print("Valor total a pagar: ", total, "\n")


  def requisita_dado_atualizar(self):
    print("------ATUALIZAR QUANTIDADE DO PRODUTO------")
    codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja atualizar a quantidade: ",[])
    quantidade = self.le_numero_inteiro("Digite a quantidade do produto que deseja atualizar: ", [])
    return {"codigo": codigo, "quantidade": quantidade}