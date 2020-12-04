from tela.tela_produto import TelaProduto
from entidade.produto import Produto
from controlador.abstract_controlador import AbstractControlador
from persistencia.produto_dao import ProdutoDAO
import PySimpleGUI as sg

class ControladorProduto(AbstractControlador):

    def __init__(self):
        self.__produto_dao = ProdutoDAO()
        self.__tela_produto = TelaProduto(self)

    @property
    def produtos(self):
        return self.__produto_dao.get_all()

    def adiciona(self):
        tela_adiciona = True

        while tela_adiciona:
            button, values = self.__tela_produto.requisita_dados_cadastro()

            if button == "Cancelar":
                self.__tela_produto.avisos("operacao_cancelada")
                tela_adiciona = False

            elif values[0] == "" or values[1] == "" or values[2] == "" or values[3] == "":
                self.__tela_produto.avisos("campo_vazio")

            else:

                ja_existe = False
                for produto in self.__produto_dao.get_all():
                    if int(values[0]) == produto.codigo:
                        ja_existe = True
                        break
                if not ja_existe:
                    novo_produto = Produto(int(values[0]), values[1], values[2], values[3])
                    self.__produto_dao.add(novo_produto)
                    tela_adiciona = False
                    self.__tela_produto.avisos("produto_cadastrado")

                else:
                    self.__tela_produto.avisos("produto_ja_cadastrado")

            self.__tela_produto.close()

    def remove(self,dados):
        self.__produto_dao.remove(dados)
        #self.__window.find_element('list_produtos').Update(dados)
        #codigo = self.__tela_produto.requisita_dado_remover()
        #for produto in self.__produto_dao.get_all():
            #if produto.codigo == dados_obj:
             #   produto_remover = produto
              #  self.__produto_dao.remove(produto_remover)
               # self.__tela_produto.avisos("produto_removido")
                #break
            #else:
             #   self.__tela_produto.avisos("codigo_invalido")

    def atualiza(self, dados_obj):

        button, values = self.__tela_produto.requisita_dado_atualizar()
        codigo = values['codigo']
        nome = values['nome']
        valor = values['valor']
        quantidade = values['quantidade']
        if button == "Cancelar":
            self.__tela_produto.close()
        elif codigo == "" or nome == "" or valor == "" or quantidade == "":
            self.__tela_produto.avisos("campo_vazio")
        else:
            if dados_obj:
            #dados = [codigo,nome,valor,quantidade]
                for obj in self.__produto_dao.get_all():
                    if obj.codigo == codigo:
                        obj.nome = nome
                        obj.valor = valor
                        obj.quantidade = quantidade
            #self.__window.FindElement('lb_produtos').Update(dados)
                self.__tela_produto.close()

    def lista(self):
        tela_lista = True

        while tela_lista:
            dados = []
            for produto in self.__produto_dao.get_all():
                dados.append(str(produto.codigo) +'-'+ produto.nome +'-'+ str(produto.valor) +'-'+
                                                             str(produto.quantidade))

            button, values = self.__tela_produto.mostra_dados_cadastrados(dados)
            self.__tela_produto.close()
            if button == "Voltar":
                tela_lista = False
            elif button == "Alterar produto":
                dados_obj = values['lb_produtos'][0]
                self.atualiza(dados_obj)

            elif button == "Remover produto":
                if dados:
                    dados_obj = values['lb_produtos'][0]
                    self.remove(dados)

    def abre_tela_inicial(self):
        lista_opcoes = {
            "Adicionar produto": self.adiciona,
            "Listar produtos": self.lista,
            "Voltar": self.finaliza_tela}

        self.__exibe_tela = True
        while self.__exibe_tela:
            button, values = self.__tela_produto.mostra_opcoes()
            funcao_escolhida = lista_opcoes[button]
            self.__tela_produto.close()
            funcao_escolhida()

    def finaliza_tela(self):
        self.__tela_produto.close()
        self.__exibe_tela = False