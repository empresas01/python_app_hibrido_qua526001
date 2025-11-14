#salvar git
git config  user.name "empresas01"
git config user.email "empresaszero1@gmail.com"
git add .
git commit -m "Aula de hoje"
git push


from dataclasses import dataclass

@dataclass
class Pessoa:
    email: str
    telefone: str
    endereço: str

    def __str__(self):
        return f"E-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
    
@dataclass
class PessoaFisica(Pessoa):
    nome: str
    idade: int
    cpf: str
    profissao: str

    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self.idade}\nCPF: {self.cpf}\nProfissão: {self.profissao}\n{super().__str__()}"
        return f"\nDADOS DO USUÁRIO:\nNome: {self.nome}\nIdade: {self}\nCPF: {self.cpf}\nProfissão: {self.profissao)\n{super().__str__()}"

def __len__(self):
    return self.idade

@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    def __str__(self):
        return f"\nDADOS DA EMPRESA:\nNome Fantasia: {self.nome_fantasia}\nCNPJ: {self.cnpj}\nWebsite: {self.website}\n{super().__str__()}"