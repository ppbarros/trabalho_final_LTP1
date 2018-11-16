from tkinter import *
from tkinter import messagebox
class Janela_Principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        self.title('Concessionária')
        Label(self, text='Menu').grid(row=0, column=0, pady=10, columnspan=3)
        self.b1 = Button(self, width=10, text='Comprador').grid(row=1, column=0, padx=5)
        self.b2 = Button(self, width=10, text='Vendedor').grid(row=1, column=1, padx=5)
        self.b3 = Button(self, width=10, text='Carros').grid(row=1, column=2, padx=5)
        self.b4 = Button(self, width=10, text='Sair',
                         command=self.destroy).grid(row=2, column=0, padx=5, columnspan=3, pady=5)



    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza que deseja sair?'):
            super().destroy()
