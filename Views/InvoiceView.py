import tkinter as tk
def ReturnInvoiceView(parent):
    ventana = tk.Frame(parent)
    # Configuración de la vista de menú
    label = tk.Label(ventana, text="Vista de Invoice")
    label.pack()
    return ventana