from entidade.carrinho import Carrinho
from tela.tela_carrinho import TelaCarrinho
from controlador.abstract_controlador import AbstractControlador
from entidade.produto import Produto
from tela.nota_fiscal import NotaFiscal
from persistencia.carrinho_dao import CarrinhoDAO

class ControladorCarrinho(AbstractControlador):

    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__tela_carrinho = TelaCarrinho()
        self.__carrinho_dao = CarrinhoDAO()
        self.__produtos_carrinho = []

    def lista_produtos_carrinho(self):
        for produto in self.__carrinho_dao.get_all():
            self.__tela_carrinho.mostra_produtos_adicionados(produto.codigo, produto.nome, produto.valor,
                                                             produto.quantidade)

        if self.__carrinho_dao == None:
            self.__tela_carrinho.avisos("carrinho_vazio")

    def adiciona(self, produto_selecionado):
        lista_separada = produto_selecionado[0].split("-")
        codigo = int(lista_separada[0])
        nome = lista_separada[1]
        valor = lista_separada[2]
        #quantidade = lista_separada[3]
        pode_add = self.__controlador_principal.controlador_produto.verifica_quantidade(
            codigo)
        if pode_add:
            if produto_selecionado not in self.__produtos_carrinho:
                self.__produtos_carrinho.append([str(codigo), nome, str(valor), str(1)])
            #else:
            #for produto in self.__produtos_carrinho:
                #if produto.codigo == codigo:
            self.__controlador_principal.controlador_produto.atualiza_quantidade(codigo)

                        #atualizar a quantidade aqui
                        #quantidade = produto.quantidade
                        #quantidade += 1
                        #produto = [str(codigo), nome, str(valor), str(1), str(quantidade)]
                        #self.__produtos_carrinho.append()

        else:
            self.__tela_carrinho.avisos("quantidade_insuficiente")


    def verifica_duplicidade(self, dados):
        existe = False
        duplicidade = False
        for produto in self.__controlador_principal.controlador_produto.produtos:
            if produto.codigo == dados["codigo"]:
                existe = True
                for prod in self.__carrinho_dao.get_all():
                    if prod.codigo == dados["codigo"]:
                        duplicidade = True
                        if dados["quantidade"] <= produto.quantidade:
                            prod.quantidade += dados["quantidade"]
                            produto.quantidade -= dados["quantidade"]
                            self.__tela_carrinho.avisos("produto_adicionado")
                            return duplicidade
                        elif dados["quantidade"] == prod.quantidade + produto.quantidade:
                            prod.quantidade += produto.quantidade
                            produto.quantidade = 0
                            return duplicidade
                        else:
                            self.__tela_carrinho.avisos("quantidade_insuficiente")

            if not existe:
                self.__tela_carrinho.avisos("codigo_invalido")

    def remove(self, produto_selecionado):
        print(self.__produtos_carrinho)
        if self.__produtos_carrinho != []:
            for produto in self.__produtos_carrinho:
                if produto_selecionado == produto:
                    if produto.quantidade > 0:
                        produto.quantidade -= 1
                        for prod in self.__controlador_principal.controlador_produto.produtos():
                            if prod.codigo == produto.codigo:
                                prod.quantidade += 1
                                break
                    else:
                        self.__produtos_carrinho.remove(produto_selecionado)

        else:
            self.__tela_carrinho.avisos("carrinho_vazio")

    def atualiza(self):
        existe = False
        dados = self.__tela_carrinho.requisita_dado_atualizar()
        for produto in self.__carrinho_dao.get_all():
            if produto.codigo == dados["codigo"]:
                existe = True
                for prod in self.__controlador_principal.controlador_produto.produtos:
                    if produto.codigo == prod.codigo:
                        if dados["quantidade"] < produto.quantidade:
                            prod.quantidade += (produto.quantidade - dados["quantidade"])
                            produto.quantidade = dados["quantidade"]
                            self.__tela_carrinho.avisos("atualiza_produto")
                            break
                        elif dados["quantidade"] == (prod.quantidade + produto.quantidade):
                            prod.quantidade = dados["quantidade"] - (prod.quantidade + produto.quantidade)
                            self.__tela_carrinho.avisos("atualiza_produto")
                        else:
                            self.__tela_carrinho.avisos("quantidade_insuficiente")
        if not existe:
            self.__tela_carrinho.avisos("codigo_invalido")

    def limpa_carrinho(self):
        if self.__produtos_carrinho != []:
            for produto in self.__produtos_carrinho:
                self.__controlador_principal.controlador_produto.atualiza_estoque_carrinho(produto.codigo, produto.quantidade)
            self.__produtos_carrinho = []
        else:
            self.__tela_carrinho.avisos("limpa_carrinho")

    def finaliza_tela(self):
        pass

    def finaliza_compra(self):
        if self.__produtos_carrinho == []:
            self.__tela_carrinho.avisos("carrinho_vazio")

        else:
            total = 0
            for produto in self.__carrinho_dao.get_all():
                total += produto.valor * produto.quantidade

            opcao = self.__tela_carrinho.confirma_tela("finaliza_compra", str(total))

            if opcao == 1:
                self.__tela_carrinho.avisos("compra_finalizada")
                nota_fiscal = NotaFiscal(self.__carrinho_dao)
                nota_fiscal.relatorio_compras()
                self.__controlador_principal.adiciona_nf_cliente(nota_fiscal)
            elif opcao == 2:
                self.__tela_carrinho.avisos("compra_cancelada")

    def abre_tela_inicial(self):
        self.__exibe_tela = True
        produtos_cadastrados = self.__controlador_principal.produtos_cadastrados()

        while self.__exibe_tela:
            button, values = self.__tela_carrinho.mostra_opcoes(produtos_cadastrados, self.__produtos_carrinho)
            if button == "Voltar":
                self.limpa_carrinho()
                self.__exibe_tela = False

            elif button == "Finalizar compra":
                self.finaliza_compra()

            elif button == "+":
                self.adiciona(values[0])

            elif button == "-":
                self.remove(values[1])

            elif button == "Limpar carrinho":
                self.limpa_carrinho()

            self.__tela_carrinho.close()

