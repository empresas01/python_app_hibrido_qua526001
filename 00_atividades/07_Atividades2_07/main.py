# TODO: Atividade 07
import os

from classe import Conta

def limpar():
    os.system("cls" if os.nome == "nt" else "clear")

def main():
    limpar() 
    
    cc = Conta(titular= "", cpf= "", agencia= "1234-5", n_conta= "12345-6", saldo=0)

    cc.titular = input("Informe o nome do titular da conta: ").strip().title()
    cc.cpf = input("Informe o CPF do titular: ").strip()

    limpar()

    while True:
             print("1. Consultar dados da conta")
             print("2. Depositar valor")
             print("3. Sacar valor")
             print("4. Sair do programa")
             opcao = input("Opção desejada: ").strip()

    match opcao:
        case "1":
            cc.consultar_dados()
            continue
        case "2":
            valor = float(input("Informe o valor a ser depositado: R$ ").strip().replace(",", "."))
            cc.depositar(valor)
            continue
        case "3":
            valor = float(input("Informe o valor a ser sacado: R$ ").strip().replace(",", "."))
            cc.sacar(valor)
            continue
        case "4":
            print("Programa encerrado")
            break
        case _:
            print("Opção inválida.")
            continue

if __name__ == "__main__":
    main()


