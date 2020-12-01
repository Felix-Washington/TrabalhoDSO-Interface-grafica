from controlador.abstract_controlador import AbstractControlador

from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario


class ControladorFuncionario(AbstractControlador):
    def __init__(self, controlador):
        self.__funcionarios = []
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_principal = controlador
        self.__funcionario_logado = None
        self.__exibe_tela = False

        self.__log_funcionario = False
        self.base_dados_funcionario()

    def abre_tela_inicial(self):
        self.__exibe_tela = True
        while self.__exibe_tela:
            lista_opcoes = {
                "Logar": self.login_funcionario,
                "Cadastrar": self.adiciona,
                "Voltar": self.finaliza_tela}

            button, values = self.__tela_funcionario.mostra_opcoes()
            funcao_escolhida = lista_opcoes[button]
            self.__tela_funcionario.close()
            funcao_escolhida()

    def login_funcionario(self):
        tela_login = True

        while tela_login:
            button, values = self.__tela_funcionario.login()

            if button == "Cancelar" or button == "None":
                tela_login = False
                self.__tela_funcionario.avisos("operacao_cancelada")

            elif values[0] == "" or values[1] == "":
                self.__tela_funcionario.avisos("campo_vazio")

            else:
                cpf = int(values[0])
                senha = values[1]
                encontrou = False

                for um_funcionario in self.__funcionarios:
                    if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
                        encontrou = True
                        break

                if encontrou:
                    self.__funcionario_logado = um_funcionario
                    self.funcionario_opcoes()
                    tela_login = False
                else:
                    self.__tela_funcionario.avisos("dados_invalidos")

            self.__tela_funcionario.close()

    def adiciona(self):
        tela_adiciona = True
        while tela_adiciona:
            button, values = self.__tela_funcionario.dados_cadastro()

            if button == "Cancelar":
                tela_adiciona = False

                self.__tela_funcionario.avisos("operacao_cancelada")

            elif values[0] == "" or values[1] == "" or values[2] == "":
                self.__tela_funcionario.avisos("campo_vazio")

            else:
                nome = values[0]
                cpf = int(values[1])
                senha = values[2]
                for um_funcionario in self.__funcionarios:

                    if um_funcionario.cpf == cpf:
                        self.__tela_funcionario.avisos("usuario_ja_cadastrado")
                        break
                    else:
                        funcionario = Funcionario(nome, cpf, senha)
                        self.__funcionarios.append(funcionario)
                        self.__tela_funcionario.avisos("cadastrar")
                        tela_adiciona = False
                        break

            self.__tela_funcionario.close()

    def finaliza_tela(self):
        self.__exibe_tela = False

    def funcionario_opcoes(self):
        self.__tela_funcionario.close()
        lista_opcoes = {
            "Ver Estoque": self.ver_estoque,
            "Cadastro": self.ver_cadastro,
            "Lista de clientes": self.lista_clientes,
            "Sair": self.desloga}

        self.__log_funcionario = True

        while self.__log_funcionario:
            button, values = self.__tela_funcionario.tela_funcionario_logado(self.__funcionario_logado.nome)
            funcao_escolhida = lista_opcoes[button]
            self.__tela_funcionario.close()
            funcao_escolhida()

    def ver_estoque(self):
        self.__controlador_principal.mostra_tela_produto()

    def ver_cadastro(self):
        tela_cadastro = True

        while tela_cadastro:
            button, values = self.__tela_funcionario.tela_mostra_cadastro(self.__funcionario_logado.nome,
                                                                      self.__funcionario_logado.cpf,
                                                                      self.__funcionario_logado.senha)
            self.__tela_funcionario.close()
            if button == "Alterar Cadastro":
                self.atualiza()

            elif button == "Remover Cadastro":
                self.remove()
                tela_cadastro = False
            else:
                tela_cadastro = False

    def atualiza(self):
        tela_atualiza = True

        while tela_atualiza:
            button, values = self.__tela_funcionario.tela_atualiza_cadastro()

            nome = values[0]
            senha = values[1]
            if button == "Cancelar":
                self.__tela_funcionario.avisos("operacao_cancelada")
                self.__tela_funcionario.close()
                tela_atualiza = False

            elif values[0] == "" or values[1] == "":
                self.__tela_funcionario.avisos("campo_vazio")
            else:

                self.__funcionario_logado.nome = nome
                self.__funcionario_logado.senha = senha

                self.__tela_funcionario.avisos("atualiza")
                self.__tela_funcionario.close()
                tela_atualiza = False

            self.__tela_funcionario.close()

    def remove(self):
        tela_remove = True

        while tela_remove:
            button, values = self.__tela_funcionario.tela_remove()
            if button == "Cancelar":
                self.__tela_funcionario.avisos("operacao_cancelada")
                tela_remove = False

            elif values[0] == "" or values[1] == "":
                self.__tela_funcionario.avisos("campo_vazio")

            else:
                #self.__tela_funcionario.confirma_tela()
                cpf = int(values[0])
                senha = values[1]
                for um_funcionario in self.__funcionarios:
                    if cpf == um_funcionario.cpf and senha == um_funcionario.senha:
                        self.__funcionarios.remove(um_funcionario)
                        self.__funcionario_logado = None
                        self.__tela_funcionario.avisos("remover")

                        self.__log_funcionario = False
                        tela_remove = False
                        break

                if cpf != um_funcionario.cpf or senha != um_funcionario.senha:
                    self.__tela_funcionario.avisos("dados_invalidos")

            self.__tela_funcionario.close()

    def lista_clientes(self):
        self.__tela_funcionario.mostra_clientes(self.__controlador_principal.controlador_cliente.lista_clientes())

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