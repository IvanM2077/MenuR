import tkinter as tk
def ReturnRejectView(parent):
    ventana = tk.Frame(parent)
    # Configuración de la vista de menú
    label = tk.Label(ventana, text="Vista de Rechazo")
    label.pack()
    return ventana