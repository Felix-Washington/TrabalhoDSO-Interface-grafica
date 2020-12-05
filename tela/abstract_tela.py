from abc import ABC, abstractmethod
import PySimpleGUI as sg


class AbstractTela(ABC):

    def __init__(self):
        pass
        #self.__window_confirmacao == None


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

    @abstractmethod
    def avisos(self, opcao: str):
        pass

    def limpa_tela(self):
        pass

    def confirma_tela(self, entidade: str, nome: str):
        tipos_verificacoes = {
            "pessoa": "Tem certeza que deseja sair da sua conta?",
            "menu": "Tem certeza que quer fechar o sistema?",
            "atualiza": "Tem certeza que deseja mudar?",
            "volta": "Tem certeza que deseja voltar?",
            "remove_cadastro": "Tem certeza que deseja remover seu cadastro?",
            "finaliza_compra": "Tem certeza que deseja finalizar a compra?",
        }
        layout = [
            [sg.Text(tipos_verificacoes[entidade])],
            [sg.Button("Sim"), sg.Button("Não")],
        ]
        window = sg.Window("Confirmação").Layout(layout)
        button, values = window.Read()
        return button, values
