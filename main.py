import cliente
from colorama import Fore, Style, init

init(autoreset=True)

import produto

def main():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "\n--- SISTEMA DA EMPRESA ---" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "1 - Clientes" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "2 - Produtos" + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "0 - Sair" + Style.RESET_ALL)
        op = input("Escolha: ")
        if op == "1":
            menu_cliente = cliente.Menu()
            menu_cliente.executar()
        elif op == "2":
            produto.executar()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
