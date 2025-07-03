import tkinter as tk
from tkinter import messagebox
from clientes import cadastrar_cliente

def cadastrar_cliente_gui():
    cadastro_janela = tk.Toplevel(janela)
    cadastro_janela.title("Cadastrar Cliente")
    cadastro_janela.geometry("350x300")
    cadastro_janela.resizable(False, False)

    # Campos do formulário
    tk.Label(cadastro_janela, text="Nome:").pack()
    nome_entry = tk.Entry(cadastro_janela, width=40)
    nome_entry.pack()

    tk.Label(cadastro_janela, text="Nascimento (dd/mm/aaaa):").pack()
    nasc_entry = tk.Entry(cadastro_janela, width=40)
    nasc_entry.pack()

    tk.Label(cadastro_janela, text="CPF (somente números):").pack()
    cpf_entry = tk.Entry(cadastro_janela, width=40)
    cpf_entry.pack()

    tk.Label(cadastro_janela, text="Endereço:").pack()
    end_entry = tk.Entry(cadastro_janela, width=40)
    end_entry.pack()

    def enviar():
        nome = nome_entry.get().strip()
        nascimento = nasc_entry.get().strip()
        cpf = cpf_entry.get().strip()
        endereco = end_entry.get().strip()

        if not all([nome, nascimento, cpf, endereco]):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        cadastrar_cliente(nome, nascimento, cpf, endereco)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        cadastro_janela.destroy()

    tk.Button(cadastro_janela, text="Cadastrar", command=enviar).pack(pady=10)
 
def criar_conta():
    messagebox.showinfo("Criar Conta", "Ainda não criado.")

def selecionar_conta():
    messagebox.showinfo("Selecionar Conta", "Ainda não criado.")

def sair():
    janela.quit()


janela = tk.Tk()
janela.title("🏦 Sistema Bancário")
janela.geometry("350x300")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Bem vindo ao banco do Tiago", font=("Helvetica", 16, "bold"))
titulo.pack(pady=20)

btn_cadastrar = tk.Button(janela, text="📋 Cadastrar Conta", width=25, command=cadastrar_cliente_gui)
btn_cadastrar.pack(pady=5)

btn_criar = tk.Button(janela, text="🏦 Criar Conta", width=25, command=criar_conta)
btn_criar.pack(pady=5)

btn_selecionar = tk.Button(janela, text="🔐 Selecionar Conta", width=25, command=selecionar_conta)
btn_selecionar.pack(pady=5)

btn_sair = tk.Button(janela, text="🚪Sair", width=25, command=sair)
btn_sair.pack(pady=20)

janela.mainloop()