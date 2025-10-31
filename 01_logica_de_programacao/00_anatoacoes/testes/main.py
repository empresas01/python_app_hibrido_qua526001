import os

# declaração de lista
usuarios = []

while True:
    # os.system('cls') # Comentado para melhor visualização em alguns ambientes
    
    # menu
    print("1 - cadastrar novo usuário")
    print("2 - Lista de usuários")
    print("3 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case '1':
            usuario = {}
            usuario['nome'] = input("Informe o novo nome: ").strip().title()
            usuario['idade'] = int(input("Informe a idade: ").strip())
            usuario['email'] = input("Informe o email: ").strip().lower()
            usuarios.append(usuario)
            
            print("Novo usuario inserido com sucesso.")
            continue
        
        case '2':
            # CORREÇÃO: Itera sobre 'usuarios', não 'usuario'
            for usuario_cadastrado in usuarios: 
                for chave in usuario_cadastrado:
                    # CORREÇÃO: Sintaxe f-string correta
                    print(f"{chave.capitalize()}: {usuario_cadastrado[chave]}") 
                # CORREÇÃO: Sintaxe f-string correta e separador visual
                print("-" * 40)
            # Adicionado input para pausar a tela e permitir a visualização
            input("Pressione Enter para continuar...") 
            continue
        
        case '3':
            break
        
        case _:
            print("Opção inválida.")
            # Adicionado input para pausar a tela
            input("Pressione Enter para continuar...") 
            continue
