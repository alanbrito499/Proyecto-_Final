import tkinter as tk
from tkinter import ttk, messagebox

class Empleado:
    def __init__(self, nss, curp, genero, num_control, turno, area):
        self.nss = nss
        self.curp = curp
        self.genero = genero
        self.num_control = num_control
        self.turno = turno
        self.area = area

empleados = {}

def registrar_empleado():
    nss = entry_nss.get()
    curp = entry_curp.get()
    genero = combo_genero.get()
    num_control = entry_num_control.get()
    turno = combo_turno.get()
    area = entry_area.get()
    if nss and curp and genero and num_control and turno and area:
        if nss in empleados:
            messagebox.showerror("Error", "Empleado ya registrado.")
            return
        empleados[nss] = Empleado(nss, curp, genero, num_control, turno, area)
        messagebox.showinfo("Éxito", "Empleado registrado.")
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def limpiar_campos():
    entry_nss.delete(0, tk.END)
    entry_curp.delete(0, tk.END)
    combo_genero.set('')
    entry_num_control.delete(0, tk.END)
    combo_turno.set('')
    entry_area.delete(0, tk.END)

root = tk.Tk()
root.title("Registro de Empleado")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="NSS:").grid(row=0, column=0)
entry_nss = tk.Entry(frame)
entry_nss.grid(row=0, column=1)

tk.Label(frame, text="CURP:").grid(row=1, column=0)
entry_curp = tk.Entry(frame)
entry_curp.grid(row=1, column=1)

tk.Label(frame, text="Género:").grid(row=2, column=0)
combo_genero = ttk.Combobox(frame, values=["Masculino", "Femenino", "Otro"])
combo_genero.grid(row=2, column=1)

tk.Label(frame, text="No. Control:").grid(row=3, column=0)
entry_num_control = tk.Entry(frame)
entry_num_control.grid(row=3, column=1)

tk.Label(frame, text="Turno:").grid(row=4, column=0)
combo_turno = ttk.Combobox(frame, values=["Matutino", "Vespertino", "Nocturno"])
combo_turno.grid(row=4, column=1)

tk.Label(frame, text="Área:").grid(row=5, column=0)
entry_area = tk.Entry(frame)
entry_area.grid(row=5, column=1)

tk.Button(frame, text="Registrar Empleado", command=registrar_empleado).grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
