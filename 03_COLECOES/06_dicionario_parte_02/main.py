# declaração de dicionário 
usuario = {
    'nome': "Lucax",
    'nascimento': "01/01/2001",
    'email': "lucax01@gmail.com",
    'telefone': "(61) 6666-6666",
    'endereço': "QI",
}

for chave in usuario:
    print(f"{chave.capitalize()}:{usuario[chave]}") 
    
