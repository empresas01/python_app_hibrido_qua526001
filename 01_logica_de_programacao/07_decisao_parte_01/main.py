# declaração de variável
nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade:").strip())

# decisão
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")