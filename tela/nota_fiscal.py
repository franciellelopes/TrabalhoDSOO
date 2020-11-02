

class NotaFiscal:
  def __init__(self, produto):
    pass

  def relatorio_compras(self, produtos: []):
    valor_total = 0
    for produto in produtos:
      print("Código: ", produto.codigo, "Nome: ", produto.nome, "Quantidade: ", "Valor: ", produto.valor ,produto.quantidade)
      valor_total += produto.valor

    print("-----------------------------------------------------------------------------------------------------------------------------")
    print("Total: ", valor_total)