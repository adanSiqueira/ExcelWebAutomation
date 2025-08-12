import customtkinter as ctk
from tkinter import filedialog, messagebox
from automator import main

arquivo = None  

def selecionar_arquivo():
    global arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    if caminho_arquivo:
        arquivo = caminho_arquivo  # salva na variável
        entrada_arquivo.delete(0, ctk.END)  # limpa campo de texto
        entrada_arquivo.insert(0, arquivo)  # mostra no campo

def incluir_no_sistema():
    if not arquivo:
        messagebox.showwarning("Aviso", "Selecione um arquivo antes de continuar.")
        return

    sucesso = main(arquivo)
    if sucesso:
        messagebox.showinfo("Sucesso", "Registros incluídos com sucesso!")
    else:
        messagebox.showerror("Erro", "Ocorreu um erro durante a inclusão.")

# Configurações da aparência
ctk.set_appearance_mode('dark')

# Janela principal
app = ctk.CTk()
app.title('System Inclusion Automator')
app.geometry('500x300')

# Label
campo_arquivo = ctk.CTkLabel(
    app,
    text='Arquivo Excel:',
    font=("Arial", 14, "bold") 
)
campo_arquivo.pack(pady=(10, 0), padx=15, anchor="w")  # Margem à esquerda

# Campo de entrada para mostrar o caminho do arquivo
entrada_arquivo = ctk.CTkEntry(app, width=350)
entrada_arquivo.pack(pady=5, padx=15, anchor="w")  # Margem à esquerda

# Botão para abrir o explorador de arquivos
botao_carregar = ctk.CTkButton(app, text="Selecionar Arquivo", command=selecionar_arquivo)
botao_carregar.pack(pady=5, padx=15, anchor="w")  # Margem à esquerda

botao_incluir = ctk.CTkButton(app, text="Incluir no sistema", command = incluir_no_sistema)
botao_incluir.pack()

app.mainloop()