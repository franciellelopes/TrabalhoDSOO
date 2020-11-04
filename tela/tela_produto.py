from tela.abstract_tela import AbstractTela

class TelaProduto(AbstractTela):
    def __init__(self, controlador_produto):
      self.__controle = controlador_produto


    def mostra_opcoes(self): 
      print("------ PRODUTO ------")
      print("1 - Adicionar Produto")
      print("2 - Remover Produto")
      print("3 - Atualizar Produto")
      print("4 - Listar Produtos")
      print("5 - Imprimir Relatório de Estoque")
      print("0 - Voltar")
    
      opcao = self.le_numero_inteiro("Escolha a opcao: ", [1,2,3,4,5,0])
      return opcao
    def produto_ja_existe(self):
      print("------------------------------")
      print("Ja existe um produto com esse codigo")
      print("------------------------------")


    def requisita_dados_cadastro(self):
      print("------ CADASTRAR PRODUTO------")
      codigo = self.le_numero_inteiro("Codigo do produto: ", [])
      print("Nome do produto: ")
      nome = self.verifica_palavra()
      print("Valor do produto: ")
      valor = self.verifica_float()      
      quantidade = self.le_numero_inteiro("Quantidade do produto: ", [])
      return {"codigo": codigo, "nome": nome, "valor": valor, "quantidade": quantidade}


    def mostra_dados_cadastrados(self, codigo: int, nome: str, valor: float, quantidade: int):
      print("---------------------------------")
      print("Codigo: ", codigo)
      print("Nome: ", nome)
      print("Valor: ", valor)
      print("Quantidade: ",quantidade)
      print("---------------------------------")


    def requisita_dado_remover(self):
      print("------REMOVER PRODUTO------")
      codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja remover: ", [])
      return codigo


    def requisita_dado_atualizar(self):
      print("------ATUALIZAR PRODUTO------")
      codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja atualizar: ", [])
      return codigo


    def atualiza_produto(self):
      print("Digite o novo nome: ")
      nome = self.verifica_palavra()
      print("Digite o novo valor: ")
      valor = self.verifica_float()
      quantidade = self.le_numero_inteiro("Digite a nova quantidade: ", [])
      return {"nome": nome, "valor": valor, "quantidade": quantidade}


    def imprime_estoque(self):
      print("------ RELATORIO DO ESTOQUE------")
      print("---------------------------------")