import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title_font = ("Helvetica", 18, "bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Go to Page One", command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        button2 = tk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

app = App()
app.mainloop()















# # este é o front
# # Biblioteca necessaria para a construcao da interface.
# # from tkinter import *
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog as dlg
# # from tkinter import *
# from tkinter import messagebox


# def compactar():
#     arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(
#         ("xml files", "*.xml"), ("All files", "*")))

#     try:
#         messagebox.showinfo(
#             title="Oi", message="tudo bom?")
#     except:
#         messagebox.showerror(title="Error", message="Ops, algo deu errado!")
#     else:
#         messagebox.showinfo(
#             title="Sucesso", message="Eita que tu é brabo msm!")

# class App(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Páginas no Tkinter")
#         self.geometry("800x600+400+300")  # Defina o tamanho e a posição da janela

#         # Crie o widget Notebook
#         self.notebook = ttk.Notebook(self)

#         # Crie as páginas
#         self.page1 = Frame(self.notebook)
#         self.page2 = Frame(self.notebook)

#         # Adicione widgets à primeira página
#         Label(self.page1, text="Página 1").pack()
#         Button(self.page1, text="Ir para a página 2", command=self.on_button_clicked).pack()

#         # Adicione widgets à segunda página
#         Label(self.page2, text="Página 2").pack()
#         Button(self.page2, text="Ir para a página 1", command=self.on_button_clicked).pack()

#         # Adicione as páginas ao Notebook
#         self.notebook.add(self.page1, text="Página 1")
#         self.notebook.add(self.page2, text="Página 2")

#         # Adicione o Notebook à janela
#         self.notebook.pack()

#     def on_button_clicked(self):
#         # Esconda a página atual
#         current_page = self.notebook.select()
#         current_page.pack_forget()
#         # Exiba a próxima página
#         next_page = self.notebook.next()
#         next_page.pack()

# app = App()
# app.mainloop()


# class App(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Xml-to-docx")
#         self.geometry("800x600+400+300")
#         # Crie o widget Notebook
#         self.notebook = ttk.Notebook(self)

#         # Criando páginas
#         self.page1 = Frame(self.notebook)
#         self.page2 = Frame(self.notebook)

#         # Paginas adiconadas
#         self.notebook.add(self.page1, text="Cadastre a primeira empresa")
#         self.notebook.add(self.page2, text="Alguma coisa mais que eu n sei")

#         # widgets às páginas
#         Label(self.page1, text="Pagina Utilizada para o cadastro de empresas").pack()
#         Button(self.page1, text="Escolha seu aquivo",
#                command=compactar, bg="#EE6A50").pack()
#         Button(self.page1, text="Ir para a página 2",
#                command=self.on_button_clicked).pack()

#         # o Notebook à janela
#         self.notebook.pack()

#     def on_button_clicked(self):
#         # Esconda a primeira página
#         self.page1.pack_forget()
#         # Exiba a segunda página
#         self.page2.pack()


app = App()
app.mainloop()

