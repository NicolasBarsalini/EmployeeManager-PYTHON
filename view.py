import tkinter as tk
import threading
from Employee import Employee
import database_connect as db

def exit_view():
    try:
        global selected_item
        selected_item = None
        view_window.destroy()  # Try closing the preview window
    except NameError:  # if the preview window is not defined
        pass  #still running execution without doing anything

def on_click(event):
    global selected_item
    selected_item = listbox.get(listbox.curselection())
    msg_selected.config(text=f"Selecionado>> {selected_item}", font=("Arial", 16), fg="blue")

def delete(item):
    global selected_item, employees
    if item is not None:
        item = item.replace(" ", "").replace("ID:", "").replace("Nome:", "").replace("Salário:R$", "").split(",")
        id = int(item[0])
        if db.delete(id):
            msg_selected.config(text="Removido do banco de dados!", fg="green")
            selected_item = None  # update the selected item
            employees = [e for e in employees if e.getID() != id]  # removes the employee from the list
            listbox.delete(0, tk.END)  # clear the list
            for i in sorted(employees, key=lambda employee: employee.getName()):
                listbox.insert(tk.END, i.toString())  # insert the updated employees
        else:
            msg_selected.config(text="A remoção falhou!", fg="red")
    else:
        msg_selected.config(text="Selecione alguma das opções antes de remover!")

def view():
    global view_window #defines the preview window as global
    view_window = tk.Tk()
    view_window.title("View")
    view_window.geometry("600x600") #window measurement (width x height)

    scrollbar = tk.Scrollbar(view_window, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    global listbox
    listbox = tk.Listbox(view_window, yscrollcommand=scrollbar.set, font=("Arial", 16))
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)
    listbox.bind('<<ListboxSelect>>', on_click)

    global employees
    employees = []
    employees = db.select()
    employees = [Employee(row[0], row[1], row[2]) for row in employees]

    if not employees:
        listbox.insert(tk.END, "Não há nada para mostrar")
        selected_item.config(text="")
    else:
        for i in sorted(employees, key=lambda employee:employee.getName()):
            listbox.insert(tk.END, i.toString())

    listbox.pack(pady=10)

    scrollbar.config(command=listbox.yview)

    global msg_selected
    msg_selected = tk.Label(view_window, text="", font=("Arial", 16))
    msg_selected.pack(pady=20)

    exit_button = tk.Button(view_window, text="Sair", font=("Arial", 20), command=exit_view, background="red", fg="white")
    exit_button.pack(pady=15, side="left", padx=15)

    delete_button = tk.Button(view_window, text="Remover", font=("Arial", 20), command=lambda:delete(selected_item), background="blue", fg="white")
    delete_button.pack(pady=15, side="right", padx=15)

    view_window.mainloop()

if __name__ == "__main__":
    interface_thread = threading.Thread(target=view)
    interface_thread.start()
