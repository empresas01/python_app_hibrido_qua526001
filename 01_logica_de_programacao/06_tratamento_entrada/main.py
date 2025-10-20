# declaração de variável
nome = input("infome seu nome:").strip().title() # eliminação de espaços em brancoLucasLucas
idade = int(input("informe sua idade:").strip())
altura = float(input("informe sua altura:").strip().replace(",","."))

# saida de dados
print(f"nome do usuário: {nome}. Tipo {type(nome)}") 
print(f"Idade: {idade} Tipo {type(idade)}")