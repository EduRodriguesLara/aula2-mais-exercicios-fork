# ==============================================================================
# EXERCÍCIO - CLASSE PET VIRTUAL (TAMAGOTCHI)
# ==============================================================================
# Crie uma estrutura do zero para controlar as necessidades de um bichinho virtual:
#
# 1. Classe PetVirtual:
#    - Atributos (__init__): nome (str), fome (int, iniciando em 5) e felicidade (int, iniciando em 5).
#    - Método alimentar(self):
#      * Se a fome for maior que 0, diminui a fome em 2 e exibe:
#        "[nome] foi alimentado! Fome atual: X"
#      * Se a fome já for 0, exibe: "[nome] já está de barriga cheia!"
#    - Método brincar(self):
#      * Aumenta a felicidade em 2 e aumenta a fome em 1.
#      * Exibe: "Você brincou com [nome]! Felicidade: X | Fome: Y"
#    - Método status(self):
#      * Exibe o nome do pet, a fome atual e a felicidade.
#      * Se a fome for maior ou igual a 8, exibe um alerta: "Atenção: [nome] precisa comer!"
#
# 2. Teste no Código:
#    - Instancie um pet virtual: meu_pet = PetVirtual("Pou")
#    - Chame o método status().
#    - Chame o método brincar() 2 vezes.
#    - Chame o método alimentar() 3 vezes.
#    - Chame o método status() novamente para conferir o resultado final.
# ==============================================================================
import random as rd
import sys
class Virtualpet:
    def __init__(self, nome:str, fome = 5, felicidade = 5, stamina = 100):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade
        self.stamina = stamina

    def brincar(self):
        if self.fome <= 0:
            print(f"{self.nome} Fugiu pela Fome..")
            sys.exit(0)
        if self.felicidade >= 66:
            print(f"{self.nome} Fugiu pela felicidade!!")
            sys.exit(0)
        if self.stamina < 25:
            print(f"{self.nome} está com muito sono para brincar.")
        if self.stamina >= 25:
            rng = rd.randint(1,6)
            match rng:
                case 1:
                    brincadeira = f"Jogou {self.nome} em um vulcão" 
                case 2:
                    brincadeira = f"Mandou {self.nome} para a coreia do norte" 
                case 3:
                    brincadeira = f"Jogou {self.nome} em um campo minado" 
                case 4:
                    brincadeira = f"Ensinou {self.nome} a jogar Pokemon" 
                case 5:
                    brincadeira = f"Jogou futebol com {self.nome}" 
                case 6:
                    brincadeira = f"Deu a chance de trabalhar numa fabrica chinesa por um salario menor que o minimo para {self.nome}" 
            print(brincadeira,f"\n{self.nome} ficou com um pouco de fome a mais")
            self.felicidade += 2
            self.fome += 1
            self.stamina -= 25

    def alimentar(self):
        if self.fome > 0:
            self.fome -= 2
            if self.fome <= 0:
                self.fome = 0
            print(f"{self.nome} foi alimentado.")
        if self.fome <= 0:
            print(f"{self.nome} está sem fome.")

    def status(self):
        print(f"Nome: {self.nome}\nFome: {self.fome}\nFelicidade: {self.felicidade}\nEnergia: {self.stamina}")            

    def botar_para_dormir(self):
        if self.fome <= 0:
            print(f"{self.nome} Fugiu pela Fome..")
            sys.exit(0)
        if self.felicidade <= 0:
            print(f"{self.nome} Fugiu pela Tristeza..")
            sys.exit(0)
        if self.fome >= 10:
            print(f"{self.nome} está com fome demais para cair no sono.")
        if self.fome < 10:
            self.stamina = 100
            self.felicidade -= 2
            print(f"{self.nome} Dormiu e recuperou suas energias")



# Testes
pet = Virtualpet("Sr. Paul")
pet.status()
pet.brincar()
pet.brincar()
pet.alimentar()
pet.alimentar()
pet.alimentar()
pet.status()
pet.botar_para_dormir()
pet.status()