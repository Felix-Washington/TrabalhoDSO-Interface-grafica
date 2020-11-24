from tela.abstract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def __init__(self, controlador_produto):
        self.__controle = controlador_produto

    def mostra_opcoes(self):
        print("------ PRODUTO ------")
        print("1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("3 - Atualizar Produto")
        print("4 - Listar Produtos")
        print("0 - Voltar")

        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def requisita_dados_cadastro(self):
        print("------ CADASTRAR PRODUTO------")
        codigo = self.le_numero_inteiro("Codigo do produto: ", [])

        nome = self.verifica_palavra("Nome do produto: ")

        valor = self.verifica_float("Valor do produto: ")

        quantidade = self.le_numero_inteiro("Quantidade do produto: ", [])
        return {"codigo": codigo, "nome": nome, "valor": valor, "quantidade": quantidade}

    def mostra_dados_cadastrados(self, codigo: int, nome: str, valor: float, quantidade: int):
        print("---------------------------------")
        print("Codigo: ", codigo)
        print("Nome: ", nome)
        print("Valor: ", valor)
        print("Quantidade: ", quantidade)
        print("---------------------------------")

    def requisita_dado_remover(self):
        print("------REMOVER PRODUTO------")
        codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja remover: ", [])
        return codigo

    def requisita_dado_atualizar(self):
        print("------ATUALIZAR PRODUTO------")
        codigo = self.le_numero_inteiro("Digite o codigo do produto que deseja atualizar: ", [])
        return codigo

    def atualiza_produto(self):
        nome = self.verifica_palavra("Digite o novo nome: ")

        valor = self.verifica_float("Digite o novo valor: ")

        quantidade = self.le_numero_inteiro("Digite a nova quantidade: ", [])
        return {"nome": nome, "valor": valor, "quantidade": quantidade}

    def avisos(self, opcao: str):
        self.limpa_tela()

        if opcao == "produto_ja_cadastrado":
            print("Produto já cadastrado!", "\n")

        elif opcao == "produto_adicionado":
            print("Produto adicionado ao carrinho!", "\n")

        elif opcao == "produto_cadastrado":
            print("Produto cadastrado com sucesso!", "\n")

        elif opcao == "atualiza_produto":
            print("Produto alterado com sucesso!")
        elif opcao == "remove_produto":
            print("Produto removido do estoque!")
        elif opcao == "codigo_invalido":
            print("Digite um código válido!")