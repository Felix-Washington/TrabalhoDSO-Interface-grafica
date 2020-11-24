from entidade.produto import Produto
from entidade.cliente import Cliente


class Carrinho:

    def __init___(self, quantidade: int, produto: Produto, cliente: Cliente):

        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        if isinstance(produto, Produto):
            self.__produto = produto
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente