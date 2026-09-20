import os
import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True) 

def menu():
    print()
    print(Fore.CYAN + Style.BRIGHT + "====== MENU ======")
    print("1- cadastar produtos \n2-listar produtos \n0-Encerrar programa \n")
while True:
    try:
        escolha = int(input("O que você deseja fazer?  "))
        if escolha in [0, 1, 2]:
           return escolha 
    except ValueError:
    print(Fore.RED + "Digite apenas um número!")
print(Fore.YELLOW + "Opção inválida! Digite 0, 1 ou 2.")

def cadastrar(arquivo):
    print()
    print("\n ====== CADASTRO DE PRODUTOS ====== \n ")

    nome_produto= input("Nome do produto: ")
    if nome_produto.strip() == "":
        print(Fore.RED + "O nome do produto não pode estar vazio!")
        continue 
    while True:
        try:
            preco = float(input("preço do produto: "))
            if preco <0:
                print(Fore.RED + "O preço deve ser maior que zero (0)")
                continue
                
            break
        except ValueError: 
        print(Fore.RED + "Digite um preço válido!")
        
    while True: 
        try: 
            quantidade= int(input("quantidade de produtos:"))
            if quantidade <0:
                print:(Fore.RED + "A quantidade deve ser maior que zero (0)")
                continue
                
            break
        except ValueError:
            print(Fore.RED + "Digite uma quantidade válida!")

    with open (arquivo, "a", encoding="utf-8") as dado:
        dado.write(
            f"{nome_produto}, {preco}, {quantidade}\n"
        )
            print(Fore.GREEN + "Produto cadastrado com sucesso!")
def listar_produtos(arquivo):
    print()
    print(Fore.GREEN + "====== PRODUTOS CADASTRADOS ====== \n")

    with open(arquivo, "r", encoding="utf-8") as dados:
        for linha in dados:
            lista=linha.split(", ")

            print(f"{Fore.YELLOW}Produto: {lista[0]} ")
            print(f"{Fore.YELLOW}Preço: {lista[1]}")
            print(f"{Fore.YELLOW}Quantidade: {lista[2]} ")


arquivo= r"C:\Users\manur\OneDrive\Documentos\EM 1DS\PA\trabalho em grupo\Desenvolvimento-colaborativo-com-git-e-github\produtos.txt"

while True:
    escolha= menu()

    if escolha == 1:
        cadastrar(arquivo)

    if escolha == 2:
        listar_produtos(arquivo)

    if escolha == 0:
        break

while True: 
    try:
    escolha = int(input("O que você deseja fazer? "))
    return escolha
except valueError:
    print(Fore.RED + "Digite apenas um número!")
