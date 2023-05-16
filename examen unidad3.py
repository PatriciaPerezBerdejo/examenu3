from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel
import tkinter.font as font
import tkinter as tk
from tkinter import ttk
import mysql.connector

#CONEXION CON EL XAMPP
conexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="estetica unisex"
)

if conexion.is_connected():
  print("Conexión exitosa a la base de datos")

cursor = conexion.cursor()
consulta = "SELECT * FROM citas"
cursor.execute(consulta)

for fila in cursor.fetchall():
  print(fila)

conexion.close()


# VALIDACION DE DATOS
def validar_datos():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "Estetica tec" and contraseña == "1234programacion":
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido de nuevo!")
        ventana.destroy()
    else:
        messagebox.showerror("Error de inicio de sesión", "Introduzca los datos correctos")

def salir():
    ventana.destroy()

def mostrar_desarrolladores():
    ventana_desarrolladores = Toplevel()
    ventana_desarrolladores.title("Desarrolladores")
    ventana_desarrolladores.geometry("300x150")

    label_titulo = Label(ventana_desarrolladores, text="Desarrolladores", font=("Dark Mono", 14, "bold"))
    label_titulo.pack(pady=10)

    label_nombres = Label(ventana_desarrolladores, text="Jonathan Raul Cruz Magaña\nJuan Josmar Bacelis de la Rosa\nPatricia Beatriz Perez Berdejo", font=("Dark Mono", 12))
    label_nombres.pack()

# VENTANA DE INICIO DE SESION
ventana = Tk()
ventana.title("Inicio de sesión")
ventana.geometry("600x400")
ventana.configure(bg="honeydew")

dark_mono_font = font.Font(family="Dark Mono")

# TITULO
label_bienvenida = Label(ventana, text="Bienvenido a nuestra estética unisex", font=(dark_mono_font, 16, "bold"), bg="honeydew")
label_bienvenida.pack(pady=15)

# INSTRUCCION POR DEBAJO DEL TITULO
label_instrucciones = Label(ventana, text="Por favor, ingrese los datos para ingresar", font=(dark_mono_font, 12), bg="honeydew")
label_instrucciones.pack()

# ENTRADAS DE USUARIO Y CONTRASEÑA
label_usuario = Label(ventana, text="Usuario", font=(dark_mono_font, 12), bg="honeydew")
label_usuario.pack(pady=10)
entry_usuario = Entry(ventana, font=(dark_mono_font, 12))
entry_usuario.pack()

label_contraseña = Label(ventana, text="Contraseña", font=(dark_mono_font, 12), bg="honeydew")
label_contraseña.pack(pady=10)
entry_contraseña = Entry(ventana, show="*", font=(dark_mono_font, 12))
entry_contraseña.pack()

# BOTON DE INICIO DE SESION
boton_ingresar = Button(ventana, text="Ingresar", command=validar_datos, font=(dark_mono_font, 12))
boton_ingresar.pack(pady=15)

# BOTON PARA SALIR
boton_salir = Button(ventana, text="Salir", command=salir, font=(dark_mono_font, 12))
boton_salir.pack(pady=5)

# BOTON PARA ENTRAR A DESARROLLADORES
boton_desarrolladores = Button(ventana, text="Desarrolladores", command=mostrar_desarrolladores, font=(dark_mono_font, 12))
boton_desarrolladores.pack(pady=5)

# EJECUCION DEL INICIO DE SESION
ventana.mainloop()

# VALIDACION DE LOS DATOS QUE DEBES DE INGRESAR
def validate_data():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    service = service_entry.get().strip()
    gender = gender_combobox.get()
    date = date_entry.get().strip()
    phone = phone_entry.get().strip()

    
    if not name or not age or not service or not gender or not date or not phone:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Error", "La edad debe ser un número entero positivo.")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "El número de teléfono debe ser un número de 10 dígitos.")
        return

    # Data is valid, add to the table
    data_table.insert("", tk.END, values=(name, age, service, gender, date, phone))
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    service_entry.delete(0, tk.END)
    gender_combobox.set("")
    date_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def delete_data():
    selected_item = data_table.selection()
    if selected_item:
        data_table.delete(selected_item)
    else:
        messagebox.showerror("Error", "Por favor, seleccione un registro para eliminar.")

# VENTANA DE CITAS
window = tk.Tk()
window.title("Registro de citas")
window.geometry("800x600")
window.configure(bg="lemon chiffon")

# LOS CAMPOS DE ENTRADASS DE TODOS LOS DATOS QUE PEDIMOS PARA AGENDAR LA CITA
name_label = tk.Label(window, text="Nombre:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Edad:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

service_label = tk.Label(window, text="Tipo de servicio:")
service_label.pack()
service_entry = tk.Entry(window)
service_entry.pack()

gender_label = tk.Label(window, text="Sexo:")
gender_label.pack()
gender_combobox = ttk.Combobox(window, values=["Masculino", "Femenino", "Otro"])
gender_combobox.pack()

date_label = tk.Label(window, text="Fecha agendada:")
date_label.pack()
date_entry = tk.Entry(window)
date_entry.pack()

phone_label = tk.Label(window, text="Teléfono:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

data_table = ttk.Treeview(window, columns=("Name", "Age", "Service", "Gender", "Date", "Phone"), show="headings")

data_table.heading("Name", text="Nombre")
data_table.heading("Age", text="Edad")
data_table.heading("Service", text="Tipo de servicio")
data_table.heading("Gender", text="Sexo")
data_table.heading("Date", text="Fecha agendada")
data_table.heading("Phone", text="Teléfono")

data_table.pack()

validate_button = tk.Button(window, text="Ingresar datos", command=validate_data)
validate_button.pack()

clear_button = tk.Button(window, text="Limpiar campos", command=clear_fields)
clear_button.pack()

delete_button = tk.Button(window, text="Eliminar datos", command=delete_data)
delete_button.pack()

# EJECUCION DE LA VENTANA FINAL
window.mainloop()