from janela_principal_2 import Janela_Principal
from concessionária import Concessionaria
from carro import Carro
from Vendedor import Vendedor
from Comprador import Comprador
class Controle:
    def __init__(self):
        self.jn = Janela_Principal(self)
        self.jn.mainloop()
