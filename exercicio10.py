class OrdemdeServico:
    total_os_criadas = 0
    total_os_abertas = 0

    def __init__(self, cliente, descricao):
        self.cliente = cliente
        self.descricao = descricao
        self.status = "Aberta"
        OrdemdeServico.total_os_criadas += 1
        OrdemdeServico.total_os_abertas += 1
        self.id_os = OrdemdeServico.total_os_criadas

    def ler_ordem(self):
        print(f"|ID: {self.id_os}|Cliente: {self.cliente}|Descrição: {self.descricao}|Status: {self.status}|")

    def finalizar_os(self):
        if self.status == "Aberta":
            self.status = "Finalizada"
            OrdemdeServico.total_os_abertas -= 1
        else:
            print("A ordem de serviço já está finalizada.")

    def verificar_abertas():
        print(OrdemdeServico.total_os_abertas)

ordem_1 = OrdemdeServico("Roberto Carlos Johnson da Silva Limoeiro Becker", "Quero Robux")
ordem_2 = OrdemdeServico("Yuri Davi Nascimento", "Compra Bobbie Goods")
ordem_3 = OrdemdeServico("Dave Doidão", "Compre uma espingarda pra mim porfavor")

ordem_1.ler_ordem()
ordem_2.ler_ordem()
ordem_3.ler_ordem()

OrdemdeServico.verificar_abertas()

ordem_1.finalizar_os()
ordem_3.finalizar_os()

ordem_1.ler_ordem()
ordem_2.ler_ordem()
ordem_3.ler_ordem()

OrdemdeServico.verificar_abertas()