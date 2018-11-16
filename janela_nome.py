from tkinter import *
class Janela_Nome(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.nome = None
        self.geometry('200x200+200+200')
        self.transient(parent)
        self.grab_set()
        self.entry = Entry(self).grid(row=0, column=1)
        Label(self, text='Digite o nome da Concessionária:').grid(row=0, column=1)
        self.btn_ok = Button(self, text='OK', width=10,
                             command=self.ok_click).grid(row=1, column=0, columnspan=2)

    def ok_click(self):
        self.nome = self.entry.get()

    def get_nome(self):
        return self.nome