# Loop
while True:
    try:
       # menu
       print("1 Soma")
       print("2 Subtração")
       print("3 Multiplicação")
       print("4 Divisão")
       print("5 Sair do programa")
       opcao = input("Informe a opção desejada: ").strip()
       
       if opcao != "5":
          n1 = int(input("Informe o 1° número: ").strip())
          n2 = int(input("Informe o 2° número: ").strip())
          
          match opcao:
              case "1":
                result = n1+n2
                print(f"O resultado da soma é {result}.")
                continue
              case "2":
                result = n1-n2
                print(f"O resultado da subtração é {result}.")
                continue
              case "3":
                result = n1*n2
                print(f"O resultado da multiplicação é {result}.")
                continue
              case "4":
                result = n1/n2
                print(f"O resultado da divisão é {result}.")
                continue
              case _:
                print("Opção inválida.")
       else:
          print("Programa encerrado.")
          break
    except:
       print("Valores inválidos.")

