import PySimpleGUI as sg


class NotaFiscal:
  def __init__(self):
    self.__window = None

  def open(self):
    button, values = self.__window.Read()
    return button, values

  def close(self):
    self.__window.Close()


  def mostra_nf(self, lista_nf):
    layout = [
       [sg.Listbox(values=lista_nf, size=(30, 5))],
      [sg.Submit("Ok")]
    ]
    self.__window = sg.Window("Nota Fiscal").Layout(layout)
    return self.open()