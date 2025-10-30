# declaração de dicionário
veiculo = {
    'fabricante': "Chevrolet",
    'modelo': "Chevette",
    'ano': 1973,
    'cor': "branco",
    'placa': "DF-1973",
}

# exibe os dados
print("Dados atuais do veículo:")
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# usuário escolhe o campo que deseja mudar
while True:
    campo = input("\nInforme o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()

    if campo == 'sair':
        print("Programa encerrado.")
        break

    match campo:
        case "fabricante":
            veiculo['fabricante'] = input("Informe o novo valor de 'fabricante': ").strip()
        case "modelo":
            veiculo['modelo'] = input("Informe o novo valor de 'modelo': ").strip()
        case "ano":
            try:
                veiculo['ano'] = int(input("Informe o novo valor de 'ano': ").strip())
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro para o ano.")
                continue
        case "cor":
            veiculo['cor'] = input("Informe o novo valor de 'cor': ").strip()
        case "placa":
            veiculo['placa'] = input("Informe o novo valor de 'placa': ").strip()
        case _:
            print("Valor inválido.")
            continue

    # mostrar na tela os novos valores
    print("\nValores atualizados:")
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")



