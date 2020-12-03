from entidade.produto import Produto
from persistencia.abstract_dao import AbstractDAO
from entidade.carrinho import Carrinho


class CarrinhoDAO(AbstractDAO):
    def __init__(self):
        super().__init__("carrinho.pkl")

    def add(self, produto: Produto):
        if (produto is not None) and (isinstance(produto, Produto)):
            super().add(produto.codigo, Produto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)