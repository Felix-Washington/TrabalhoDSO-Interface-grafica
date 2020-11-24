
class NotaFiscal:
  def __init__(self, produtos):
    self.__produtos = produtos

  def relatorio_compras(self):
    valor_total = 0
    print("-------------------------------Nota-Fiscal--------------------------------")
    for produto in self.__produtos:
      print("Código: ", produto.codigo, "Nome: ", produto.nome, "Valor: ", produto.valor ,"Quantidade: ", produto.quantidade)
      valor_total += produto.valor * produto.quantidade

    print("--------------------------------------------------------------------------")
    print("Total: ", valor_total)
    print("--------------------------------------------------------------------------")
    print("")