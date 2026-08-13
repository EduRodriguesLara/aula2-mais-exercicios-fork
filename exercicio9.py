class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def comparar_tamanho(self, outro_livro):
            if self.paginas > outro_livro.paginas:
                print(f"O livro {self.titulo} possui mais paginas doque {outro_livro.titulo}.")
            elif self.paginas < outro_livro.paginas:
                print(f"O livro {outro_livro.titulo} possui mais paginas doque {self.titulo}.")
            elif self.paginas == outro_livro.paginas:
                print(f"Os dois livros possuem a mesma quantidade de paginas.")
        

    def __str__(self):
        return f"Livro: {self.titulo}, {self.paginas} paginas pelo Autor {self.autor}"


livro_1 = Livro("Demon Slayer Volume 17", "Koyoharu Gotouge", 192)
livro_2 = Livro("O Pequeno Principe", "Antoine de Saint-Exupéry", 138)

print(livro_1)
print(livro_2)
livro_1.comparar_tamanho(livro_2)
