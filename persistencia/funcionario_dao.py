from persistencia.abstract_dao import AbstractDAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(AbstractDAO):
    def __init__(self):
        super().__init__("funcionarios.pkl")

    def add(self, funcionario: Funcionario):
        if (funcionario is not None) and (isinstance(funcionario, Funcionario)) and (isinstance((funcionario.cpf, str))):
            super().add(funcionario.cpf, funcionario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key):
        if isinstance(key, int):
            super().remove(key)
