from controlador.abstract_controlador import AbstractControlador
from entidade.cliente import Cliente
from tela.tela_cliente import TelaCliente


class ControladorCliente(AbstractControlador):
    def __init__(self, controlador):
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
            1: self.login_cliente,
            2: self.adiciona,
            0: self.finaliza_tela}

        # self.limpa_tela()
        self.__exibe_tela = True

        while self.__exibe_tela:
            opcao_escolhida = self.__tela_cliente.mostra_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            self.limpa_tela()
            funcao_escolhida()

    def login_cliente(self):
        cpf, senha = self.__tela_cliente.login()
        encontrou = False
        for um_cliente in self.__clientes:
            if cpf == um_cliente.cpf and senha == um_cliente.senha:
                encontrou = True
                break

        if encontrou:
            self.__cliente_logado = um_cliente
            self.cliente_opcoes()
            self.limpa_tela()
        else:
            self.__tela_cliente.avisos("dados_invalidos")

    def adiciona(self):
        nome, cpf, senha = self.__tela_cliente.dados_cadastro()
        for um_cliente in self.__clientes:
            if um_cliente.cpf == cpf:
                self.__tela_cliente.avisos("usuario_ja_cadastrado")
                break
            else:
                cliente = Cliente(nome, cpf, senha)
                self.__clientes.append(cliente)
                self.__tela_cliente.avisos("cadastrar")
                break

    def finaliza_tela(self):
        self.__exibe_tela = False
        self.limpa_tela()

    def cliente_opcoes(self):
        lista_opcoes = {
            1: self.compra,
            2: self.ver_cadastro,
            3: self.atualiza,
            4: self.remove,
            5: self.lista_nota_fiscal,
            0: self.desloga
        }

        # self.limpa_tela()
        self.__log_cliente = True
        while self.__log_cliente:
            opcao_escolhida = self.__tela_cliente.tela_cliente_logado(self.__cliente_logado.nome)

            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def compra(self):
        self.limpa_tela()
        self.__controlador_principal.mostra_tela_carrinho()

    def ver_cadastro(self):
        self.limpa_tela()
        self.__tela_cliente.tela_mostra_cadastro(self.__cliente_logado.nome,
                                                 self.__cliente_logado.cpf,
                                                 self.__cliente_logado.senha)

    def atualiza(self):
        opcao, dado = self.__tela_cliente.tela_atualiza_cadastro()
        if opcao == 1:
            self.__cliente_logado.nome = dado
            self.__tela_cliente.avisos("atualiza")
        elif opcao == 2:
            self.__cliente_logado.senha = dado
            self.__tela_cliente.avisos("atualiza")

        if opcao != 0:
            for um_cliente in self.__clientes:
                if self.__cliente_logado.cpf == um_cliente:
                    self.__clientes[um_cliente] = self.__cliente_logado
                    break

    def remove(self):
        cpf, senha = self.__tela_cliente.tela_remove()

        if cpf == 0 and senha == -1:
            self.__tela_cliente.avisos("operacao_cancelada")

        else:
            for um_cliente in self.__clientes:
                if cpf == um_cliente.cpf and senha == um_cliente.senha:
                    self.__clientes.remove(um_cliente)
                    self.__cliente_logado = None
                    self.__tela_cliente.avisos("remover")
                    self.__log_cliente = False
                    break

            if cpf != um_cliente.cpf or senha != um_cliente.senha:
                self.__tela_cliente.avisos("dados_invalidos")

    def lista_nota_fiscal(self):
        for nota_fiscal in self.__cliente_logado.notas_fiscais:
            nota_fiscal.relatorio_compras()

    def desloga(self):
        # self.limpa_tela()
        opcao = self.__tela_cliente.confirma_tela("pessoa", self.__cliente_logado.nome)
        if opcao == 1:
            self.__log_cliente = False
            self.__cliente_logado = None
            self.limpa_tela()

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