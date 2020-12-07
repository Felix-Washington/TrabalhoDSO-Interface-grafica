from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente
from persistencia.cliente_dao import ClienteDAO


class ControladorCliente(AbstractControlador):
    def __init__(self, controlador):
        self.__cliente_dao = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controlador_principal = controlador
        self.__cliente_logado = None
        self.__log_cliente = True


    @property
    def cliente_logado(self):
        return self.__cliente_logado

    def abre_tela_inicial(self):
        lista_opcoes = {
            "Logar": self.login_cliente,
            "Cadastrar": self.adiciona,
            "Voltar": self.finaliza_tela}

        self.__exibe_tela = True

        while self.__exibe_tela:
            button, values = self.__tela_cliente.mostra_opcoes()
            funcao_escolhida = lista_opcoes[button]
            self.__tela_cliente.close()
            funcao_escolhida()

    def login_cliente(self):
        tela_login = True

        while tela_login:
            button, values = self.__tela_cliente.login()

            if button == "Cancelar" or button == "None":
                tela_login = False
                self.__tela_cliente.avisos("operacao_cancelada")

            elif values[0] == "" or values[1] == "":
                self.__tela_cliente.avisos("campo_vazio")

            else:
                cpf = int(values[0])
                senha = values[1]
                encontrou = False

                cliente = None
                for um_cliente in self.__cliente_dao.get_all():
                    if cpf == um_cliente.cpf and senha == um_cliente.senha:
                        encontrou = True
                        cliente = um_cliente


                if encontrou:
                    self.__cliente_logado = cliente
                    self.cliente_opcoes()
                    tela_login = False
                else:
                    self.__tela_cliente.avisos("dados_invalidos")

            self.__tela_cliente.close()

    def adiciona(self):
        tela_adiciona = True
        while tela_adiciona:
            button, values = self.__tela_cliente.dados_cadastro()

            if button == "Cancelar":
                tela_adiciona = False

                self.__tela_cliente.avisos("operacao_cancelada")

            elif values[0] == "" or values[1] == "" or values[2] == "":
                self.__tela_cliente.avisos("campo_vazio")

            else:

                values[1] = int(values[1])
                encontrou = False

                for um_cliente in self.__cliente_dao.get_all():
                    if um_cliente.cpf == values[1]:
                        encontrou = True

                if encontrou:
                    self.__tela_cliente.avisos("usuario_ja_cadastrado")
                else:
                    cliente = Cliente(values[0], values[1], values[2])
                    self.__cliente_dao.add(cliente)
                    self.__tela_cliente.avisos("cadastrar")
                    tela_adiciona = False


            self.__tela_cliente.close()

    def finaliza_tela(self):
        self.__exibe_tela = False

    def cliente_opcoes(self):
        self.__tela_cliente.close()
        lista_opcoes = {
            "Comprar": self.compra,
            "Cadastro": self.ver_cadastro,
            "Notas Fiscais": self.lista_nota_fiscal,
            "Sair": self.desloga
        }

        self.__log_cliente = True
        while self.__log_cliente:
            button, values = self.__tela_cliente.tela_cliente_logado(self.__cliente_logado.nome)
            funcao_escolhida = lista_opcoes[button]
            self.__tela_cliente.close()
            funcao_escolhida()

    def compra(self):

        self.__controlador_principal.mostra_tela_carrinho()

    def dado_cliente(self):
        cpf_cliente = self.__cliente_logado.cpf
        return cpf_cliente

    def ver_cadastro(self):
        tela_cadastro = True

        while tela_cadastro:
            button, values = self.__tela_cliente.tela_mostra_cadastro(self.__cliente_logado.nome,
                                                                      self.__cliente_logado.cpf,
                                                                      self.__cliente_logado.senha)
            self.__tela_cliente.close()
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
            button, values = self.__tela_cliente.tela_atualiza_cadastro()

            if button == "Cancelar":
                self.__tela_cliente.avisos("operacao_cancelada")
                tela_atualiza = False

            elif values[0] == "" or values[1] == "":
                self.__tela_cliente.avisos("campo_vazio")
            else:

                self.__cliente_logado.nome = values[0]
                self.__cliente_logado.senha = values[1]
                self.__cliente_dao.add(self.__cliente_logado)
                self.__tela_cliente.avisos("atualiza")
                tela_atualiza = False

            self.__tela_cliente.close()

    def remove(self):
        tela_remove = True

        while tela_remove:
            button, values = self.__tela_cliente.tela_remove()
            if button == "Cancelar":
                self.__tela_cliente.avisos("operacao_cancelada")
                tela_remove = False

            elif values[0] == "" or values[1] == "":
                self.__tela_cliente.avisos("campo_vazio")

            else:
                cpf = int(values[0])
                senha = values[1]


                if cpf == self.__cliente_logado.cpf and senha == self.__cliente_logado.senha:
                    self.__cliente_dao.remove(cpf)
                    self.__log_cliente = False
                    tela_remove = False
                    self.__tela_cliente.avisos("remover")

                else:
                    self.__tela_cliente.avisos("dados_invalidos")


            self.__tela_cliente.close()

    def lista_nota_fiscal(self):

        button, values = self.__tela_cliente.mostra_notas_fiscais(self.__cliente_logado.notas_fiscais)

        if button == "Voltar":
            self.__tela_cliente.close()

    def desloga(self):

        button, values = self.__tela_cliente.confirma_tela("pessoa")
        if button == "Sim":
            self.__log_cliente = False
            self.__cliente_logado = None
            self.__tela_cliente.avisos("desloga")

        self.__tela_cliente.close()


    def lista_clientes(self):
        return self.__cliente_dao.get_all()

    def adiciona_nf(self, key, total):
        cliente = self.__cliente_dao.get(key)
        cliente.notas_fiscais.append("Valor total: "+str(total))
        self.__cliente_dao.add(cliente)