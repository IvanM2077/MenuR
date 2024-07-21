import tkinter as tk
def ReturnInvoiceView(parent):
    ventana = tk.Frame(parent, bg='#303A52')  # Color de fondo en formato hexadecimal
    #Configuracion de las columnas
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    # Label de bienvenida
    lbl = tk.Label(ventana, text="Vista de Invoice", bg='#596174', bd=5, relief="solid", font=("Helvetica", 18))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    ventana.pack(fill='both', expand=True)
    return ventana