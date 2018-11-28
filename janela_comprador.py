from tkinter import *
from Comprador import Comprador
from tkinter import messagebox


class Janela_Comprador(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Comprador')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)
        Label(self, text='').grid(row=6, column=0, padx=40, pady=30)

        self.btn_add = Button(self, text='Adicionar Comprador', command=self.add_comp). \
            grid(row=4, column=1, columnspan=3, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover Comprador', command=self.rmv_vend). \
            grid(row=7, column=1, columnspan=3, pady=10, stick=S)
        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=8, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var). \
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome'). \
            grid(row=1, column=1, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var). \
            grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF'). \
            grid(row=2, column=1, padx=1, pady=1)

        self.entry_cpf_var2 = StringVar()
        self.entry_cpf2 = Entry(self, textvariable=self.entry_cpf_var2). \
            grid(row=6, column=3, padx=1, pady=1, stick=S)
        self.lbl_cpf2 = Label(self, text='CPF'). \
            grid(row=6, column=1, padx=1, pady=1, stick=S)

    def add_comp(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        c = Comprador(nome, cpf)
        self.control.bd.add_comprador(c)
        messagebox.showinfo('Comprador', f'{nome} foi adicionado.')

    def rmv_vend(self):
        cpf = self.entry_cpf_var2.get()
        rmvd = None
        for comp in self.control.bd.show_comp():
            if cpf == comp.get_cpf():
                if messagebox.askyesno\
                            ('Excluir', f'Tem ceteza que deseja excluir o comprador {comp.get_nome()}?') is False:
                    return None
                rmvd = self.control.bd.rmv_comp(comp)
                messagebox.showinfo('Comprador', f'{comp.get_nome()} foi removido.')
        if rmvd is None:
            messagebox.showerror('Comprador', 'Não há comprador cadastrado com este CPF')

    def destroy(self):
        self.control.bd.save_comprador()
        super().destroy()
