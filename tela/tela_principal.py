from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaPrincipal(AbstractTela):

    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = None

    def init_components(self):

        sg.ChangeLookAndFeel("Reddit")
        menu_def = [
            ['File', ['Open', 'Save', 'Exit', 'Properties']]
        ]

    def mostra_opcoes(self):
        layout = [
            [sg.Text('Como você deseja entrar?', size=(30, 2))],

            [sg.Button("Funcionário"), sg.Button("Cliente")]]

        self.__window = sg.Window("Loja de Brinquedos", default_element_size=(100, 50)).Layout(layout)

        return self.open()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    @property
    def window(self):
        return self.__window


    def avisos(self, opcao: str):
        dicionario = {
            "inicia": "Bem vindo a loja de brinquedos!",
            "finaliza": "Sistema encerrado!",
            }

        sg.Popup(dicionario[opcao])