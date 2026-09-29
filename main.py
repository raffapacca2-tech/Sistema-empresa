import cliente
import produto

def main():
    while True:
        print("\n--- SISTEMA DA EMPRESA ---")
        print("1 - Clientes")
        print("2 - Produtos")
        print("0 - Sair")
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
