from tkinter import *
from Comprador import Comprador
from tkinter import messagebox


class Janela_Comprador(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Comprador')
        self.geometry('400x200+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)

        self.btn_add = Button(self, text='Adicionar Comprador', command=self.add_comp). \
            grid(row=4, column=1, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover Comprador', command=self.rmv_vend). \
            grid(row=4, column=3, columnspan=2, pady=10, stick=S)
        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=5, column=1, columnspan=3, stick=S, pady=20)

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

    def add_comp(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        c = Comprador(nome, cpf)
        self.control.bd.add_comprador(c)
        messagebox.showinfo('Comprador', f'{nome} foi adicionado.')

    def rmv_vend(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        rmvd = None
        if messagebox.askyesno('Excluir', f'Tem ceteza que deseja excluir o vendedor {nome}?') is False:
            return None
        for c in self.control.bd.show_comp():
            if c.get_nome() == nome and c.get_cpf() == cpf:
                rmvd = self.control.bd.rmv_comp(c)
                messagebox.showinfo('Comprador', f'{nome} foi removido.')
        if rmvd is None:
            messagebox.showerror('Comprador', 'Não há vendedor cadastrado com estes dados')

    def destroy(self):
        self.control.bd.save_comprador()
        super().destroy()
