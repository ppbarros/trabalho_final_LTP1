from tkinter import *
from Vendedor import Vendedor
from tkinter import messagebox
class Janela_Vendedor(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Vendedor')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()
        self.btn_add = Button(self, text='Adicionar Vendedor', command=self.add_vend).grid(row=3, columnspan=2)
        self.btn_close = Button(self, text='Sair', command=super().destroy, width=10)
        self.btn_close.grid(row=4, column=0, columnspan=2, stick=S)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).grid(row=0, column=1, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome').grid(row=0, column=0, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var).grid(row=1, column=1, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF').grid(row=1, column=0, padx=1, pady=1)

        self.entry_mat_var = StringVar()
        self.entry_mat = Entry(self, textvariable=self.entry_mat_var).grid(row=2, column=1, padx=1, pady=1)
        self.lbl_mat = Label(self, text='Matrícula').grid(row=2, column=0, padx=1, pady=1)


    def add_vend(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        matricula = self.entry_mat_var.get()
        v = Vendedor(nome, cpf, matricula)
        self.control.bd.add_vendedor(v)
        messagebox.showinfo('Vendedor', f'{nome} foi adicionado.')