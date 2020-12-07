from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaCarrinho(AbstractTela):

    def __init__(self):
        self.__window = None

    def mostra_opcoes(self, produtos, produto_novo):
        layout = [
            [sg.Text("Produtos disponíveis", size=(30, 1)), sg.Text("Produtos no carrinho")],
            [sg.Listbox(values=produtos, size=(30, 5)), sg.Listbox(values=produto_novo, size=(30,5))],
            [sg.Button("Finalizar compra")],
            [sg.Button("+"), sg.Button("-")],
            [sg.Button("Limpar carrinho"), sg.Cancel("Voltar")]]

        self.__window = sg.Window("Realizar Compra").Layout(layout)
        return self.open()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def avisos(self, opcao: str):
        dicionario = {
            "produto_removido": "Produto removido com sucesso",
            "compra_cancelada": "Compra cancelada!",
            "carrinho_vazio": "O carrinho está vazio",
            "quantidade_insuficiente": "Quantidade insuficiente no estoque!",
            "limpa_carrinho": "O carrinho foi esvaziado",
            "selecionar_produto": "Selecione um produto",
            "compra_finalizada": "Compra finalizada com sucesso"
        }

        sg.Popup(dicionario[opcao])