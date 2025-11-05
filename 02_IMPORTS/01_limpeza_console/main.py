# Importação de bibliotecas Python
import os

#LOOP
while True:
    # Limpeza de console (tradicional)
    os.system("cls")

    # tratamento de exceções
    try:
        # entrada de dados
        nome = input("Digite seu nome: ").strip().title()
        email = input("Digite seu e-mail: ").strip().lower()
        cpf = input("Digite seu CPF (somente números): ").strip()

        # limpeza de console (terminal)
        os.system("cls")

        # Saida de dados
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")

        # Menu 
        print("1 - Inserir novos dados")
        print("2 - Sair do programa")

        opcao = input("Opção desejada: ").strip()
    
        # verificação de opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
    except Exception as e:
        print("Não foi possível receber informações.")