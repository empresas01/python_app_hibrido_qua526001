# TODO: Atividade 07 - 07/11/25
"""
#Crie um app de banco. o Programa deverá ter a classe conta, com os atributos:
titular da conta (nome)
 CPF Do Titular
Numero da agencia
Numero da da conta
O usuário irá inserir os dados "Titular da conta" e "CPF" , e poderá escolher entre as seguintes opções:
Consultar dados da conta
Depositar valor
Sacar valor
Sair do programa
"""
#Resposta:

class ContaBancaria:
    
    def __init__(self, titular, cpf):
        self.titular = titular.strip().title()
        self.cpf = cpf.strip()
        self.numero_agencia = "0001"
        self.numero_conta = "12345-6"
        self.saldo = 0.0

    def depositar(self, valor):
        """Deposita um valor na conta, se for positivo."""
        if valor > 0:
            self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        """Saca um valor da conta, se houver saldo suficiente."""
        if valor > self.saldo:
            return "Erro: Saldo insuficiente."
        elif valor <= 0:
            return "Erro: O valor do saque deve ser positivo."
        else:
            self.saldo -= valor
            return self.saldo
    def consultar_dados(self):
        """Retorna os dados da conta."""
        return {
            "Titular": self.titular,
            "CPF": self.cpf,
            "Número da Agência": self.numero_agencia,
            "Número da Conta": self.numero_conta,
            "Saldo": self.saldo
        }   
def main(): 
    titular = input("Digite o nome do titular da conta: ")
    cpf = input("Digite o CPF do titular: ")
    conta = ContaBancaria(titular, cpf)

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar dados da conta")
        print("2. Depositar valor")
        print("3. Sacar valor")
        print("4. Sair do programa")
        
        opcao = input("Opção: ")

        if opcao == "1":
            dados = conta.consultar_dados()
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
        elif opcao == "2":
            valor_deposito = float(input("Digite o valor a depositar: "))
            novo_saldo = conta.depositar(valor_deposito)
            print(f"Depósito realizado. Novo saldo: {novo_saldo}")
        elif opcao == "3":
            valor_saque = float(input("Digite o valor a sacar: "))
            resultado_saque = conta.sacar(valor_saque)
            if isinstance(resultado_saque, str):
                print(resultado_saque)
            else:
                print(f"Saque realizado. Novo saldo: {resultado_saque}")
        elif opcao == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()                  



        
    