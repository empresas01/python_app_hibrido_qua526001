#biblioteca
import os

# função
def boas_vindas(nome):
    os.system("cls")
    print(f"Seja bem vindo, {nome}🐍 ")

    # algoritmo principal
os.system("cls")
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome) 