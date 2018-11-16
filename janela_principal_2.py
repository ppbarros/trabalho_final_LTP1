from tkinter import *
from tkinter import messagebox
from janela_comprador import Janela_Comprador
from janela_vendedor import Janela_Vendedor
from janela_carros import Janela_Carros
class Janela_Principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        self.title('Concessionária')
        self.geometry('500x500+200+200')
        Label(self, text='Carros').grid(row=0, column=0, pady=10, columnspan=3)

        self.btn_close = Button(self, width=10, text='Sair',
                         command=self.destroy).grid(row=2, column=0, padx=5, columnspan=3, pady=5, stick=S)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)



    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza que deseja sair?'):
            super().destroy()

    def janela_comprador(self):
        Janela_Comprador(self)

    def janela_vendedor(self):
        Janela_Vendedor(self)

    def janela_carros(self):
        Janela_Carros(self)