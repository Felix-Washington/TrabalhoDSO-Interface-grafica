from tela.abstract_tela import AbstractTela


class TelaFuncionario(AbstractTela):
    def __init__(self):
        pass

    def dados_cadastro(self):
        nome = self.verifica_palavra("Digite seu nome: ")

        cpf = self.le_numero_inteiro("Digite seu cpf:  ", "")

        senha = input("Digite a sua senha: ")

        return nome, cpf, senha

    def login(self):
        cpf = self.le_numero_inteiro("Digite seu cpf:  ", "")

        senha = input("Digite a sua senha: ")

        return cpf, senha

    def tela_atualiza_cadastro(self):
        print("O que você quer alterar?")
        print("1 - Nome")
        print("2 - Senha")

        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2])
        if opcao == 1:
            dado = self.verifica_palavra("Digite seu novo nome: ")

        elif opcao == 2:
            dado = input("Digite a sua nova senha: ")

        return opcao, dado

    def tela_remove(self):
        cpf = self.le_numero_inteiro("Digite seu cpf:  ", "")

        senha = input("Digite sua senha: ")

        opcao = self.confirma_tela("remove_cadastro", "")

        if opcao == 1:
            return cpf, senha
        elif opcao == 2:
            return 0, 0

    def tela_mostra_cadastro(self, nome, cpf, senha):
        print("--------------------------------------------")
        print("Nome:", nome.lower().capitalize())
        print("CPF:", cpf)
        print("Senha:", senha)
        print("--------------------------------------------")

    def tela_funcionario_logado(self, nome_funcionario: str):
        print("Ola", nome_funcionario.lower().capitalize(), "o que você deseja?")
        print("1 - Ver Estoque")
        print("2 - Ver Cadastro")
        print("3 - Alterar Cadastro")
        print("4 - Remover Cadastro")
        print("5 - Listar Clientes")
        print("0 - Sair")

        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 5, 0])

        return opcao

    def mostra_opcoes(self):
        print("Como funcionário você deseja:")
        print("1 - Logar")
        print("2 - Cadastrar")
        print("0 - Voltar")

        opcao = self.le_numero_inteiro("Escolha a opcao: ", [1, 2, 0])
        return opcao

    def avisos(self, opcao: str):
        self.limpa_tela()
        dicionario = {
            "cadastrar": "Funcionário cadastrado com sucesso!",
            "remover": "Funcionário removido com sucesso!",
            "dados_invalidos": "Erro! Digite o cpf ou a senha corretamente!",
            "atualiza": "Funcionário alterado com sucesso!",
            "usuario_ja_cadastrado": "Funcionário já cadastrado",
            "operacao_cancelada": "Operação Cancelada"}

        print("")
        print(dicionario[opcao])