from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente
from persistencia.cliente_dao import ClienteDAO

class ControladorCliente(AbstractControlador):
    def __init__(self, controlador):
        self.cliente_dao = ClienteDAO
        self.__clientes = []
        self.__tela_cliente = TelaCliente()
        self.__controlador_principal = controlador
        self.__cliente_logado = None

        self.__log_cliente = True

        self.base_dados_cliente()

    @property
    def clientes(self):
        return self.__clientes

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

            if button == "Cancelar":
                tela_login = False
                self.__tela_cliente.close()
                self.__tela_cliente.avisos("operacao_cancelada")

            elif values[0] == "" or values[1] == "":
                self.__tela_cliente.avisos("campo_vazio")

            else:
                cpf = int(values[0])
                senha = values[1]
                encontrou = False

                for um_cliente in self.__clientes:
                    if cpf == um_cliente.cpf and senha == um_cliente.senha:
                        encontrou = True
                        break

                if encontrou:
                    self.__cliente_logado = um_cliente
                    self.cliente_opcoes()
                    tela_login = False
                else:
                    self.__tela_cliente.avisos("dados_invalidos")

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
                nome = values[0]
                cpf = int(values[1])
                senha = values[2]
                for um_cliente in self.__clientes:

                    if um_cliente.cpf == cpf:
                        self.__tela_cliente.avisos("usuario_ja_cadastrado")
                        break
                    else:
                        cliente = Cliente(nome, cpf, senha)
                        self.__clientes.append(cliente)
                        self.__tela_cliente.avisos("cadastrar")
                        tela_adiciona = False
                        break

            self.__tela_funcionario.close()

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
        self.__tela_cliente.close()
        self.__controlador_principal.mostra_tela_carrinho()

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

            nome = values[0]
            senha = values[1]
            if button == "Cancelar":
                self.__tela_cliente.avisos("operacao_cancelada")
                self.__tela_cliente.close()
                tela_atualiza = False

            elif values[0] == "" or values[1] == "":
                self.__tela_cliente.avisos("campo_vazio")
            else:

                self.__cliente_logado.nome = nome
                self.__cliente_logado.senha = senha

                self.__tela_cliente.avisos("atualiza")
                self.__tela_cliente.close()
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
                for um_cliente in self.__clientes:
                    if cpf == um_cliente.cpf and senha == um_cliente.senha:
                        self.__clientes.remove(um_cliente)
                        self.__cliente_logado = None
                        self.__tela_cliente.avisos("remover")

                        self.__log_cliente = False
                        tela_remove = False
                        break

                if cpf != um_cliente.cpf or senha != um_cliente.senha:
                    self.__tela_cliente.avisos("dados_invalidos")

            self.__tela_cliente.close()

    def lista_nota_fiscal(self):
        for nota_fiscal in self.__cliente_logado.notas_fiscais:
            nota_fiscal.relatorio_compras()

    def desloga(self):

        button, values = self.__tela_cliente.confirma_tela("pessoa", self.__cliente_logado.nome)
        self.__tela_cliente.close()
        if button == "Sim":
            self.__log_cliente = False
            self.__cliente_logado = None
            self.__tela_cliente.avisos("desloga")

    def base_dados_cliente(self):
        cliente = Cliente("Lucas", 123, "123")
        self.__clientes.append(cliente)

        cliente = Cliente("Jade", 123456, "123654")
        self.__clientes.append(cliente)

        cliente = Cliente("Mariana", 321654, "456")
        self.__clientes.append(cliente)

    def lista_clientes(self):
        self.limpa_tela()
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_clientes(cliente.nome, cliente.cpf)