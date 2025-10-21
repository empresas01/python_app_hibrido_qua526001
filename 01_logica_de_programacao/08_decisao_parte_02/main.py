# declaração de variáveis
nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade: ").strip())
altura = float(input("informe a altura: ").strip().replace(",","."))

# verificação das condições
if idade >= 12 and altura >= 1.15:
    print(f"{nome}, autorizado.")
else:
    print(f"{nome}, não autorizado.")
    