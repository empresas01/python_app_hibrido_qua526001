# tratamento de exceção
try:
    # entrada de dados
    numero = int(input("Informe um número inteiro positivo: ").strip())
    
    # laço de repetição
    while numero >= 0:
        print(numero)
        numero -= 1
except:
    print("Não foi possivel executar o contador.")