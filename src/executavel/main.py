import tkinter as tk
from tkinter import filedialog as dlg
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title_font = ("Helvetica", 18, "bold")
        self.title("Xml-to-Docx")
        self.geometry("800x600+400+300")
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

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # create a label
        label = tk.Label(self, text="Cadastro de Empresas",
                        font=controller.title_font)
        # image = tk.PhotoImage(file="image/fundo.jpg")
        # label = tk.Label(self, image=image)
        label.pack(side="top", fill="x", pady=10)

        # create a button
        self.cnpj_label = tk.Label(self, text="CNPJ:")
        self.cnpj_entry = tk.Entry(self)
        self.endereco_label = tk.Label(self, text="Endereço:")
        self.endereco_entry = tk.Entry(self)
        self.razao_social_label = tk.Label(self, text="Razão social:")
        self.razao_social_entry = tk.Entry(self)
        self.inscricao_estadual_label = tk.Label(
            self, text="Inscrição estadual:")
        self.inscricao_estadual_entry = tk.Entry(self)
        self.cadastrar_button = tk.Button(
            self, text="Cadastrar", command=self.on_button)

        #'pack' organiza os widgets na tela
        self.cnpj_label.pack()
        self.cnpj_entry.pack()
        self.endereco_label.pack()
        self.endereco_entry.pack()
        self.razao_social_label.pack()
        self.razao_social_entry.pack()
        self.inscricao_estadual_label.pack()
        self.inscricao_estadual_entry.pack()
        self.cadastrar_button.pack()


    def on_cadastro(self):


        #pegando os dados do usuario
        cnpj = self.cnpj_entry.get()
        endereco = self.endereco_entry.get()
        razao_social = self.razao_social_entry.get()
        inscricao_estadual = self.inscricao_estadual_entry.get()

        #criando uma aqrquivo txt
        arquivo = open(f'{cnpj}.txt', 'w')

        #escrevendo os dados no arquivo
        arquivo.write(f"CNPJ: {cnpj}")
        arquivo.write(f"Endereço: {endereco}")
        arquivo.write(f"Razão social: {razao_social}")
        arquivo.write(f"Inscrição estadual: {inscricao_estadual}")

        #fechando o arquivo
        arquivo.close()

        # Cria uma mensagem
        mensagem = tk.Message(self, text=f"Tentando cadastrar empresa com CNPJ {cnpj}, endereço {endereco}, razão social {razao_social} e inscrição estadual {inscricao_estadual}")

        # Exibe a mensagem
        mensagem.pack()
        print(f"Tentando cadastrar empresa com CNPJ {cnpj}, endereço {endereco}, razão social {razao_social} e inscrição estadual {inscricao_estadual}")
    def funcao_do_botao(self):
        self.controller.show_frame("PageOne")

    def on_button(self):
        messagebox.showinfo(title="Atenção aos Dados!", message="Confirme seus dados CNPJ , endereço , razão social e inscrição estadual")
        self.on_cadastro()
        self.funcao_do_botao()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        label = tk.Label(self, text="This is page 1",
                        font=controller.title_font)
        self.cnpj_label = tk.Label(self, text="CNPJ:")
        self.cnpj_entry = tk.Entry(self)

        self.cnpj_label.pack()
        self.cnpj_entry.pack()
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Veja existe",
                            command=self.search_enterprise)
        button.pack()

    def funcao_do_botao(self, page):
        self.controller.show_frame(page)

    def search_enterprise(self):
        try:
            cnpj = self.cnpj_entry.get()
            open(f'{cnpj}.txt', 'r')
            messagebox.showinfo(title="Atenção!", message="Sua empresa foi encontrada")
            self.funcao_do_botao("PageTwo")
        except:
            messagebox.showinfo(title="Atenção!", message="Sua empresa não foi encontrada, efetue o cadastro")
            self.funcao_do_botao("StartPage")


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2",
                        font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Voltar para a página inicial",
                            command=lambda: controller.show_frame("PageOne"))
        button.pack()


app = App()
app.mainloop()

