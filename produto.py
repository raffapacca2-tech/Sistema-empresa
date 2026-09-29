import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# CORRIGIDO: caminho relativo, funciona em qualquer PC
ARQUIVO = "produtos.txt"

def menu():
    print()
    print(Fore.CYAN + Style.BRIGHT + "====== MENU ======")
    print("1- Cadastrar produtos")
    print("2- Listar produtos")
    print("3- Excluir produto")
    print("0- Encerrar programa\n")
    while True:
        try:
            escolha = int(input("O que você deseja fazer? "))
            if escolha in [0, 1, 2, 3]:
                return escolha
            print(Fore.RED + "Opção inválida! Digite 0, 1, 2 ou 3.\n")
        except ValueError:
            print(Fore.RED + "Opção inválida! Digite 0, 1, 2 ou 3.\n")

def cadastrar(arquivo):
    print(Fore.GREEN + "\n====== CADASTRO DE PRODUTOS ======\n")
    while True:
        nome_produto = input("Nome do produto: ")
        if nome_produto.strip():
            break
        print(Fore.RED + "O nome do produto não pode estar vazio!\n")
    while True:
        try:
            preco = float(input("Preço do produto: ").replace(",", "."))
            if preco <= 0:
                print(Fore.RED + "O preço deve ser maior que zero.\n")
                continue
            break
        except ValueError:
            print(Fore.RED + "Digite um preço válido!\n")
    while True:
        try:
            quantidade = int(input("Quantidade de produtos: "))
            if quantidade <= 0:
                print(Fore.RED + "A quantidade deve ser maior que zero.\n")
                continue
            break
        except ValueError:
            print(Fore.RED + "Digite uma quantidade válida!\n")
    with open(arquivo, "a", encoding="utf-8") as dado:
        dado.write(f"{nome_produto};{preco};{quantidade}\n")
    print(Fore.GREEN + "Produto cadastrado com sucesso!")

def listar_produtos(arquivo):
    print()
    print(Fore.GREEN + "====== PRODUTOS CADASTRADOS ======\n")
    encontrou = False
    try:
        with open(arquivo, "r", encoding="utf-8") as dados:
            for linha in dados:
                lista = linha.strip().split(";")
                encontrou = True
                print(Fore.YELLOW + f"Produto: {lista[0]}")
                print(Fore.YELLOW + f"Preço: {lista[1]}")
                print(Fore.YELLOW + f"Quantidade: {lista[2]}")
                print()
        if not encontrou:
            print(Fore.YELLOW + "Nenhum produto cadastrado ainda!")
    except FileNotFoundError:
        print(Fore.RED + "Nenhum produto cadastrado ainda!")

def excluir_produto(arquivo):
    print()
    print(Fore.CYAN + "====== EXCLUIR PRODUTO ======\n")
    nome_excluir = input("Digite o nome do produto que deseja excluir: ")
    try:
        with open(arquivo, "r", encoding="utf-8") as dados:
            linhas = dados.readlines()
        novas_linhas = []
        encontrou = False
        for linha in linhas:
            lista = linha.strip().split(";")
            if lista[0].lower() == nome_excluir.strip().lower():
                encontrou = True
            else:
                novas_linhas.append(linha)
        if encontrou:
            with open(arquivo, "w", encoding="utf-8") as dados:
                dados.writelines(novas_linhas)
            print(Fore.GREEN + "Produto excluído com sucesso!")
        else:
            print(Fore.YELLOW + "Produto não encontrado!")
    except FileNotFoundError:
        print(Fore.YELLOW + "Nenhum produto cadastrado ainda!")

# FUNÇÃO QUE O MAIN.PY VAI CHAMAR
def executar():
    while True:
        escolha = menu()
        if escolha == 1:
            cadastrar(ARQUIVO)
        elif escolha == 2:
            listar_produtos(ARQUIVO)
        elif escolha == 3:
            excluir_produto(ARQUIVO)
        elif escolha == 0:
            break

# ISSO AQUI ARRUMA O SEU PRINT - só roda se executar direto o produto.py
if __name__ == "__main__":
    executar()
