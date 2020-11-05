from tela.abstract_tela import AbstractTela

class TelaCliente(AbstractTela):
  def __init__(self):
    pass


  def dados_cadastro(self):
    nome = self.verifica_palavra("Digite seu nome: ")

    cpf = self.le_numero_inteiro("Digite seu cpf: ", [])

    senha = input("Digite sua senha: ")

    return str(nome), int(cpf), str(senha)


  def login(self):    
    cpf = self.le_numero_inteiro("Digite seu cpf: ", [])

    senha = input("Digite sua senha: ")

    return cpf, senha


  def tela_remove(self):
    cpf = self.le_numero_inteiro("Digite seu cpf: ", []) 

    senha = input("Digite sua senha: ")

    opcao = self.confirma_tela("remove_cadastro", "")

    if opcao == 1:
      return cpf, senha
    elif opcao == 2:
      return 0, 0


  def tela_atualiza_cadastro(self):
    print("O que você deseja alterar?")
    print("1 - Nome")
    print("2 - Senha")
    print("0 - Voltar")
    
    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 0])

    if opcao == 1:
      dado = self.verifica_palavra("Digite seu novo nome: ")

    elif opcao == 2:
      dado = input("Digite sua nova senha: ")

    return opcao, dado
    

  def tela_mostra_cadastro(self, nome, cpf, senha):    
    print("--------------------------------------------")
    print("Nome:", nome.lower().capitalize())
    print("CPF:", cpf)
    print("Senha:", senha)
    print("--------------------------------------------")
    print("")


  def tela_cliente_logado(self, nome_cliente: str):
    print("Ola", nome_cliente.lower().capitalize(), "o que você deseja?")
    print("1 - Comprar")
    print("2 - Ver Cadastro")
    print("3 - Alterar Cadastro")
    print("4 - Remover Cadastro")
    print("5 - Notas Fiscais")
    print("0 - Sair")

    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])
    return opcao


  def mostra_opcoes(self):
    print("Como cliente você deseja:")
    print("1 - Logar")
    print("2 - Cadastrar")
    print("0 - Voltar")

    opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 0])
    return opcao

  def avisos(self, opcao: str, entidade: str):
    self.limpa_tela()
    
    if opcao == "cadastrar":
      print(entidade, "cadastrado com sucesso!", "\n")

    elif opcao == "remover":
      print(entidade, "removido com sucesso!", "\n")

    elif opcao == "dados_invalidos":
      print("Erro! Digite o cpf ou a senha corretamente!", "\n")

    elif opcao == "atualiza":
      print(entidade, "alterado com sucesso!", "\n")

    elif opcao == "usuario_ja_cadastrado":
      print(entidade, "já cadastrado", "\n")


