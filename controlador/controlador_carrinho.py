from entidade.carrinho import Carrinho
from tela.tela_carrinho import TelaCarrinho
from controlador.abstract_controlador import AbstractControlador
from entidade.produto import Produto


class ControladorCarrinho(AbstractControlador):

    def __init__(self, controlador):
        self.__controlador_principal = controlador
        self.__tela_carrinho = TelaCarrinho()
        self.__produtos_carrinho = []

    def adiciona(self, produto_selecionado):

        lista_separada = produto_selecionado[0].split("-")
        codigo = int(lista_separada[0])
        nome = lista_separada[1]
        valor = lista_separada[2]
        pode_add = self.__controlador_principal.controlador_produto.verifica_quantidade(
            int(codigo))

        if pode_add:
            if self.__produtos_carrinho == []:
                self.__produtos_carrinho.append([str(codigo), nome, str(valor), str(1)])
            else:
                produto_dentro = False
                for produto_verifica in self.__produtos_carrinho:
                    if str(codigo) == produto_verifica[0]:
                        produto_dentro = True
                        break
                    else:
                        produto_dentro = False
                if produto_dentro:
                    for produto in self.__produtos_carrinho:
                        if str(codigo) == produto[0]:
                            produto[3] = int(produto[3])
                            produto[3] += 1
                            produto[3] = str(produto[3])
                            break
                else:
                    self.__produtos_carrinho.append([str(codigo), nome, str(valor), str(1)])

            self.__controlador_principal.controlador_produto.atualiza_quantidade(codigo)

        else:
            self.__tela_carrinho.avisos("quantidade_insuficiente")

    def remove(self, produto_selecionado):

        codigo = produto_selecionado[0][0]
        for produto in self.__produtos_carrinho:
            if codigo == produto[0]:
                self.__controlador_principal.controlador_produto.atualiza_estoque_carrinho(int(produto[0]), 1)
                produto[3] = int(produto[3])
                produto[3] -= 1
                produto[3] = str(produto[3])
                if int(produto[3]) <= 0:
                    self.__produtos_carrinho.remove(produto)
                    break

    def limpa_carrinho(self):

        for produto in self.__produtos_carrinho:
            self.__controlador_principal.controlador_produto.atualiza_estoque_carrinho(int(produto[0]), int(produto[3]))
        self.__produtos_carrinho = []

        self.__tela_carrinho.avisos("limpa_carrinho")

    def finaliza_tela(self):
        pass

    def finaliza_compra(self):
        if self.__produtos_carrinho == []:
            self.__tela_carrinho.avisos("carrinho_vazio")

        else:
            total = 0
            for produto in self.__produtos_carrinho:
                total += int(produto[2]) * int(produto[3])

            button, values = self.__tela_carrinho.confirma_tela("finaliza_compra")

            if button == "Sim":
                self.__controlador_principal.nf_cliente(total)
                self.__tela_carrinho.close()
                self.__produtos_carrinho = []
                self.__tela_carrinho.avisos("compra_finalizada")


            elif button == "Não":
                self.__tela_carrinho.avisos("compra_cancelada")

    def atualiza(self,dados_obj):
        pass

    def abre_tela_inicial(self):
        self.__exibe_tela = True


        while self.__exibe_tela:
            produtos_cadastrados = self.__controlador_principal.produtos_cadastrados()
            button, values = self.__tela_carrinho.mostra_opcoes(produtos_cadastrados, self.__produtos_carrinho)
            if button == "Voltar":
                self.limpa_carrinho()
                self.__exibe_tela = False

            elif button == "Finalizar compra":
                self.finaliza_compra()
                self.__exibe_tela = False


            elif button == "+":
                if not values[0]:
                    self.__tela_carrinho.avisos("selecionar_produto")
                else:
                    self.adiciona(values[0])

            elif button == "-":
                if not values[1]:
                    self.__tela_carrinho.avisos("selecionar_produto")
                else:
                    self.remove(values[1])

            elif button == "Limpar carrinho":
                self.limpa_carrinho()

            self.__tela_carrinho.close()

