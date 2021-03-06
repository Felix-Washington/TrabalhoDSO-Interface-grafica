import PySimpleGUI as sg
from tela.abstract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def __init__(self, controlador_produto):
        self.__controle = controlador_produto
        self.__window = None

    def mostra_opcoes(self):
        layout = [
            [sg.Text('O que você deseja?')],

            [sg.Button("Adicionar produto")],
            [sg.Button("Listar produtos")],

            [sg.Cancel("Voltar")]

        ]

        self.__window = sg.Window("Produtos").Layout(layout)
        return self.open()

    def open(self):
        button, values = self.__window.Read()
        return button, values


    def close(self):
        self.__window.Close()

    def requisita_dados_cadastro(self):
        layout = [
            [sg.Text('Código: ', size=(20, 1)), sg.InputText()],
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText()],
            [sg.Text("Valor: ", size=(20, 1)), sg.InputText()],
            [sg.Text("Quantidade", size=(20, 2)), sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Cadastro de produto").Layout(layout)
        return self.open()


    def mostra_produtos(self, dados):
        layout = [
            [sg.Text("Produtos cadastrados: ")],
            [sg.Listbox(values=dados, size=(30, 5))],
            [sg.Button("Alterar produto"), sg.Button("Remover produto"), sg.Cancel("Voltar")]]

        self.__window = sg.Window("Produtos").Layout(layout)
        return self.open()

    def requisita_dado_atualizar(self, nome= "", valor = "", quantidade= ""):
        layout = [
            [sg.Text("Nome: ", size=(20, 1)), sg.InputText(nome, key='nome')],
            [sg.Text("Valor: ", size=(20, 1)), sg.InputText(valor, key='valor')],
            [sg.Text("Quantidade", size=(20, 2)), sg.InputText(quantidade, key='quantidade')],

            [sg.Submit("Salvar Alteração"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Atualização de produto").Layout(layout)
        return self.open()

    def avisos(self, opcao: str):
        dicionario = {
            "produto_ja_cadastrado": "Produto já cadastrado!",
            "produto_adicionado": "Produto adicionado ao carrinho!",
            "produto_cadastrado": "Produto cadastrado com sucesso!",
            "atualiza_produto": "Produto alterado com sucesso!",
            "remove_produto": "Produto removido do estoque!",
            "codigo_invalido": "Digite um código válido!",
            "operacao_cancelada": "Operação cancelada!",
            "digite_dados_validos": "Digite dados validos",
            "selecione_produto": "Selecione um produto",
            "campo_vazio": "Preencha todos os campos!"
        }

        sg.Popup(dicionario[opcao])