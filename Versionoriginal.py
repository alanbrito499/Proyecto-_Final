import tkinter as tk
from tkinter import ttk

def mostrar_instrucciones():
    instrucciones = (
        "Instrucciones de uso por si no me entendiste como usarlo :\n\n"
        "1. Llena los campos de NSS, CURP, Género, No. Control, Turno y Área para registrar un empleado.\n"
        "2. Use los botones para marcar tu entrada, salida, agregar horas extra, vacaciones, dias económicos, incapacidad o faltas.\n"
        "3. Los empleados con 3 retardos o 3 faltas serán suspendidos automáticamente por 1 semana.\n"
        "4. Los datos de los empleados se muestran en la tabla inferior.\n"
        "5. Creo se puede ver esta pestaña para ver las instrucciones cuando quiera"
    )
    text_instrucciones.config(state='normal')
    text_instrucciones.delete(1.0, tk.END)
    text_instrucciones.insert(tk.END, instrucciones)
    text_instrucciones.config(state='disabled')

root = tk.Tk()
root.title("Control de Asistencias")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

frame = tk.Frame(notebook)
notebook.add(frame, text="Principal")

frame_instrucciones = tk.Frame(notebook)
notebook.add(frame_instrucciones, text="Cómo usar el código")

text_instrucciones = tk.Text(frame_instrucciones, wrap='word', height=20, width=80)
text_instrucciones.pack(padx=10, pady=10, fill='both', expand=True)
mostrar_instrucciones()
from tkinter import ttk, messagebox
import datetime

class Empleado:
    def __init__(self, nss, curp, genero, num_control, turno, area):
        self.nss = nss
        self.curp = curp
        self.genero = genero
        self.num_control = num_control
        self.turno = turno
        self.area = area
        self.horas_extra = 0
        self.dias_vacacionales = 0
        self.dias_economicos = 0
        self.retardos = 0
        self.incapacitaciones = 0
        self.entradas = []
        self.salidas = []
        self.faltas = 0
        self.suspendido_hasta = None

empleados = {}

def limpiar_campos():
    entry_nss.delete(0, tk.END)
    entry_curp.delete(0, tk.END)
    combo_genero.set('')
    entry_num_control.delete(0, tk.END)
    combo_turno.set('')
    entry_area.delete(0, tk.END)

def actualizar_lista():
    for row in tree.get_children():
        tree.delete(row)
    for emp in empleados.values():
        tree.insert('', tk.END, values=(
            emp.nss, emp.curp, emp.genero, emp.num_control, emp.turno, emp.area,
            emp.horas_extra, emp.dias_vacacionales, emp.dias_economicos,
            emp.retardos, emp.incapacitaciones, emp.faltas,
            emp.entradas[-1] if emp.entradas else '',
            emp.salidas[-1] if emp.salidas else '',
            emp.suspendido_hasta.strftime('%Y-%m-%d') if emp.suspendido_hasta else ''
        ))

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
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def marcar_entrada():
    nss = entry_nss.get()
    if nss in empleados:
        emp = empleados[nss]
        hoy = datetime.date.today()
        if emp.suspendido_hasta and hoy <= emp.suspendido_hasta:
            messagebox.showwarning("Suspendido", f"Empleado suspendido hasta {emp.suspendido_hasta}")
            return
        hora = datetime.datetime.now().strftime('%H:%M')
        emp.entradas.append(hora)
    
        if hora > '09:10':
            emp.retardos += 1
            if emp.retardos % 3 == 0:
                emp.suspendido_hasta = hoy + datetime.timedelta(days=7)
                messagebox.showwarning("Suspensión", "Empleado suspendido por 1 semana por 3 retardos.")
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")

def marcar_salida():
    nss = entry_nss.get()
    if nss in empleados:
        emp = empleados[nss]
        hora = datetime.datetime.now().strftime('%H:%M')
        emp.salidas.append(hora)
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")

def agregar_horas_extra():
    nss = entry_nss.get()
    if nss in empleados:
        try:
            horas = int(entry_horas_extra.get())
            empleados[nss].horas_extra += horas
            entry_horas_extra.delete(0, tk.END)
            actualizar_lista()
        except Exception:
            messagebox.showerror("Error", "Ingrese un número válido.")
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")
def agregar_vacaciones():
    nss = entry_nss.get()
    if nss in empleados:
        try:
            dias = int(entry_vacaciones.get())
            empleados[nss].dias_vacacionales += dias
            entry_vacaciones.delete(0, tk.END)
            actualizar_lista()
        except Exception:
            messagebox.showerror("Error", "Ingrese un número válido.")
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")
def agregar_economicos():
    nss = entry_nss.get()
    if nss in empleados:
        try:
            dias = int(entry_economicos.get())
            empleados[nss].dias_economicos += dias
            entry_economicos.delete(0, tk.END)
            actualizar_lista()
        except Exception:
            messagebox.showerror("Error", "Ingrese un número válido.")
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")
def agregar_incapacidad():
    nss = entry_nss.get()
    if nss in empleados:
        try:
            dias = int(entry_incapacidad.get())
            empleados[nss].incapacitaciones += dias
            entry_incapacidad.delete(0, tk.END)
            actualizar_lista()
        except Exception:
            messagebox.showerror("Error", "Ingrese un número válido.")
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")

def agregar_falta():
    nss = entry_nss.get()
    if nss in empleados:
        emp = empleados[nss]
        emp.faltas += 1
        if emp.faltas % 3 == 0:
            emp.suspendido_hasta = datetime.date.today() + datetime.timedelta(days=7)
            messagebox.showwarning("Suspensión", "Empleado suspendido por 1 semana por 3 faltas.")
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")

# --- Interfaz gráfica ---
root = tk.Tk()
root.title("Control de Asistencias")

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
tk.Label(frame, text="Horas Extra:").grid(row=8, column=0)
entry_horas_extra = tk.Entry(frame, width=5)
entry_horas_extra.grid(row=8, column=1)
btn_horas_extra = tk.Button(frame, text="Agregar", command=agregar_horas_extra)
btn_horas_extra.grid(row=8, column=2)

tk.Label(frame, text="Vacaciones:").grid(row=9, column=0)
entry_vacaciones = tk.Entry(frame, width=5)
entry_vacaciones.grid(row=9, column=1)
btn_vacaciones = tk.Button(frame, text="Agregar", command=agregar_vacaciones)
btn_vacaciones.grid(row=9, column=2)

tk.Label(frame, text="Económicos:").grid(row=10, column=0)
entry_economicos = tk.Entry(frame, width=5)
entry_economicos.grid(row=10, column=1)
btn_economicos = tk.Button(frame, text="Agregar", command=agregar_economicos)
btn_economicos.grid(row=10, column=2)

tk.Label(frame, text="Incapacidad:").grid(row=11, column=0)
entry_incapacidad = tk.Entry(frame, width=5)
entry_incapacidad.grid(row=11, column=1)
btn_incapacidad = tk.Button(frame, text="Agregar", command=agregar_incapacidad)
btn_incapacidad.grid(row=11, column=2)
tk.Label(frame, text="Incapacidad:").grid(row=11, column=0)
entry_incapacidad = tk.Entry(frame, width=5)
entry_incapacidad.grid(row=11, column=1)
tk.Button(frame, text="Agregar", command=agregar_incapacidad).grid(row=11, column=2)

tk.Button(frame, text="Agregar Falta", command=agregar_falta).grid(row=12, column=0, columnspan=2, pady=5)

cols = [
    "NSS", "CURP", "Género", "No. Control", "Turno", "Área", "Horas Extra",
    "Vacaciones", "Económicos", "Retardos", "Incapacidad", "Faltas",
    "Últ. Entrada", "Últ. Salida", "Suspendido Hasta"
]
tree = ttk.Treeview(root, columns=cols, show='headings', height=8)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=90)
tree.pack(padx=10, pady=10)

root.mainloop()
