#Ficha cadastro de usuário

nome = input("Informe seu nome ou nome artístico 'apelido':").strip().title() 
idade = int(input("Informe sua idade:").strip())
cidade_natal = input("Informe sua cidade natal:").strip().title()
cidade_atual = input("Informe sua cidade atual:").strip().title()
estilos = input("Informe seus estilos de arte:").strip().title()
cursos_e_graduacoes = input("Informe seus cursos e graduações:").strip().title()
sexo = input("Informe seu sexo (M/F/Outro):").strip().title()
e_mail = input("Informe seu e-mail:").strip().title()
instagram = input("Informe seu instagram:").strip().title()
facebook = input("Informe seu facebook:").strip().title()
youtube = input("Informe seu canal do youtube:").strip().title()
tiktok = input("Informe seu perfil do tiktok:").strip().title()
spotify = input("Informe seu perfil do spotify:").strip().title()
twitch = input("Informe seu perfil do twitch:").strip().title()
git_hub = input("Informe seu perfil do git hub:").strip().title()
linkedin = input("Informe seu perfil do linkedin:").strip().title()
whatsapp = input("Informe seu número do whatsapp:").strip().title()
pcd = input("Você é uma pessoa com deficiência? (sim/não):").strip().title().boolean()



# saída de dado
print(f"Boa tarde, meu nome é {nome}, tenho {idade} anos, sou de {cidade_natal} e atualmente moro em {cidade_atual}.")

git config user.name "empresas01"
git config user.email "empresaszero1@gmail.com"
git status
git add .
git status
git commit -m "Aula de hoje"
git push
git config --unset-all user.name
git config --unset-all user.email
git config --list