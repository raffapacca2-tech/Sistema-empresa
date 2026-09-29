# Sistema integrado - Projeto Final
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
            try:
                cliente.menu()
            except AttributeError:
                cliente.main()
        elif op == "2":
            try:
                produto.menu()
            except AttributeError:
                produto.main()
        elif op == "0":
            break

if __name__ == "__main__":
    main()
