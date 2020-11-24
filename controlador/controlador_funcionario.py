from controlador.abstract_controlador import AbstractControlador

from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario


class ControladorFuncionario(AbstractControlador):
    def __init__(self, controlador):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_principal = controlador
        self.__funcionario_logado = None

        self.__log_funcionario = False
        self.base_dados_funcionario()

    def abre_tela_inicial(self):
        lista_opcoes = {
            1: self.login_funcionario,
            2: self.adiciona,
            0: self.finaliza_tela}

        self.__exibe_tela = True

        while self.__exibe_tela:
            opcao_escolhida = self.__tela_funcionario.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            self.limpa_tela()
            funcao_escolhida()

    def login_funcionario(self):
        cpf, senha = self.__tela_funcionario.login()
        encontrou = False

        for um_funcionario in self.__funcionarios:
            if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
                encontrou = True
                break

        if encontrou:
            self.__funcionario_logado = um_funcionario
            self.funcionario_opcoes()
        if not encontrou:
            self.limpa_tela()
            self.__tela_funcionario.avisos("dados_invalidos")

    def adiciona(self):
        nome, cpf, senha = self.__tela_funcionario.dados_cadastro()
        self.limpa_tela()
        for um_funcionario in self.__funcionarios:
            if cpf == um_funcionario.cpf:
                self.__tela_funcionario.avisos("usuario_ja_cadastrado")
                break
            else:
                um_funcionario = Funcionario(nome, cpf, senha)
                self.__funcionarios.append(um_funcionario)
                self.__tela_funcionario.avisos("cadastrar")
                break

    def finaliza_tela(self):
        self.__exibe_tela = False
        self.limpa_tela()

    def funcionario_opcoes(self):
        lista_opcoes = {
            1: self.ver_estoque,
            2: self.ver_cadastro,
            3: self.atualiza,
            4: self.remove,
            5: self.lista_clientes,
            0: self.desloga}

        self.__log_funcionario = True
        self.limpa_tela()

        while self.__log_funcionario:
            opcao_escolhida = self.__tela_funcionario.tela_funcionario_logado(self.__funcionario_logado.nome)
            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()

    def ver_estoque(self):
        self.limpa_tela()
        self.__controlador_principal.mostra_tela_produto()

    def ver_cadastro(self):
        self.limpa_tela()
        self.__tela_funcionario.tela_mostra_cadastro(
            self.__funcionario_logado.nome,
            self.__funcionario_logado.cpf,
            self.__funcionario_logado.senha)

    def atualiza(self):
        opcao, dado = self.__tela_funcionario.tela_atualiza_cadastro()
        self.limpa_tela()
        if opcao == 1:
            self.__funcionario_logado.nome = dado
            self.__tela_funcionario.avisos("atualiza")
        elif opcao == 2:
            self.__funcionario_logado.senha = dado
            self.__tela_funcionario.avisos("atualiza")

        if opcao != 0:
            for um_funcionario in self.__funcionarios:
                if self.__funcionario_logado.cpf == um_funcionario:
                    self.__funcionarios[um_funcionario] = self.__funcionario_logado
                    break

    def remove(self):
        cpf, senha = self.__tela_funcionario.tela_remove()
        for um_funcionario in self.__funcionarios:

            if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
                self.__funcionarios.remove(um_funcionario)
                self.__tela_funcionario.avisos("remover")
                self.__log_funcionario = False
                break

            elif cpf == 0 and senha == 0:
                self.__tela_funcionario.avisos("operacao_cancelada")
                break

        if cpf != um_funcionario.cpf or senha != um_funcionario.senha:
            self.__tela_funcionario.avisos("dados_invalidos")

    def lista_clientes(self):
        self.__controlador_principal.controlador_cliente.lista_clientes()

    def desloga(self):
        opcao = self.__tela_funcionario.confirma_tela("pessoa", self.__funcionario_logado.nome)
        if opcao == 1:
            self.__log_funcionario = False
            self.limpa_tela()

    def base_dados_funcionario(self):
        funcionario = Funcionario("Felix", 123, "123")
        self.__funcionarios.append(funcionario)

        funcionario = Funcionario("Dorival", 123456, "123654")
        self.__funcionarios.append(funcionario)

        funcionario = Funcionario("Franciele", 321654, "456")
        self.__funcionarios.append(funcionario)