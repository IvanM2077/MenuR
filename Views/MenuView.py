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

    # Botón para ver resumen del pedido
    btn_InvoiceOrderView = tk.Button(ventana, text="Agregar a la orden", command=parent.invoiceView, font=("Helvetica", 12))
    btn_InvoiceOrderView.grid(row=3, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # Botón para ver la confirmación del pedido
    btn_ConfirmView = tk.Button(ventana, text="Confirmación", command=parent.confirmView, font=("Helvetica", 12))
    btn_ConfirmView.grid(row=4, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # Botón para  ver el rechazo del pedido
    btn_RejectView = tk.Button(ventana, text="Rechazo", command=parent.rejectView, font=("Helvetica", 12))
    btn_RejectView.grid(row=5, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # Botón ver el selector de pedidos
    btn_SelectorView = tk.Button(ventana, text="pedidos", command=parent.selectorView, font=("Helvetica", 12))
    btn_SelectorView.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    ventana.pack(fill='both', expand=True)
    return ventana


