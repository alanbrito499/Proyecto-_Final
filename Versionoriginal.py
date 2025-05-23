import tkinter as tk
from tkinter import ttk, messagebox

def registrar_datos():
    datos = {
        "Número de control": entry_num_control.get(),
        "Nombre": entry_nombre.get(),
        "Edad": entry_edad.get(),
        "Género": combo_genero.get(),
        "CURP": entry_curp.get(),
        "NSS": entry_nss.get(),
        "Turno": combo_turno.get()
    }
    messagebox.showinfo("Registro exitoso", "Datos registrados correctamente.")

ventana = tk.Tk()
ventana.title("Registro de Asistencia - Hospital Sante")
ventana.geometry("400x350")

tk.Label(ventana, text="Número de control:").pack(pady=5)
entry_num_control = tk.Entry(ventana)
entry_num_control.pack()

tk.Label(ventana, text="Nombre:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Género:").pack(pady=5)
combo_genero = ttk.Combobox(ventana, values=["Masculino", "Femenino", "Otro"])
combo_genero.pack()

tk.Label(ventana, text="CURP:").pack(pady=5)
entry_curp = tk.Entry(ventana)
entry_curp.pack()

tk.Label(ventana, text="Número de Seguro Social:").pack(pady=5)
entry_nss = tk.Entry(ventana)
entry_nss.pack()
tk.Label(ventana, text="Turno:").pack(pady=5)
combo_turno = ttk.Combobox(ventana, values=["matutino", "vespertino", "nocturno"])
combo_turno.pack()

tk.Button(ventana, text="Registrar", command=registrar_datos).pack(pady=20)

ventana.mainloop()