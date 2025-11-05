# bibliotecas
from modulo import limpar, primeiro_grau, segundo_grau

def main():
    limpar()
    while True:
        print("0 - Sair do programa")
        print("1 - Calcular equação do 1° grau")
        print("2 - Calcular equação do 2° grau")
        opcao = input("Opção deseja: ").strip()
        match opcao:
            case "0":
                limpar()
                print("Programa encerrado")
                break
            case "1":
                a = float(input("Digite o valor de a: ").strip().replace(",", "."))
                b = float(input("Digite o valor de b: ").strip().replace(",", "."))
                limpar()
                x = primeiro_grau(a, b)
                print(f"x = {x}")
                continue
            case "2":
                a = float(input("Digite o valor de 'a': ").strip().replace(",","."))
                b = float(input("Digite o valor de 'b': ").strip().replace(",","."))
                c = float(input("Digite o valor de 'c': ").strip().replace(",","."))
                limpar()
                resultados = segundo_grau(a, b, c)
                for x in resultados:
                    print(f"x = {x}")
                continue
            case _:
                limpar()
                print("Opção inválida.")
                continue
            
if __name__ == "__main__":
    main()
