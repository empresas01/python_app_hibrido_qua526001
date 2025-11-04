import os
import math # Importa o módulo math para usar math.sqrt (raiz quadrada)

# limpa console
def limpar():
    # Usa 'cls' no Windows e 'clear' em sistemas Unix/Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')

# funções de cálculo
def quadrado(l):
    return l**2

def retangulo(base, altura):
    return base * altura

def triangulo(base, altura):
    return (base * altura) / 2

# TODO: Atividade: Crie uma nova função para calcular a hipotenusa do triangulo
# Teorema de Pitágoras: a² + b² = c² -> c = sqrt(a² + b²)
def hipotenusa(cateto1, cateto2):
    # Usa math.sqrt para calcular a raiz quadrada da soma dos quadrados dos catetos
    return math.sqrt(cateto1**2 + cateto2**2)

# Função auxiliar para entrada de números decimais
def input_float(prompt):
    while True:
        try:
            # Permite que o usuário use ',' ou '.' como separador decimal
            valor = float(input(prompt).strip().replace(",", "."))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

# algoritmo principal
limpar()

while True:
    print("-----------------------------------")
    print("Escolha uma opção de cálculo:")
    print("1 - Calcular área do quadrado")
    print("2 - Calcular área do retângulo")
    print("3 - Calcular área do triângulo")
    print("4 - Calcular hipotenusa do triângulo")
    print("5 - Sair do programa")
    print("-----------------------------------")

    # Opção correta de input e validação básica
    opcao = input("Digite o número da opção desejada: ").strip()
    limpar()

    match opcao:
        case "1":
            lado = input_float("Informe o lado do quadrado: ")
            resultado = quadrado(lado)
            limpar()
            print(f"Área do quadrado: {resultado}")
            input("\nPressione Enter para continuar...") # Pausa para o usuário ver o resultado
            limpar()
            continue
        case "2":
            base = input_float("Informe a base do retângulo: ")
            altura = input_float("Informe a altura do retângulo: ")
            resultado = retangulo(base, altura)
            limpar()
            print(f"Área do retângulo: {resultado}")
            input("\nPressione Enter para continuar...")
            limpar()
            continue
        case "3":
            base = input_float("Informe a base do triângulo: ")
            altura = input_float("Informe a altura do triângulo: ")
            resultado = triangulo(base, altura)
            limpar()
            print(f"Área do triângulo: {resultado}")
            input("\nPressione Enter para continuar...")
            limpar()
            continue
        case "4":
            cateto1 = input_float("Informe o primeiro cateto: ")
            cateto2 = input_float("Informe o segundo cateto: ")
            resultado = hipotenusa(cateto1, cateto2)
            limpar()
            print(f"A hipotenusa é: {resultado}")
            input("\nPressione Enter para continuar...")
            limpar()
            continue
        case "5":
            print("Saindo do programa. Até mais!")
            break
        case _:
            print("Opção inválida. Por favor, tente novamente.")
            input("\nPressione Enter para continuar...")
            limpar()
            continue

-------------------

#salvar git
git config  user.name "empresas01"
git config user.email "empresaszero1@gmail.com"
git add .
git commit -m "Aula de hoje"
git push

