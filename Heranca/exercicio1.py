class Animal:
    def __init__(self,nome:str,especie:str):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        print(f"{self.nome} fez Soms inreconheciveis semelhantes ao do Yuri pensando")



class Cachorro(Animal):
    def __init__(self,nome:str,especie:str,raca:str):
        super().__init__(nome,especie)
        self.especie = "cachorro"
        self.raca = raca
        


    def emitir_som(self):
        print(f"{self.nome} fez Au-Au")

class Gato(Animal):
    def __init__(self,nome:str,especie:str,raca:str):
        super().__init__(nome,especie)
        self.especie = "Gato"
        self.raca = raca
        


    def emitir_som(self):
        print(f"{self.nome} fez Mew-Mew")


class Vaca(Animal):
    def __init__(self,nome:str,especie:str,raca:str):
        super().__init__(nome,especie)
        self.especie = "Vaca"
        self.raca = raca
        


    def emitir_som(self):
        print(f"{self.nome} fez Muuh")

canino = Cachorro("Jailson","Cão","Pincher")
gato = Gato("FRIEND","Gato","Ragdoll")
vaca = Vaca("Miltank","Vaca","Jersey")

canino.emitir_som()
gato.emitir_som()
vaca.emitir_som()