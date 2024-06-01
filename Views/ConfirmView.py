import tkinter as tk
def ReturnConfirmView(parent):
    ventana = tk.Frame(parent)
    # Configuración de la vista de menú
    label = tk.Label(ventana, text="Vista de confirmación")
    label.pack()
    return ventana