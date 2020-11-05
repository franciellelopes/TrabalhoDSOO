from abc import ABC, abstractmethod
import os

class AbstractTela(ABC):
  @abstractmethod
  def __init__():
    pass

  def le_numero_inteiro(self, mensagem: str, opcoes_validas: []):
    while True:
      valor_lido = input(mensagem)
      try:
        inteiro = int(valor_lido)
        if len(opcoes_validas) > 0 and inteiro not in opcoes_validas:
          raise ValueError
        return inteiro
      except ValueError:
        print("Digite uma opção válida!")


  def verifica_float(self, mensagem):
    while True:
      try:
        valor = float(input(mensagem))
        if type(valor) != float:
          raise ValueError
        else:
          return valor
      except ValueError:
          print("Digite apenas numeros")
        

  def verifica_palavra(self, mensagem):
    while True:
      valor = input(mensagem)
      
      try:
        ha_numero = any(char.isdigit() for char in valor)

        if ha_numero:
          raise ValueError
        else:
          return valor
      except ValueError:
        print("Digite apenas letras!")



  @abstractmethod
  def mostra_opcoes(self):
    pass


  def avisos(self, opcao: str, entidade: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcao == "cadastrar":
      print(entidade, "cadastrado com sucesso!", "\n")

    elif opcao == "remover":
      print(entidade, "removido com sucesso!", "\n")

    elif opcao == "dados_invalidos":
      print("Erro! Digite o cpf ou a senha corretamente!", "\n")

    elif opcao == "finaliza":
      print("Sistema Encerrado!")

    elif opcao == "inicia":
      print("Bem vindo a loja de brinquedos!", "\n")

    elif opcao == "atualiza":
      print(entidade, "alterado com sucesso!", "\n")

    elif opcao == "usuario_ja_cadastrado":
      print(entidade, "já cadastrado", "\n")

    elif opcao == "operacao_cancelada":
      print("Operação cancelada!", "\n")

    elif opcao == "compra_finalizada":
      print("Compra finalizada com sucesso!", "\n")
    
    elif opcao == "compra_cancelada":
      print("Compra cancelada!", "\n")

    elif opcao == "carrinho_vazio":
      print("Não há produtos no carrinho!", "\n")

    elif opcao == "quantidade_insuficiente":
      print("Quantidade insuficiente no estoque!")

    elif opcao == "produto_ja_cadastrado":
      print("Produto já cadastrado!", "\n")

    elif opcao == "produto_adicionado":
      print("Produto adicionado ao carrinho!", "\n")

    elif opcao == "produto_cadastrado":
      print("Produto cadastrado com sucesso!", "\n")

  def confirma_tela(self, entidade: str, nome: str):
    os.system('cls' if os.name == 'nt' else 'clear')

    if entidade == "pessoa":
      print(nome.lower().capitalize(), "tem certeza que deseja sair da sua conta?")

    elif entidade == "menu":
      print("Tem certeza que quer fechar o sistema?")

    elif entidade == "atualiza":
      print("Tem certeza que deseja mudar", nome)

    elif entidade == "volta":
      print("Tem certeza que deseja voltar?")

    elif entidade == "remove_cadastro":
      print("Tem certeza que deseja remover o cadastro?")

    elif entidade == "finaliza_compra":
      print("Tem certeza que deseja finalizar a compra de", nome, "R$?" )

    print("1 - Sim")
    print("2 - Não")

    opcao = self.le_numero_inteiro("", [1, 2])

    return opcao