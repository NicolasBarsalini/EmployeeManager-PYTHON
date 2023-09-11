import tkinter as tk
import threading
import sys
from view import view
from filter_view import filter_view
import database_connect as db

def register():
    try:
        name = name_entry.get()
        salary = float(salary_entry.get())
        if name != None and salary != None and type(salary) == float: 
            try:
                db.insert(name, salary)
            except Exception as e:
                msg.config(text="Falha na comunicação com o banco de dados!")
            msg.config(text="Registrado com sucesso")
    except ValueError:
        msg.config(text="Valores inválidos!")

def exit():
    db.connection_close() #to close the connection
    sys.exit()

def start_tkinter():
    root = tk.Tk()
    root.title("Atom.Inc")
    root.geometry("1920x1080")  #window measurement

    name_label = tk.Label(root, text="Insira o nome do empregado:", font=("Arial", 20))
    name_label.pack(pady=15)  # vertical spacing

    global name_entry
    name_entry = tk.Entry(root, font=("Arial", 20))
    name_entry.pack(pady=15)

    salary_label = tk.Label(root, text="Insira o salário do empregado:", font=("Arial", 20))
    salary_label.pack(pady=15)  # vertical spacing
    
    global salary_entry
    salary_entry = tk.Entry(root, font=("Arial", 20))
    salary_entry.pack(pady=15)

    register_button = tk.Button(root, text="Registrar", font=("Arial", 20), command=register, background="green", fg="white")
    register_button.pack(pady=15)

    show_employees_button = tk.Button(root, text="Mostrar", font=("Arial",20), command=view, background="blue", fg="white")
    show_employees_button.pack(pady=15)

    filter_employee_button = tk.Button(root, text="Filtrar", font=("Arial",20), command=filter_view, background="purple", fg="white")
    filter_employee_button.pack(pady=15)

    exit_button = tk.Button(root, text="Sair", font=("Arial", 20), command=exit, background="red", fg="white")
    exit_button.pack(pady=15)

    global msg
    msg = tk.Label(root, text="", font=("Arial", 20))
    msg.pack(pady=15)

    exit_label = tk.Label(root, text="(Clique em sair para sair)", font=("Arial", 16))
    exit_label.pack(pady=5)
    
    root.mainloop()

db.connect() #to connect to SQL Server
interface_thread = threading.Thread(target=start_tkinter)
interface_thread.start()

