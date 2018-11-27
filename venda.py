class Venda:
    def __init__(self, carro, vend, comp, preco):
        self.carro = carro
        self.vendedor = vend
        self.comprador = comp
        self.preco = preco

    def lucro(self):
        return self.preco - self.carro.get_preco()