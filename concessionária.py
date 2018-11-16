import os
from carro import Carro
class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

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