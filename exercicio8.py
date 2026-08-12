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
class Virtualpet:
    def __init__(self, nome:str, fome = 5, felicidade = 5):
        self.nome = nome
        self.fome = fome
        self.felicidade = felicidade

    def brincar(self):
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
        print(brincadeira)
        if self.fome > 0:




# Testes
pet = Virtualpet("Pal")
pet.brincar()