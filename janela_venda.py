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

        Label(self, text='').grid(row=0, column=0, padx=25, pady=5)
        Label(self, text='').grid(row=2, column=0, pady=5, padx=25)
        Label(self, text='').grid(row=0, column=2, padx=10)
        self.bt_canel = Button(self, text='Cancelar', width=10, command=super().destroy).grid(row=4, column=1, pady=20)
        self.bt_confirm = Button(self, text='Confirmar', width=10).grid(row=4, column=3, pady=20)

        self.cpf_comp_entry = StringVar()
        self.cpf_comp = Entry(self, textvariable=self.cpf_comp_entry).grid(row=1, column=3)
        self.cpf_comp_lbl = Label(self, text='CPF do Comprador').grid(row=1, column=1)

        self.mat_vend_entry = StringVar()
        self.mat_vend = Entry(self, textvariable=self.mat_vend_entry).grid(column=3, row=2)
        self.mat_vend_lbl = Label(self, text='Matrícula do Vendedor').grid(row=2, column=1)

        self.preco_venda_entry = StringVar()
        self.preco_venda = Entry(self, textvariable=self.cpf_comp_entry).grid(row=3, column=3)
        self.preco_venda_lbl = Label(self, text='Preço de Venda').grid(row=3, column=1)
