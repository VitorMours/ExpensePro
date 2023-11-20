from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from tkinter import messagebox
import json

lista_despesas = []


class LoginWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Expense PRO")
        self.minsize(400, 100)
        logo = PhotoImage(file='app/img/logo.png')
        self.iconphoto(False, logo)



        self.login_stringvar = StringVar()
        self.pass_stringvar = StringVar()

        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.main_text_font = font.Font(weight=font.BOLD, size=35)

        # Elements
        self.content_frame = ttk.Frame(self, width=826, height=400, borderwidth=5, padding=(3, 3, 12, 12))
        self.main_text = ttk.Label(self.content_frame, text="Expense PRO", font=self.main_text_font)
        self.login_frame = ttk.Frame(self.content_frame, padding=(5, 5, 5, 5))

        self.pass_entry = ttk.Entry(self.login_frame, textvariable=self.pass_stringvar)
        self.login_entry = ttk.Entry(self.login_frame, textvariable=self.login_stringvar)
        self.pass_text = ttk.Label(self.login_frame, text="Password: ")
        self.login_text = ttk.Label(self.login_frame, text="ID: ")
        self.login_button = ttk.Button(self.login_frame, text="Log In", command=self.checking)

        # Grid
        self.content_frame.grid(column=0, row=0, sticky=(N, S, W, E))
        self.main_text.grid(column=0, row=2, sticky=W)

        self.login_frame.grid(column=1, row=0, rowspan=5, sticky=(tk.N, tk.S, tk.W, tk.E))

        self.login_text.grid(column=1, row=0, sticky=tk.W)
        self.login_entry.grid(column=1, row=1)
        self.pass_text.grid(column=1, row=2, sticky=tk.W)
        self.pass_entry.grid(column=1, row=3)
        self.login_button.grid(column=1, row=4, sticky=tk.E, pady=5)

        # Resizing
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.login_frame.columnconfigure(0, weight=1)
        self.login_frame.columnconfigure(1, weight=1)
        self.login_frame.rowconfigure(1, weight=1)


    def checking(self):
        print("h1")
        print(self.login_stringvar.get())
        if self.login_stringvar.get() == '123' and self.pass_stringvar.get() == "password":
            self.destroy()
            self.main_app = MainWindow()
        elif self.login_stringvar.get() == "admin" and self.pass_stringvar.get() == "admin":
            self.destroy()
            self.admin_app = AdminWindow()



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Pro")
        logo = PhotoImage(file='app/img/logo.png')
        self.iconphoto(False, logo)




        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.main_text_font = font.Font(weight=font.BOLD, size=35)

        self.content_frame = ttk.Frame(self, width=300, borderwidth=5, padding=(3, 3, 12, 12))
        self.head_text = ttk.Label(self.content_frame, text="Expense Pro")
        self.registrar = ttk.Button(self.content_frame, text="Registrar Despesa", command=self.registro)
        self.atualizar = ttk.Button(self.content_frame, text="Atualizar Despesa", command=self.modificar)
        self.ler = ttk.Button(self.content_frame, text="Ler e Revisar Despesas", command=self.ler)
        self.excluir = ttk.Button(self.content_frame, text="Excluir Despesa", command=self.modificar)
        self.logout = ttk.Button(self.content_frame, text="Log Out", command=self.destroy)

        #self.img = ImageTk.PhotoImage(Image.open("app/img/login_person.svg"))
        #self.person = PhotoImage(self.content_frame, image=self.img)

        # Grid
        self.content_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.head_text.grid(column=0, row=0)
        self.registrar.grid(column=0, row=1, sticky=(E, W))
        self.atualizar.grid(column=0, row=2, sticky=(E, W))
        self.ler.grid(column=0, row=3, sticky=(E, W))
        self.excluir.grid(column=0, row=4, sticky=(E, W))
        self.logout.grid(column=0, row=5, sticky=(E, W))
        self.columnconfigure(0, weight=1)

    def registro(self):
        self.withdraw()
        registro = RegisterWindow()
        registro.wait_window()
        self.deiconify()

    def ler(self):
        self.withdraw()
        ler = ReadWindow()
        ler.wait_window()
        self.deiconify()

    def modificar(self):
        self.withdraw()
        modificar = ModifyWindow("modificção")
        modificar.wait_window()
        self.deiconify()

    def deletar(self):
        self.withdraw()
        modificar = ModifyWindow("deleção")
        modificar.wait_window()
        self.deiconify()


class RegisterWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Expense Pro")
        logo = PhotoImage(file='app/img/logo.png')




        self.data_stringvar = StringVar()
        self.tipo_stringvar = StringVar()
        self.descricao_stringvar = StringVar()
        self.registro_stringvar = IntVar()
        self.empresa_stringvar = StringVar()
        self.peso_stringvar = DoubleVar()
        self.valor_stringvar = DoubleVar()

        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.main_text_font = font.Font(weight=font.BOLD, size=35)


        self.content_frame = ttk.Frame(self, width=300, borderwidth=5, padding=(3, 3, 12, 12))
        self.head_text = ttk.Label(self.content_frame, text="Expense Pro")

        self.data_text = ttk.Label(self.content_frame, text="Data: ")
        self.data_entry = Text(self.content_frame, width=10, height=1)

        self.tipo_text = ttk.Label(self.content_frame, text="Tipo de registro: ")
        self.tipo_entry = Text(self.content_frame, width=10, height=1)

        self.descricao_text = ttk.Label(self.content_frame, text="Descrição da despesa: ")
        self.descricao_entry = Text(self.content_frame, width=10, height=5)

        self.registro_text = ttk.Label(self.content_frame, text="Numero de registro: ")
        self.registro_entry = Text(self.content_frame, width=10, height=1)

        self.empresa_text = ttk.Label(self.content_frame, text="Empresa da despesa: ")
        self.empresa_entry = Text(self.content_frame, width=10, height=1)

        self.peso_text = ttk.Label(self.content_frame, text="Peso da despesa: ")
        self.peso_entry = Text(self.content_frame, width=10, height=1)

        self.valor_text = ttk.Label(self.content_frame, text="Valor da despesa ")
        self.valor_entry = Text(self.content_frame, width=10, height=1)

        self.voltar_button = ttk.Button(self.content_frame, text="Voltar", command=self.voltar)
        self.registrar_button = ttk.Button(self.content_frame, text="Registrar", command=self.registrar_despesa)

        self.content_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.head_text.grid(column=0, row=0, sticky=tk.W)
        self.data_text.grid(column=0, row=1, sticky=tk.W)
        self.data_entry.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))
        self.tipo_text.grid(column=0, row=3, sticky=tk.W)
        self.tipo_entry.grid(column=0, row=4, columnspan=2, sticky=(tk.W, tk.E))
        self.descricao_text.grid(column=0, row=5, sticky=tk.W)
        self.descricao_entry.grid(column=0, row=6, columnspan=2, sticky=(tk.W, tk.E))
        self.registro_text.grid(column=0, row=7)
        self.registro_entry.grid(column=0, row=8)
        self.empresa_text.grid(column=1, row=7)
        self.empresa_entry.grid(column=1, row=8)
        self.valor_text.grid(column=0, row=9)
        self.valor_entry.grid(column=0, row=10)
        self.peso_text.grid(column=1, row=9)
        self.peso_entry.grid(column=1, row=10)

        self.voltar_button.grid(column=0, row=11)
        self.registrar_button.grid(column=1, row=11)

    def registrar_despesa(self, event=None):
        global lista_despesas
        print(f"dasds{self.data_stringvar.get()}")
        print(self.data_stringvar)
        despesa = {
            "data": self.data_entry.get(1.0, "end-1c"),
            "tipo": self.tipo_entry.get(1.0, "end-1c"),
            "descricao": self.descricao_entry.get(1.0, "end-1c"),
            "registro": self.registro_entry.get(1.0, "end-1c"),
            "empresa": self.empresa_entry.get(1.0, "end-1c"),
            "peso": self.peso_entry.get(1.0, "end-1c"),
            "valor": self.valor_entry.get(1.0, "end-1c"),
        }
        print(despesa)
        lista_despesas.append(despesa)
        self.destroy()

    def voltar(self):
        self.destroy()


class ReadWindow(tk.Tk):
    def __init__(self):
        global lista_despesas
        super().__init__()
        self.boxes = 2
        self.title("Expense Pro")
        logo = PhotoImage(file='app/img/logo.png')

        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.main_text_font = font.Font(weight=font.BOLD, size=35)

        self.content_frame = ttk.Frame(self, width=300, borderwidth=5, padding=(3, 3, 12, 12))
        self.head_text = ttk.Label(self.content_frame, text="Expense Pro")
        self.window_text = ttk.Label(self.content_frame, text="Despesas Mensais")

        self.voltar_button = ttk.Button(self.content_frame, text="Voltar", command=self.destroy)
        self.despesas = Listbox(self.content_frame, listvariable=StringVar(value=lista_despesas))


        self.content_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.head_text.grid(column=0, row=0, sticky=tk.W)
        self.window_text.grid(column=0, row=1)
        print(lista_despesas)

        for gastos in lista_despesas:
            self.information_string_builder = ""
            for k, v in gastos.items():
                self.information_string_builder += f"{k}: {v}\n"

            self.compra = ttk.Label(self.content_frame, text=f"{self.information_string_builder}\n----------------------")
            self.compra.grid(column=0, row=self.boxes)
            self.boxes += 1

        self.voltar_button.grid(column=0, row=self.boxes+1)

""


class ModifyWindow(tk.Tk):
    def __init__(self, escolha):
        self.boxes = 2
        self.escolha = escolha
        super().__init__()
        self.title("Expense Pro")
        global lista_despesas
        #logo = PhotoImage(file='app/img/logo.png')
        #self.iconphoto(False, logo)


        self.busca_registro = tk.IntVar()

        self.DefaultFont = font.nametofont("TkDefaultFont")
        self.TextFont = font.Font(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.DefaultFont.configure(family="@Microsoft JhengHei UI", weight=font.BOLD)
        self.main_text_font = font.Font(weight=font.BOLD, size=35)

        self.content_frame = ttk.Frame(self, width=300, borderwidth=5, padding=(3, 3, 12, 12))
        self.head_text = ttk.Label(self.content_frame, text="Expense Pro")

        self.text = ttk.Label(self.content_frame, text="Buscar Despesas")
        self.busca = ttk.Entry(self.content_frame, textvariable=self.busca_registro)
        self.lista_busca = Listbox(self.content_frame, listvariable=StringVar(value=lista_despesas), height=1)
        self.busca_button = ttk.Button(self.content_frame, text="Buscar", command=self.buscar)
        self.voltar_button = ttk.Button(self.content_frame, text="Voltar", command=self.voltar)
        self.solicitar_button = ttk.Button(self.content_frame, text="Solicitar", command=self.solicitar)

        for gastos in lista_despesas:

            self.information_string_builder = ""
            for k, v in gastos.items():
                self.information_string_builder += f"{k}: {v}\n"

            self.compra = ttk.Label(self.lista_busca, text=f"{self.information_string_builder}\n----------------------")
            self.compra.grid(column=0, row=self.boxes)
            self.boxes += 1
            self.scrollbar = ttk.Scrollbar(
                self,
                orient=tk.VERTICAL,
                command=self.lista_busca.yview
            )

            self.lista_busca['yscrollcommand'] = self.scrollbar.set

        # Grid
        self.content_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.head_text.grid(column=0, row=0, sticky=tk.W)
        self.busca.grid(column=0, row=1, sticky=(tk.W, tk.E))
        self.busca_button.grid(column=1, row=1, sticky=(tk.W, tk.E))
        self.lista_busca.grid(column=0, row=2, columnspan=2, sticky=(tk.W, tk.E))
        self.solicitar_button.grid(column=1, row=3)
        self.voltar_button.grid(column=0, row=3)
        self.scrollbar.grid(column=2, row=0, rowspan=2, sticky=(tk.N, tk.S))
        self.lista_busca.bind('<<ListboxSelect>>', lambda x: self.show())


    def voltar(self):
        self.destroy()

    def solicitar(self):
        self.destroy()
        messagebox.showinfo("Expense Pro", f"Processo de {self.escolha} solicitado!")

    def buscar(self):
        global lista_despesas
        lista = []
        valores = StringVar()
        for registro in lista_despesas:
            chave = registro["registro"]
            print(f"{chave} -> {self.busca_registro.get()}")

            if registro["registro"] == self.busca_registro.get():
                self.lista_busca.delete(registro)

                lista.append(registro)

                self.lista_busca.insert(registro)

    def show(self, *args):
        print("escolhido")
        self.lista_busca.curselection()




class AdminWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Pro")