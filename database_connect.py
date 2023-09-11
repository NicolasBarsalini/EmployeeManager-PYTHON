import pyodbc as p

data_connect = (
    "Driver={SQL Server};" 
    "Server=DESKTOP-LRKTNDG;" #your HOSTNAME
    "Database=PythonSQL;" #Database's name
)

conn = None
table = "Employee" #your table to insert here

def connect():
    global conn
    try:
        conn = p.connect(data_connect)
        print("Connected!")
    except Exception as e:
        print(f"Error during connection: {e}")

def connection_close():
    global conn
    if conn is not None:
        try:
            conn.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Error during connection close: {e}")
    else:
        print("You do not have any connection!")

def insert(employee_name, salary):
    global conn
    if conn is not None:
        try:
            cursor = conn.cursor()
            command = f"INSERT INTO {table} (Name, Salary) VALUES (?, ?)"
            cursor.execute(command, (employee_name, salary))
            cursor.commit()
            print("Inserted successfully!")
        except Exception as e:
            print(f"Error during insert: {e}")
    else:
        print("You must be connected to use it!")

def select():
    global conn
    if conn is not None:
        try:
            cursor = conn.cursor()
            command = f"SELECT * FROM {table}"
            cursor.execute(command)
            result = cursor.fetchall()
            # print the results here:
            return result
        except Exception as e:
            print(f"Error during SELECT: {e}")
    else:
        print("You must be connected to use it!")

def delete(employee_id):
    global conn
    if conn is not None:
        try:
            cursor = conn.cursor()
            command = f"DELETE FROM {table} WHERE EmployeeID = ?"
            cursor.execute(command, (employee_id,))
            conn.commit()  # Adicione esta linha para efetivar a exclusão
            print("Deleted successfully!")
            return True  # Indica que a exclusão foi bem-sucedida
        except Exception as e:
            print(f"Error during delete: {e}")
    else:
        print("You must be connected to use this function!")
    return False  # Indica que a exclusão falhou