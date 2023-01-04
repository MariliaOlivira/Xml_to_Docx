# este é o front
# Biblioteca necessaria para a construcao da interface.
from tkinter import *
from tkinter import filedialog as dlg
from tkinter import *
from tkinter import messagebox

def compactar():
    arquivo_loc = dlg.askopenfilename(title="select a file", filetypes=(
        ("xml files", "*.xml"), ("All files", "*")))

    try:
        messagebox.showinfo(
            title="Oi", message="tudo bom?")
    except:
        messagebox.showerror(title="Error", message="Ops, algo deu errado!")
    else:
        messagebox.showinfo(
            title="Sucesso", message="Eita que tu é brabo msm!")


# Inicializacao da tela principal.
Tela_principal = Tk()

# Formatacao do título que aparece no canto superior esquerdo da tela.
Tela_principal.title("XML-TO-DOCx")

# Tamanho da tela que se adequa a imagem.
Tela_principal.geometry('340x254')

# Para evitar que minha janela se redimensione
Tela_principal.resizable(False, False)

Tela_principal["bg"] = "white"

# Botao para escolher o arquivo.
botao_compactar = Button(
    Tela_principal, text="Escolha seu aquivo",command=compactar, bg="#EE6A50").place(relx=0.5, rely=0.5, anchor=CENTER)

Tela_principal.mainloop()
