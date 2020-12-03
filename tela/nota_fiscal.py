import PySimpleGUI as sg


class NotaFiscal:
  def __init__(self, produtos):
    self.__produtos = produtos
    self.__window = None

  def open(self):
    button, values = self.__window.Read()
    return button, values

  def close(self):
    self.__window.Close()

  def relatorio_compras(self, cliente_notas_fiscais):
    valor_total = 0
    for produto in self.__produtos:
      print("Código: ", produto.codigo, "Nome: ", produto.nome, "Valor: ", produto.valor ,"Quantidade: ", produto.quantidade)
      valor_total += produto.valor * produto.quantidade

    return produtos
