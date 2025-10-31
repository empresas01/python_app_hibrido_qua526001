# bibliotecas
import os

# declaração de lista
usuarios = []

os.system("cls")
while 'True':
    # menu
    print("1 - cadastrar novo usuário")
    print("2 - Lista de usuários")
    print("3 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls")
    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe o novo nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade: ").strip())
            usuario['email'] = input("Informe o email: ").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuario inserido com sucesso.")
            continue
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}\n")
        case "3":
            break
        case _:
            print("Opção inválida.")
            continue 