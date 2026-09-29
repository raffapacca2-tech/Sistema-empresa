from colorama import Fore, Style, init

init(autoreset=True)


class cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class menu:
    def __init__(self):
        self.Clientes = []
    def exibir_menu(self):
        print(Fore.BLUE + Style.BRIGHT + "=== Menu de Cadastros ===")
        print("1. Cadastrar Cliente")
        print("3. Sair")

    def cadastrar_cliente(self):
        while True:
            try:
                nome = input("Digite o nome do cliente: ")
                if not nome.strip():
                    raise ValueError("Nome não pode estar vazio!")
                break
            except ValueError as e:
                print(Fore.RED + str(e))

        while True:
            try:
                email = input("Digite o email do cliente: ")
                if not email.strip():
                    raise ValueError("Email não pode estar vazio!")
                if "@" not in email:
                    raise ValueError("Email tem que ter @ obrigatoriamente!")
                break
            except ValueError as e:
                print(Fore.RED + str(e))

        while True:
            try:
                telefone = input("Digite o telefone do cliente: ")
                if not telefone.strip():
                    raise ValueError("Telefone não pode estar vazio!")
                if not telefone.strip().isdigit():
                    raise ValueError("Telefone só pode ter números, sem letras!")
                break
            except ValueError as e:
                print(Fore.RED + str(e))

        cliente_novo = cliente(nome, email, telefone)
        self.Clientes.append(cliente_novo)
        print(Fore.GREEN + "Cliente cadastrado com sucesso!")

    def executar(self):       
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_cliente()
            elif opcao == "3":
                print(Fore.BLUE + "Saindo...")
                break
            else:
                print(Fore.RED + "Opção inválida!")
if __name__ == "__main__":
    m = menu()
    m.executar()                