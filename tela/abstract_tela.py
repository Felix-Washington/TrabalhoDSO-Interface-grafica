from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def avisos(self, opcao: str):
        pass

    def limpa_tela(self):
        pass

    def confirma_tela(self, entidade: str):
        tipos_verificacoes = {
            "pessoa": "Tem certeza que deseja sair da sua conta?",
            "menu": "Tem certeza que quer fechar o sistema?",
            "atualiza": "Tem certeza que deseja mudar?",
            "remove_cadastro": "Tem certeza que deseja remover seu cadastro?",
            "finaliza_compra": "Tem certeza que deseja finalizar a compra?",
        }
        layout = [
            [sg.Text(tipos_verificacoes[entidade])],
            [sg.Button("Sim"), sg.Button("Não")],
        ]
        window = sg.Window("Confirmação").Layout(layout)
        button, values = window.Read()
        window.Close()
        return button, values
