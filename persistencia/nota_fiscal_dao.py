from persistencia.abstract_dao import AbstractDAO
from entidade.nota_fiscal import NotaFiscal

class FuncionarioDAO(AbstractDAO):
    def __init__(self):
        super().__init__("clientes.pkl")

    def add(self, nota_fiscal: NotaFiscal):
        if (nota_fiscal is not None) and (isinstance(nota_fiscal, NotaFiscal)) and (isinstance((nota_fiscal.cpf, str))):
            super().add(nota_fiscal.cpf, int)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)
