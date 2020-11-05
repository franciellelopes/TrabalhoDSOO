

class NotaFiscal:
  def __init__(self):
    self.__produtos = []


  def relatorio_compras(self, produtos):
    valor_total = 0
    print("-------------------------------Nota-Fiscal--------------------------------")
    for produto in produtos:
      print("Código: ", produto.codigo, "Nome: ", produto.nome, "Valor: ", produto.valor ,"Quantidade: ", produto.quantidade)
      valor_total += produto.valor

    print("--------------------------------------------------------------------------")
    print("Total: ", valor_total)
    print("--------------------------------------------------------------------------")
    print("")

    self.__produtos = produtos
    for produto in self.__produtos:
      print("teste nome", produto.nome)

  def mostra_nota(self):
    valor_total = 0
    print("")
    print("-------------------------------Nota-Fiscal--------------------------------")
    for produto in self.__produtos:
      print("Código: ", produto.codigo, "Nome: ", produto.nome, "Valor: ", produto.valor, "Quantidade", produto.quantidade)

      
      valor_total += produto.valor
    print("Total: ", valor_total)
    print("--------------------------------------------------------------------------")
    print("")