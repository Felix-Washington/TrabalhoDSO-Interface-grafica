from controlador.abstract_controlador import AbstractControlador

from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario
from persistencia.funcionario_dao import FuncionarioDAO


class ControladorFuncionario(AbstractControlador):
    def __init__(self, controlador):
        self.__funcionario_dao = FuncionarioDAO()
        self.__tela_funcionario = TelaFuncionario()
        self.__controlador_principal = controlador
        self.__funcionario_logado = None
        self.__exibe_tela = False

        self.__log_funcionario = False

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
                for um_funcionario in self.__funcionario_dao.get_all():
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
                values[1] = int(values[1])
                encontrou = False
                for um_funcionario in self.__funcionario_dao.get_all():
                    if um_funcionario.cpf == values[1]:
                        encontrou = True

                if encontrou:
                    self.__tela_funcionario.avisos("usuario_ja_cadastrado")

                else:
                    funcionario = Funcionario(values[0], values[1], values[2])
                    self.__funcionario_dao.add(funcionario)
                    self.__tela_funcionario.avisos("cadastrar")
                    tela_adiciona = False


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

            if button == "Cancelar":
                self.__tela_funcionario.avisos("operacao_cancelada")
                tela_atualiza = False

            elif values[0] == "" or values[1] == "":
                self.__tela_funcionario.avisos("campo_vazio")
            else:

                self.__funcionario_logado.nome = values[0]
                self.__funcionario_logado.senha = values[1]
                self.__funcionario_dao.add(self.__funcionario_logado)


                self.__tela_funcionario.avisos("atualiza")
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
                cpf = int(values[0])
                senha = values[1]
                if cpf == self.__funcionario_logado.cpf and senha == self.__funcionario_logado.senha:
                    self.__funcionario_dao.remove(cpf)
                    tela_remove = False
                    self.__tela_funcionario.avisos("remover")

                else:
                    self.__tela_funcionario.avisos("dados_invalidos")
            self.__tela_funcionario.close()

    def lista_clientes(self):
        dados = [

        ]
        for cliente in self.__controlador_principal.controlador_cliente.lista_clientes():
            dados.append(cliente.nome + " "*30 + str(cliente.cpf))

        button, values = self.__tela_funcionario.mostra_clientes(dados)

        if button == "Voltar":
            self.__tela_funcionario.close()

    def desloga(self):

        button, values = self.__tela_funcionario.confirma_tela("pessoa")
        if button == "Sim":
            self.__log_funcionario = False
            self.__funcionario_logado = None

