from colorama import Fore, Style, init

# Ativa o Colorama para usar cores no terminal
init(autoreset=True)


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone


class Menu:
    def __init__(self):
        self.clientes = []


    def exibir_menu(self):
        print(Fore.CYAN + "\n==============================")
        print(Fore.CYAN + Style.BRIGHT + "       MENU DE CADASTROS")
        print(Fore.CYAN + "==============================")
        print(Fore.GREEN + "1 - Cadastrar Cliente")
        print(Fore.YELLOW + "2 - Listar Clientes")
        print(Fore.RED + "3 - Sair")
        print(Fore.CYAN + "==============================")


    def cadastrar_cliente(self):

        # NOME
        while True:
            nome = input("Digite o nome: ").strip()

            # strip() remove espaços do início e do final
            if nome == "":
                print(Fore.RED + "Nome não pode estar vazio!")

            # replace() remove os espaços para verificar apenas as letras
            # isalpha() verifica se o texto contém somente letras
            elif not nome.replace(" ", "").isalpha():
                print(Fore.RED + "Nome deve conter apenas letras!")

            else:
                break


        # EMAIL
        while True:
            email = input("Digite o email: ").strip()

            if email == "":
                print(Fore.RED + "Email não pode estar vazio!")

            elif "@" not in email:
                print(Fore.RED + "Email precisa ter @!")

            elif "." not in email:
                print(Fore.RED + "Email inválido!")

            # Verifica se o email possui caracteres inválidos
            elif not all(c.isalnum() or c in "._+-@" for c in email):
                print(Fore.RED + "Email contém caracteres inválidos!")

            else:
                # Verifica se o email já está cadastrado
                email_repetido = False

                for cliente in self.clientes:
                    # lower() transforma o texto em minúsculas
                    if cliente.email.lower() == email.lower():
                        email_repetido = True
                        break

                if email_repetido:
                    print(Fore.RED + "Esse email já está cadastrado!")
                else:
                    break


        # TELEFONE
        while True:
            telefone = input("Digite o telefone: ").strip()

            if telefone == "":
                print(Fore.RED + "Telefone não pode estar vazio!")

            # isdigit() verifica se o texto contém somente números
            elif not telefone.isdigit():
                print(Fore.RED + "Telefone deve ter apenas números!")

            # len() conta a quantidade de caracteres
            elif len(telefone) < 10 or len(telefone) > 11:
                print(Fore.RED + "Telefone deve ter 10 ou 11 números!")

            else:
                break


        # Cria o objeto do cliente
        novo_cliente = Cliente(nome, email, telefone)

        # append() adiciona o cliente no final da lista
        self.clientes.append(novo_cliente)


        # SALVAR NO ARQUIVO

        # "a" permite adicionar dados sem apagar os anteriores
        # encoding="utf-8" permite salvar acentos e caracteres especiais
        arquivo = open("clientes.txt", "a", encoding="utf-8")

        # \n pula uma linha no arquivo
        arquivo.write("Nome: " + nome + "\n")
        arquivo.write("Email: " + email + "\n")
        arquivo.write("Telefone: " + telefone + "\n")
        arquivo.write("------------------------------\n")

        arquivo.close()

        print(Fore.GREEN + "\nCliente cadastrado com sucesso!")
        print(Fore.GREEN + "Dados salvos em clientes.txt")


    # NOVA FUNÇÃO: LISTAR CLIENTES
    def listar_clientes(self):

        if len(self.clientes) == 0:
            print(Fore.RED + "\nNenhum cliente cadastrado!")

        else:
            print(Fore.CYAN + "\n==============================")
            print(Fore.CYAN + Style.BRIGHT + "       CLIENTES CADASTRADOS")
            print(Fore.CYAN + "==============================")

            for cliente in self.clientes:
                print(Fore.GREEN + "Nome: " + cliente.nome)
                print(Fore.GREEN + "Email: " + cliente.email)
                print(Fore.GREEN + "Telefone: " + cliente.telefone)
                print(Fore.CYAN + "------------------------------")


    def executar(self):

        while True:
            self.exibir_menu()

            opcao = input(Fore.YELLOW + "Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":
                print(Fore.BLUE + "\nSaindo...")
                break

            else:
                print(Fore.RED + "\nOpção inválida!")


# Verifica se o código está sendo executado como programa principal
if __name__ == "__main__":
    menu = Menu()
    menu.executar()
