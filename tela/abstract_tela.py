from abc import ABC, abstractmethod
import os


class AbstractTela(ABC):
    @abstractmethod
    def __init__():
        pass

    def le_numero_inteiro(self, mensagem: str, opcoes_validas: []):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if len(opcoes_validas) > 0 and inteiro not in opcoes_validas:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Digite uma opção válida!")

    def verifica_float(self, mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                if type(valor) != float:
                    raise ValueError
                else:
                    return valor
            except ValueError:
                print("Digite apenas numeros")

    def verifica_palavra(self, mensagem):
        while True:
            valor = input(mensagem)

            try:
                ha_numero = any(char.isdigit() for char in valor)

                if ha_numero:
                    raise ValueError
                else:
                    return valor
            except ValueError:
                print("Digite apenas letras!")

    @abstractmethod
    def mostra_opcoes(self):
        pass

    @abstractmethod
    def avisos(self, opcao: str):
        pass

    def limpa_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def confirma_tela(self, entidade: str, nome: str):
        os.system('cls' if os.name == 'nt' else 'clear')

        if entidade == "pessoa":
            print(nome.lower().capitalize(), "tem certeza que deseja sair da sua conta?")

        elif entidade == "menu":
            print("Tem certeza que quer fechar o sistema?")

        elif entidade == "atualiza":
            print("Tem certeza que deseja mudar", nome)

        elif entidade == "volta":
            print("Tem certeza que deseja voltar?")

        elif entidade == "remove_cadastro":
            print("Tem certeza que deseja remover o cadastro?")

        elif entidade == "finaliza_compra":
            print("Tem certeza que deseja finalizar a compra de", nome, "R$?")

        print("1 - Sim")
        print("2 - Não")

        opcao = self.le_numero_inteiro("", [1, 2])

        return opcao