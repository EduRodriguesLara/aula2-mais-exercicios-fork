class CofreDigital:
    def __init__(self,titular, senha, saldo = 0.0):
        self.titular = titular
        self._senha = senha
        self._saldo = saldo


    def alterar_senha(self):
        print("Gostaria de fazer uma alteração na sua senha?")
        escolha = input("S- Sim | N- Não\nOpção selecionada: ").lower()
        if escolha =="s":
            senha_nova = input("Digite sua Nova Senha: ")
            self._senha = senha_nova
            print(f"Senha alterada com Sucesso!")
        else:
            print("Operação Cancelada.")


    def sacar(self, valor:float):
        ativo = True
        print("Para Realizar o saque será nessesaria a sua senha.")
        while ativo == True:
            escolha = input("Digite sua senha: ")
            if escolha == self._senha:
                print("Senha correta.")
                print("Gostaria de fazer o Saque de R$",valor,"do Cofre Digital?")
                escolha = input("S- Sim | N- Não\nOpção selecionada: ").lower()
                if escolha == "s":
                    print("Operação realizada.")
                    self._saldo -= valor
                else:
                    print("Operação Cancelada.")

            else:
                print("Senha errada.\nQuer tentar novamente?")
                switch = input("S- Sim | N- Não").lower()
                match switch:
                    case "s":
                        pass
                    case "n":
                        ativo = False
                

    def depositar(self, valor:float):
        print("Gostaria de fazer o Deposito de R$",valor,"para o Cofre Digital?")
        escolha = input("S- Sim | N- Não\nOpção selecionada: ").lower()
        if escolha =="s":
            print("Operação realizada.")
            self._saldo += valor
        else:
            print("Operação Cancelada.")


    def menu(self):
        rodado = 1
        if rodado == 0:
            print(f"Seja Muito bem vindo {self.name}!")
        print(f"Qual operação você deseja realizar?")
        print(f"1- Sacar")
        print(f"2- Depositar")
        print(f"3- Alterar Senha")
        print(f"4- Encerrar Sessão")
        escolhido = int(input("Opção selecionada: "))
        match escolhido:
            case 1:
                try:
                    valor1 = float(input("Digite o Valor Desejado para o Saque.\nEscolhido:R$"))
                    usuario.sacar(valor1)
                    rodado += 1
                except:
                    print("Erro, tente digitar um valor valido")
            case 2:
                try:
                    valor2 = float(input("Digite o Valor Desejado para o Deposito.\nEscolhido:R$"))
                    usuario.depositar(valor2)
                    rodado += 1
                except:
                    print("Erro, tente digitar um valor valido")
            case 3:
                usuario.alterar_senha()
                rodado += 1
            case 4:
                print(f"Sessão encerrada, Até mais {self.name}!")
                active == False
                breakpoint

# Parte que define o objeto.
active = True
nome = input("Digite seu Nome: ")
senha = input("Digite sua Senha: ")
usuario = CofreDigital(nome,senha)
while active == True:
#    usuario.senha = "dudu"
    usuario.menu()