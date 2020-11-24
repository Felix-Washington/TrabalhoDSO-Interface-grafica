from tela.tela_produto import TelaProduto
from entidade.produto import Produto
from controlador.abstract_controlador import AbstractControlador


class ControladorProduto(AbstractControlador):

    def __init__(self):
        self.__produtos = []
        self.__tela_produto = TelaProduto(self)
        self.base_dados_produto()

    @property
    def produtos(self):
        return self.__produtos

    def adiciona(self):
        dados = self.__tela_produto.requisita_dados_cadastro()
        ja_existe = False
        for produto in self.produtos:
            if dados["codigo"] == produto.codigo:
                ja_existe = True
                break
        if not ja_existe:
            novo_produto = Produto(dados["codigo"], dados["nome"], dados["valor"], dados["quantidade"])
            self.__produtos.append(novo_produto)
            self.__tela_produto.avisos("produto_cadastrado")
        else:
            self.__tela_produto.avisos("produto_ja_cadastrado")

    def remove(self):
        codigo = self.__tela_produto.requisita_dado_remover()
        for produto in self.__produtos:
            if produto.codigo == codigo:
                produto_remover = (produto)
                self.__produtos.remove(produto_remover)
                self.__tela_produto.avisos("produto_removido")
                break
            else:
                self.__tela_produto.avisos("codigo_invalido")

    def atualiza(self):
        existe = False
        codigo = self.__tela_produto.requisita_dado_atualizar()
        for produto in self.__produtos:
            if produto.codigo == codigo:
                existe = True

        if existe:
            dados = self.__tela_produto.atualiza_produto()
            produto.nome = dados["nome"]
            produto.valor = dados["valor"]
            produto.quantidade = dados["quantidade"]
            self.__tela_produto.avisos("atualiza_produto")
        else:
            self.__tela_produto.avisos("codigo_invalido")

    def lista(self):
        self.limpa_tela()
        for produto in self.__produtos:
            self.__tela_produto.mostra_dados_cadastrados(produto.codigo, produto.nome, produto.valor,
                                                         produto.quantidade)

    def abre_tela_inicial(self):
        opcoes = {
            1: self.adiciona,
            2: self.remove,
            3: self.atualiza,
            4: self.lista,
            0: self.finaliza_tela}

        self.limpa_tela()
        self.__exibe_tela = True
        while self.__exibe_tela:
            opcao = self.__tela_produto.mostra_opcoes()
            funcao = opcoes[opcao]
            funcao()

    def finaliza_tela(self):
        self.limpa_tela()
        self.__exibe_tela = False

    def base_dados_produto(self):
        produto = Produto(101, "Carrinho", 50, 3)
        self.__produtos.append(produto)

        produto = Produto(102, "Boneca", 30, 5)
        self.__produtos.append(produto)

        produto = Produto(103, "Urso de pelúcia", 25, 5)
        self.__produtos.append(produto)