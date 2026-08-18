# ==============================================================================
# EXERCÍCIO - CLASSE BICICLETA
# ==============================================================================
# Crie uma estrutura para controlar a velocidade de uma bicicleta:
#
# 1. Classe Bicicleta:
#    - Atributos (__init__): modelo (str) e velocidade (int, iniciando em 0).
#    - Método pedalar(self): aumenta a velocidade em 5 e exibe:
#      "A bike [modelo] acelerou! Velocidade: X km/h"
#      A bike não pode passar de 60 km/h
#    - Método frear(self):
#      * Se a velocidade for maior que 0, diminui em 5 e exibe:
#        "Reduzindo... Velocidade: X km/h"
#      * Se a velocidade já for 0, exibe:
#        "A bicicleta já está totalmente parada!"
#    - Método radar_de_velocidade(self): exibe a velocidade atual.
#
# 2. Teste no Código:
#    - Instancie uma bicicleta: minha_bike = Bicicleta("Caloi")
#    - Chame o método pedalar() 2 vezes.
#    - Chame o método radar_de_velocidade().
#    - Chame o método frear() 3 vezes para validar a trava de velocidade zero.
# ==============================================================================
import random as rd
class Bicicleta:
    def __init__(self, modelo, velocidade=0):
        self.modelo = modelo
        self.velocidade = velocidade

    def pedalar(self):
        if self.velocidade >= 60:
            print(f"Velocidade maxima de {self.velocidade} ja foi alcançada!")
        if self.velocidade < 60:
            print(f"Velocidade antiga: {self.velocidade}Km/h")
            self.velocidade += 5
            print(f"Velocidade acelerou para {self.velocidade}Km/h!")

    def manobra(self):
        rng = rd.randint(1, 6)
        if rng > 3:
            print(f"Errou a manobra e quebrou o cranio batendo a cabeça em um cara fantasiado de fofão...")
        if rng == 3:
            print(f"Você decidiu não fazer a manobra por segurança.")
        if rng < 3:
            print(f"ACERTOU A MANOBRA, RADICAL!!")

    def freiar(self):
        if self.velocidade <= 0:
           print(f"A Bicicleta já foi foi parada!")
        if self.velocidade > 0:
            print(f"Velocidade antiga: {self.velocidade}Km/h")
            self.velocidade -= 5
            if self.velocidade <= 0:
                self.velocidade = 0
            print(f"Velocidade diminuiu para {self.velocidade}Km/h")

    def radar_velocidade(self):
        print(f"Velocidade atual: {self.velocidade}Km/h")

# Teste no codigo :D

bike = Bicicleta("Caloi")
bike.radar_velocidade()

bike.pedalar()
bike.pedalar()

bike.manobra()
bike.radar_velocidade

bike.freiar()
bike.freiar()
bike.freiar()