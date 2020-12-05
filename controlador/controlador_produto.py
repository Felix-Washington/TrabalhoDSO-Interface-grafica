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

    def remove(self, codigo_produto_selecionado):
        produto = self.__produto_dao.get(codigo_produto_selecionado)
        self.__produto_dao.remove(produto.codigo)
        self.__tela_produto.avisos("remove_produto")

    def atualiza(self, codigo_produto_selecionado):
        produto = self.__produto_dao.get(codigo_produto_selecionado)

        button, values = self.__tela_produto.requisita_dado_atualizar(produto.nome, produto.valor, produto.quantidade)
        print(values)


        if button == "Cancelar":
            self.__tela_produto.close()
        elif values['nome'] == "" or values['valor'] == "" or values['quantidade'] == "":
            self.__tela_produto.avisos("campo_vazio")
        else:
            produto.nome = values['nome']
            produto.valor = values['valor']
            produto.quantidade = values['quantidade']


            self.__produto_dao.add(produto)

        self.__tela_produto.close()

    def lista_produtos_disponiveis(self):
        produtos = []
        for produto in self.__produto_dao.get_all():
            produtos.append('{:3d}'.format(produto.codigo) + '-' + produto.nome + '-' + str(produto.valor) + '-' +
                         str(produto.quantidade))
        return produtos
    def lista(self):
        tela_lista = True

        while tela_lista:
            dados = []
            for produto in self.__produto_dao.get_all():
                dados.append('{:3d}'.format(produto.codigo) +'-'+ produto.nome +'-'+ str(produto.valor) +'-'+
                                                             str(produto.quantidade))

            button, values = self.__tela_produto.mostra_dados_cadastrados(dados)
            print(values)
            self.__tela_produto.close()
            if button == "Voltar":
                tela_lista = False
            elif button == "Alterar produto":
                #primeira posição [0] é do dicionário, a segunda posição [0] é pra pegar o item selecionado do listbox, e o [0:3] é para pegar somente o código do produto
                self.atualiza(int(values[0][0][0:3]))

            elif button == "Remover produto":
                #dados_obj = values['lb_produtos'][0]
                self.remove(int(values[0][0][0:3]))


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