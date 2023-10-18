import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

#-----------------VENTANA----------------
# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema Venta de Pasajes")
ventana.geometry("600x400")

# Datos del pasajero
datos_pasajero = {}

# Información de los asientos
asientos_primera_clase = {"clase": "Primera Clase", "precio": 200000, "disponibles": list(range(1, 15))}
asientos_clase_ejecutiva = {"clase": "Clase Ejecutiva", "precio": 150000, "disponibles": list(range(15, 29))}
asientos_clase_turistica = {"clase": "Clase turística o económica", "precio": 100000, "disponibles": list(range(29, 50))}

asientos = [asientos_primera_clase, asientos_clase_ejecutiva, asientos_clase_turistica]

#----------------INGRESAR DATOS DEL PASAJERO--------------
def ingresar_pasajero():
    # Crear una nueva ventana para ingresar los datos del pasajero
    dialogo = tk.Toplevel(ventana)
    dialogo.title("Ingresar Pasajero")

    # Campos de entrada
    campos = ["RUN", "Nombre", "Apellidos", "Celular", "Correo electrónico"]
    for i, campo in enumerate(campos):
        tk.Label(dialogo, text=campo).grid(row=i, column=0)
        datos_pasajero[campo] = tk.Entry(dialogo)
        datos_pasajero[campo].grid(row=i, column=1)

    # Botón para guardar los datos
    def guardar_datos():
        for campo in campos:
            datos_pasajero[campo] = datos_pasajero[campo].get()
        dialogo.destroy()
        messagebox.showinfo("Éxito", "Cliente ingresado con éxito")

    tk.Button(dialogo, text="Guardar", command=guardar_datos).grid(row=len(campos), column=0, columnspan=2)

#-----------------COMPRAR PASAJE--------------
def comprar_pasaje():
   # Crear una nueva ventana para comprar pasaje
    dialogo = tk.Toplevel(ventana)
    dialogo.title("Comprar Pasaje")

    # Campos de entrada
     # Campos de entrada
    campos = ["Asiento", "Es cliente frecuente (s/n)"]
    entradas = {}
    for i, campo in enumerate(campos):
        tk.Label(dialogo, text=campo).grid(row=i+2, column=0)  # Ajustamos las filas sumando 2
        entradas[campo] = tk.Entry(dialogo)
        entradas[campo].grid(row=i+2, column=1)  # Ajustamos las filas sumando 2

    # ComboBox para el destino
    tk.Label(dialogo, text="Destino").grid(row=0, column=0)
    destino = ttk.Combobox(dialogo, values=["Elija una Opción", "Iquique", "Santiago", "Punta Arenas"])
    destino.grid(row=0, column=1)
    destino.current(0)  # Establecemos "Elija una Opción" como la opción seleccionada por defecto

    # ComboBox para el horario
    tk.Label(dialogo, text="Horario").grid(row=1, column=0)
    horario = ttk.Combobox(dialogo, values=["Elija una Opción", "06:00", "10:00", "14:00", "18:00", "22:00"])
    horario.grid(row=1, column=1)
    horario.current(0)  # Establecemos "Elija una Opción" como la opción seleccionada por defecto

    # ComboBox para la forma de pago
    tk.Label(dialogo, text="Forma de Pago").grid(row=len(campos)+2, column=0)
    forma_pago = ttk.Combobox(dialogo, values=["", "Debito", "Credito"])
    forma_pago.grid(row=len(campos)+2, column=1)

    # ComboBox para las cuotas
    tk.Label(dialogo, text="Cuotas").grid(row=len(campos)+3, column=0)
    cuotas = ttk.Combobox(dialogo, values=["", "3", "6"])
    cuotas.grid(row=len(campos)+3, column=1)

    def actualizar_cuotas(event):
        # Si la forma de pago es "Debito", deshabilitamos el ComboBox de cuotas
        if forma_pago.get() == "Debito":
            cuotas.set("")  # Limpiamos cualquier valor seleccionado
            cuotas.config(state="disabled")  # Deshabilitamos el ComboBox
        else:
            cuotas.config(state="normal")  # Habilitamos el ComboBox

    # Llamamos a la función actualizar_cuotas cada vez que se selecciona una opción en el ComboBox de forma de pago
    forma_pago.bind("<<ComboboxSelected>>", actualizar_cuotas)

    # Botón para comprar pasaje
    def comprar():
        destino = entradas["Destino"].get()
        horario = entradas["Horario"].get()
        asiento = int(entradas["Asiento"].get())
        es_cliente_frecuente = entradas["Es cliente frecuente (s/n)"].get().lower() == "s"

        # Aquí puedes agregar la lógica para verificar la disponibilidad del asiento y calcular el precio

        dialogo.destroy()

    tk.Button(dialogo, text="Comprar", command=comprar).grid(row=len(campos)+2, column=0, columnspan=2)

#--------------------ANULAR PASAJE------------------
def anular_pasaje():
    # Crear una nueva ventana para anular pasaje
    dialogo = tk.Toplevel(ventana)
    dialogo.title("Anular Pasaje")

    # Campos de entrada
    campos = ["RUN", "Destino", "Horario"]
    entradas = {}
    for i, campo in enumerate(campos):
        tk.Label(dialogo, text=campo).grid(row=i, column=0)
        entradas[campo] = tk.Entry(dialogo)
        entradas[campo].grid(row=i, column=1)

    # Botón para anular pasaje
    def anular():
        run = entradas["RUN"].get()
        destino = entradas["Destino"].get()
        horario = entradas["Horario"].get()

        # Aquí puedes agregar la lógica para verificar la información del pasajero y anular el pasaje

        dialogo.destroy()

    tk.Button(dialogo, text="Anular", command=anular).grid(row=len(campos), column=0, columnspan=2)

#------------------ ASIENTOS DISPONIBLES--------------
def asientos_disponibles():
    # Crear una nueva ventana para mostrar los asientos disponibles
    dialogo = tk.Toplevel(ventana)
    dialogo.title("Asientos Disponibles")

    # Mostrar los asientos disponibles
    for info in asientos:
        tk.Label(dialogo, text=info["clase"]).grid(column=0, columnspan=7)
        for i, asiento in enumerate(info["disponibles"], start=1):
            tk.Label(dialogo, text=str(asiento)).grid(row=(i-1)//7 + 1, column=(i-1)%7)

#----------------- SALIR ----------------
# Botón para salir de la aplicación
def salir():
    ventana.destroy()

#------------------BOTONES----------------
# Botones de menú
boton1 = tk.Button(ventana, text="Ingresar Pasajero", command=ingresar_pasajero)
boton1.grid(row=0, column=0)  
boton2 = tk.Button(ventana, text="Comprar Pasaje", command=comprar_pasaje)
boton2.grid(row=1, column=0)
boton3 = tk.Button(ventana, text="Anular Pasaje", command=anular_pasaje)
boton3.grid(row=2, column=0)
boton4 = tk.Button(ventana, text="Asientos Disponibles", command=asientos_disponibles)
boton4.grid(row=3, column=0)
boton5 = tk.Button(ventana, text="Salir", command=salir)
boton5.grid(row=4, column=0)

# Mostrar ventana 
ventana.mainloop()