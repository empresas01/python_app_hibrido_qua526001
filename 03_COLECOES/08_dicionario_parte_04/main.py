# declaração de coelções 
usuarios = [
    {
        'nome':"Fulano",
        'idade':20,
        'email':"fulando@gmail.com"
    },
    {
        'nome':"Cicrano",
        'idade':25,
        'email':"circrano@gmail.com"
    },
    {
        'nome':"Beltrano",
        'idade':22,
        'email':"beltrano@gmail.com"
    }
]

# Exibindo os dados dos usuarios
for usuario in usuarios:
    print(f"\n{'='*40}\n")
    for chave in usuario:
              print(f"{chave.capitalize()}: {usuario[chave]}") 