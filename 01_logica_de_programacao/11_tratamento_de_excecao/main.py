# tratamento de exceções
try:
    # entrada de dados
    nome = input("Informe seu nome: ").strip()
    idade = int(input("Informe sua idade: ").strip())
    altura = float(input("Informe sua altura (em metros): ").strip().replace(",","."))

    # saída de dado
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
except:
    print("infelizmente o programa não pode ser executado.")