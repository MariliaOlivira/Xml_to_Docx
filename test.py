import tkinter as tk

class CadastroEmpresaForm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.cnpj_label = tk.Label(self, text="CNPJ:")
        self.cnpj_entry = tk.Entry(self)
        self.endereco_label = tk.Label(self, text="Endereço:")
        self.endereco_entry = tk.Entry(self)
        self.razao_social_label = tk.Label(self, text="Razão social:")
        self.razao_social_entry = tk.Entry(self)
        self.inscricao_estadual_label = tk.Label(self, text="Inscrição estadual:")
        self.inscricao_estadual_entry = tk.Entry(self)
        self.cadastrar_button = tk.Button(self, text="Cadastrar", command=self.on_cadastro)

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
        # Aqui você pode adicionar a lógica de cadastro da empresa,
        # como verificar se os campos estão preenchidos corretamente e
        # enviar os dados para o banco de dados ou para outra fonte
        cnpj = self.cnpj_entry.get()
        endereco = self.endereco_entry.get()
        razao_social = self.razao_social_entry.get()
        inscricao_estadual = self.inscricao_estadual_entry.get()
        print(f"Tentando cadastrar empresa com CNPJ {cnpj}, endereço {endereco}, razão social {razao_social} e inscrição estadual {inscricao_estadual}")

root = tk.Tk()
form = CadastroEmpresaForm(root)
form.pack()
root.mainloop()
