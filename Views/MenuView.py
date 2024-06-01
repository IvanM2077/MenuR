import tkinter as tk

def ReturnMenuView(parent):
    ventana = tk.Frame(parent)
    # Configuración de la vista de menú
    label = tk.Label(ventana, text="Vista de Menú")
    label.pack()
    # Crear y agregar un botón para navegar a la siguiente vista
    btn_navigate = tk.Button(ventana, text="Navegar a la siguiente vista", command=parent.menuOrderView)
    btn_navigate.pack()
    return ventana
