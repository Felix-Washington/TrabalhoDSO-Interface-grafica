from entidade.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: int, senha: str):
        super().__init__(nome, cpf, senha)
        self.__notas_fiscais = []

    @property
    def notas_fiscais(self):
        return self.__notas_fiscais

    @notas_fiscais.setter
    def notas_fiscais(self, notas_fiscais):
        self.__notas_fiscais = notas_fiscais