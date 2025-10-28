# delcaração de lista
nome = []

try:
    while True:
        print("1 - Inserir nome na lista")
        print("2 - Exibir nomes da lista")
        print("3 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        match opcao:
            case "1":
                novo_nome = input("Informe o novo nome: ").strip().title()
                nome.append(novo_nome)
                print(f"{novo_nome} Inserido com sucesso!.\n")
                pass
            case "2":
                print("\nLista de nomes:\n")
                pass
            case "3":
                break
            case _:
                print("Opção inválida. Tente novamente.")
except Exception as e:
    print(f"Erro ao exibir a lista: {e}")