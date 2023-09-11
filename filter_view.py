import tkinter as tk
from Employee import Employee
import database_connect as db

def exit_filter_view():
    try:
        filter_view_window.destroy()  # Tenta fechar a janela de visualização
    except NameError:  # Se a janela de visualização não estiver definida
        pass  # Continua a execução sem fazer nada

def find():
    if name_entry.get() != "":
        employees = db.select()
        employees = [Employee(row[0], row[1], row[2]) for row in employees]
        name = name_entry.get()
        found = False
        for i in employees:
            if i.getName() == name:
                msg_empty.config(text=i.toString())
                found = True
        if not found:
            msg_empty.config(text="Não encontrado!")

def filter_view():
    global filter_view_window  # Define a janela de visualização como global
    filter_view_window = tk.Tk()
    filter_view_window.title("Filter View")
    filter_view_window.geometry("600x600")  # Tamanho da janela (largura x altura)

    name_label = tk.Label(filter_view_window, text="Insira o nome do empregado:", font=("Arial", 16))
    name_label.pack(pady=15)  # Espaçamento vertical

    global name_entry
    name_entry = tk.Entry(filter_view_window, font=("Arial", 20))
    name_entry.pack(pady=10)

    find_button = tk.Button(filter_view_window, text="Buscar", font=("Arial", 20), command=find, background="blue", fg="white")
    find_button.pack(pady=10)

    global msg_empty
    msg_empty = tk.Label(filter_view_window, text="", font=("Arial", 16))
    msg_empty.pack(pady=15)

    exit_filter_view_button = tk.Button(filter_view_window, text="Sair", font=("Arial", 20), command=exit_filter_view, background="red", fg="white")
    exit_filter_view_button.pack(pady=10)

    exit_filter_view_label = tk.Label(filter_view_window, text="(Clique em sair para sair)", font=("Arial", 16))
    exit_filter_view_label.pack(pady=10)
    
    filter_view_window.mainloop()

if __name__ == "__main__":
    filter_view()
