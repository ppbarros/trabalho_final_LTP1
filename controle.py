from janela_principal_2 import Janela_Principal
from concessionária import Concessionaria
from carro import Carro
from Vendedor import Vendedor
from Comprador import Comprador
from bd_simulado import Bd_Simulado
class Controle:
    def __init__(self):
        self.jn = Janela_Principal(self)
        self.bd = Bd_Simulado()
        self.bd.carregar_carros()
        self.bd.carregar_compradores()
        self.bd.carregar_vendedores()
        self.jn.mainloop()
