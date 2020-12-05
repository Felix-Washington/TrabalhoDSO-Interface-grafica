from tela.abstract_tela import AbstractTela
import PySimpleGUI as sg

class TelaCliente(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):

        sg.ChangeLookAndFeel("Reddit")
        menu_def = [
            ['File', ['Open', 'Save', 'Exit', 'Properties']]
        ]

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):

        #super().close()
        self.__window.Close()

    def dados_cadastro(self):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text('Nome: ')],
            [sg.InputText()],
            [sg.Text("Cpf: ")],
            [sg.InputText()],
            [sg.Text("Senha: ")],
            [sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Cadastro de cliente").Layout(layout)

        return self.open()

    def login(self):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text("Cpf:")],
            [sg.InputText()],
            [sg.Text("Senha:")],
            [sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Login de cliente").Layout(layout)

        return self.open()

    def tela_remove(self):
        layout = [
            [sg.Text("Cpf:")],
            [sg.InputText()],
            [sg.Text("Senha:")],
            [sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Remover cadastro").Layout(layout)

        return self.open()

    def tela_atualiza_cadastro(self):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text('Nome: ')],
            [sg.InputText()],
            [sg.Text("Senha: ")],
            [sg.InputText()],

            [sg.Submit("Salvar"), sg.Cancel("Cancelar")]]

        self.__window = sg.Window("Alterar cadastro").Layout(layout)

        return self.open()

    def tela_mostra_cadastro(self, nome, cpf, senha):
        layout = [
            [sg.Text("Nome:", size=(10,1)), sg.Text(nome)],
            [sg.Text("Cpf:", size=(10,1)), sg.Text(cpf)],
            [sg.Text("Senha:", size=(10,1)), sg.Text(senha)],
            [sg.Button("Alterar Cadastro"), sg.Button("Remover Cadastro"), sg.Cancel("Voltar")]]

        self.__window = sg.Window(nome, default_element_size=(100, 50)).Layout(layout)

        return self.open()

    def tela_cliente_logado(self, nome_cliente: str):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text("Olá o que deseja?", size=(30, 2))],
            [sg.Button("Cadastro")],
            [sg.Button("Comprar")],
            [sg.Button("Notas Fiscais")],
            [sg.Button("Sair")]]

        self.__window = sg.Window(nome_cliente).Layout(layout)

        return self.open()

    def mostra_opcoes(self):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text('Como cliente você deseja?', size=(30, 2))],
            [sg.Cancel("Voltar")],

            [sg.Button("Logar"), sg.Button("Cadastrar")]]

        self.__window = sg.Window("Cliente").Layout(layout)

        return self.open()

    def mostra_notas_fiscais(self, notas_fiscais):
        layout = [
            # [sg.Menu(menu_def, tearoff=True)]
            [sg.Text("Notas Fiscais", size=(20, 1))],
            [sg.Listbox(values=notas_fiscais, size=(30, 5))],
            [sg.Cancel("Voltar")]]

        self.__window = sg.Window("Notas fiscais").Layout(layout)

        return self.open()

    def avisos(self, opcao: str):
        dicionario = {
            "cadastrar": "Cliente cadastrado com sucesso!",
            "remover": "Cliente removido com sucesso!",
            "dados_invalidos": "Erro! Digite o cpf ou a senha corretamente!",
            "desloga": "Usuário deslogado com sucesso!",
            "atualiza": "Dados alterados com sucesso!",
            "usuario_ja_cadastrado": "Cliente já cadastrado",
            "operacao_cancelada": "Operação Cancelada",
            "campo_vazio": "Preencha todos os campos!"}

        sg.Popup(dicionario[opcao])



