# biblioteca
import os 

# declaração de lista
nomes = []

# Limpa o console
os.system("cls")

# loop
while True:
    print("1 - Inserir nome na lista")
    print("2 - Exibir lista de nomes")
    print("3 - Excluir nome da lista")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    match opcao:
        case "1":
            os.system("cls")
            novo_nome = input("Informe o novo nome: ").strip().title()
            nomes.append(novo_nome)
            os.system("cls")
            print(f"{novo_nome} cadastro com sucesso.")
            continue
        case "2":
            os.system("cls")
            print("\nLista de nomes:\n") 
            for i in range(len(nomes)):
                print(f"{i} - {nomes[i]}")
            print(f"\n{'-'*40}\n")
        case "3":
            os.system("cls")
            try:
                posicao = (input("informe a posição a ser excluida: ").strip())
                if posicao >=0 and posicao <  len(nomes):
                    del(nomes[posicao])            
            except Exception as e:
                print(f"Posição inválida.) {e}.")
        case "4":
            print("programa encerrado.")
            break
        case _:
            print("opção inválida.")
            continue