from persistencia.abstract_dao import AbstractDAO
from entidade.produto import Produto

class ProdutoDAO(AbstractDAO):
    def __init__(self):
        super().__init__("produtos.pkl")

    def add(self, produto: Produto):
        if (produto is not None) and (isinstance(produto, Produto)) and (isinstance(produto.codigo, int)):
            super().add(produto.codigo, produto)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)


    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)
