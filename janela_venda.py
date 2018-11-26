from tkinter import *
from tkinter import messagebox


class Janela_Venda(Toplevel):
    def __init__(self, parent, control, carro):
        super().__init__(parent)
        self.carro = carro
        self.control = control
        self.title(f'Venda - {self.carro.get_placa()}')
        self.geometry('400x200+200+200')
        self.transient(parent)
        self.grab_set()
