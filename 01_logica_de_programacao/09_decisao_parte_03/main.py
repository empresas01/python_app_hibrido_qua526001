# entrada de dados
aluno = input("Informe o nome do aluno: ").strip().title()
nota = float(input("Informe a primeira nota: ").strip().replace(",","."))

# verifica a nota do aluno  
if nota >= 0 and nota <= 10:
    if nota > 7:
      print(f'{aluno} está aprovado.')   
    elif nota >= 5:
      print(f'{aluno} está de recuperação.')
    else:
        print(f"{aluno} está reprovado.")
else:
    print(f"Nota do {aluno} inválida.")
     