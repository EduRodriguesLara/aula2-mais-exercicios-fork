# 1: Em Aplicativo - Guarde o nome e o consumo de bateria no próprio objeto aplicativo;

# 2: Em Celular - Verifique se o celular está ligado (self.ligado) E se a bateria é maior 
# ou igual ao consumo do objeto 'app' passado por parâmetro;

# 3: Em executar_app - Subtraia o consumo do aplicativo da bateria atual do celular,
# não deve ser possivel executar um app com o celular desligado,
# deve se mostrado na tela o nome do aplicativo que foi usado.

# 4: Crie dois objetos Aplicativo com consumos de bateria diferentes;
# 5: Crie um objeto Celular, ligue o aparelho e execute cada um dos aplicativos criados.

class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        self.nome = nome
        self.consumo_bateria = consumo_bateria
        pass


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def checar(self):
        print(f"Fabricante: {self.marca}\nModelo: {self.modelo}\nBateria: {self.bateria}\nStatus: {self.ligado}")
        
    def recarregar(self, porcentagem):
        self.bateria += porcentagem
        if self.bateria < 100:
            print(f"Celular carregado, Bateria atual é de {self.bateria}%.")
        if self.bateria >= 100:
            self.bateria = 100
            print(f"Celular carregado, Bateria atual é de {self.bateria}%.")

    def ligar(self):
        if self.bateria <= 0:
            print("Carga insuficiente, Recarregue antes de ligar.")
        if self.bateria > 0:
            self.ligado = True
            print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        if self.ligado == False:
            print("Ligue o celular primeiro..")
        if self.ligado == True:
            if self.bateria < app.consumo_bateria:
                print("Bateria insuficiente, recarregue o dispositivo urgentemente senão você sera executado pela apple")
            if self.bateria >= app.consumo_bateria:
                print(f"O {self.modelo} executou {app.nome}, {app.consumo_bateria}% de bateria gasta.")
                self.bateria -= app.consumo_bateria
                if self.bateria <= 0:
                    self.ligado = False
                pass


telefone_celular = Celular("Apple", "Iphone 6s")
aplicativo_1 = Aplicativo("Fortune Tiger", 25)
aplicativo_2 = Aplicativo("Genshin Impact", 50)

telefone_celular.checar()
telefone_celular.ligar()
telefone_celular.checar()

telefone_celular.executar_app(aplicativo_1)
telefone_celular.checar()
telefone_celular.executar_app(aplicativo_1)
telefone_celular.checar()
telefone_celular.executar_app(aplicativo_2)
telefone_celular.checar()

telefone_celular.recarregar(25)
telefone_celular.checar()