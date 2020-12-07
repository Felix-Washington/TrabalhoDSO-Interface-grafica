

class NotaFiscal:

    def __init__(self, cpf_cliente: str, total: float):
        self.__cpf_cliente = cpf_cliente
        self.__total = total

    @property
    def cpf_cliente(self):
        return self.__cpf_cliente

    @property
    def total(self):
        return self.__total


