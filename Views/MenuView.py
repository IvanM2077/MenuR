import tkinter as tk


def ReturnMenuView(parent):
    ventana = tk.Frame(parent, bg='#41436A')

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = tk.Label(ventana, text="Menú Opciones", bg='#C56C86', bd=5, relief="solid", font=("Helvetica", 18))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Botón para tomar orden
    btn_MenuOrderView = tk.Button(ventana, text="Tomar Orden", command=parent.menuOrderView, font=("Helvetica", 12))
    btn_MenuOrderView.grid(row=2, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # Botón para tomar orden
    btn_InvoiceOrderView = tk.Button(ventana, text="Agregar a la orden", command=parent.invoiceView, font=("Helvetica", 12))
    btn_InvoiceOrderView.grid(row=2, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # Botón para nota de la orden
    btn_InvoiceView = tk.Button(ventana, text="Nota de la orden", command=parent.invoiceView, font=("Helvetica", 12))
    btn_InvoiceView.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    ventana.pack(fill='both', expand=True)
    return ventana


