
from tela.nota_fiscal import NotaFiscal
from persistencia.nota_fiscal_dao import NotaFiscalDAO
class ControladorNotaFiscal:

    def __init__(self,controlador):
        self.__controlador_principal = controlador
        self.__tela_nf= NotaFiscal()
        self.__nota_fiscal_dao = NotaFiscalDAO()
        self.__lista_nf=[]

    def lista(self):
        for nf in self.__nota_fiscal_dao.get_all():
            self.__lista_nf.append(nf)
        return self.__lista_nf

    def tela_nf(self, lista_nf):
        self.__tela_nf.mostra_nf(lista_nf)

    def adiciona(self,cpf_cliente,total):
        nota_fiscal = [cpf_cliente,total]
        self.__nota_fiscal_dao.add(nota_fiscal)


