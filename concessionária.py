import os
from carro import Carro
class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []
        if os.path.exists(f'{self.nome}.txt'):
            file = open(f'{self.nome}.txt', 'r')
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
            file = open(f'{self.nome}.txt', 'w')
        file.close()

    def get_nome(self):
        return self.nome

    def get_carros(self):
        return self.carros

    def add_carro(self, carro):
        # file = open(f'{self.nome}.txt', 'w')
        self.carros.append(carro)
        # file.writelines(str(self.carros) + '\n')
        # file.close()

    def save_cars(self):
        file = open(f'{self.nome}.txt', 'w')
        for c in self.carros:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()