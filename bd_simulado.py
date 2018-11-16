import os
from concessionária import Concessionaria
from carro import Carro
class Bd_Simulado:
    def __init__(self):
        self.carros=[]

    def carregar_carros(self):
        if os.path.exists(f'{Concessionaria.get_nome()}.txt'):
            file = open(f'{Concessionaria.get_nome()}.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                carro = Carro(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              int(c[2]),
                              c[3].strip().strip('"').strip("'"),
                              float(c[4]),
                              c[5].strip().strip('"').strip("'"))
                self.carros.append(carro)
        else:
            file = open(f'{Concessionaria.get_nome()}.txt', 'w')
        file.close()