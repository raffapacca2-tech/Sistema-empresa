import cliente
from colorama import Fore, Style, init

init(autoreset=True)

import produto

def main():
    while True:
        print(f"{Fore.CYAN}\n--- SISTEMA DA EMPRESA ---{Style.RESET_ALL}")
        print(f"{Fore.GREEN}1 - Clientes{Style.RESET_ALL}")
        print(f"{Fore.GREEN}2 - Produtos{Style.RESET_ALL}")
        print(f"{Fore.RED}0 - Sair{Style.RESET_ALL}")
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
