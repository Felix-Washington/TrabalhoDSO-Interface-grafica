from controlador.controlador_cliente import ControladorCliente
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_produto import ControladorProduto
from controlador.controlador_carrinho import ControladorCarrinho

from tela.tela_principal import TelaPrincipal


class ControladorPrincipal():
    def __init__(self):
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_produto = ControladorProduto()
        self.__controlador_carrinho = ControladorCarrinho(self)

        self.__tela_principal = TelaPrincipal(self)
        self.__exibe_tela = True

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def nota_fiscal(self):
        return self.__nota_fiscal

    def inicia(self):
        self.__tela_principal.avisos("inicia")
        self.abre_tela_inicial()

    def mostra_tela_funcionario(self):
        self.__controlador_funcionario.abre_tela_inicial()

    def mostra_tela_cliente(self):
        self.__controlador_cliente.abre_tela_inicial()

    def mostra_tela_produto(self):
        self.__controlador_produto.abre_tela_inicial()

    def mostra_tela_carrinho(self):
        self.__controlador_carrinho.abre_tela_inicial()

    def adiciona_nf_cliente(self, nota_fiscal):
        self.__controlador_cliente.cliente_logado.notas_fiscais.append(nota_fiscal)

    def abre_tela_inicial(self):
        lista_opcoes = {
            1: self.mostra_tela_funcionario,
            2: self.mostra_tela_cliente,
            0: self.fecha_sistema}

        while self.__exibe_tela:
            opcao_escolhida = self.__tela_principal.mostra_opcoes()

            funcao_escolhida = lista_opcoes[opcao_escolhida]

            funcao_escolhida()

    def fecha_sistema(self):
        self.__exibe_tela = False
        self.__tela_principal.avisos("finaliza")