from tkinter import *


class Janela_Nota_Venda(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Nota de Venda')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()


