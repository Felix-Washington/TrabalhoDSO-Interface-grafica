from entidade.pessoa import Pessoa

class Funcionario(Pessoa):

  def __init__(self, nome: str, cpf: int, senha: str):
    super().__init__(nome, cpf, senha)

