from tkinter import *
class Janela_Vendedor(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Vendedor')
        self.geometry('200x200+200+200')
        self.transient(parent)
        self.grab_set()
        self.btn_close = Button(self, text='Sair', command=super().destroy, width=10)
        self.btn_close.grid(stick=S)