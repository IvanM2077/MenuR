import customtkinter as ctk


def ReturnMenuView(parent, session):
    ventana = ctk.CTkFrame(parent, fg_color='#41436A')

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    Name = session.user.FirstName

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text=f"Menú Opciones Bienvenido {Name}", bg_color='#C56C86', text_color='#FFFFFF',
                       font=("Helvetica", 18))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Botones (algunos comentados)
    # btn_MenuOrderView = ctk.CTkButton(ventana, text="Tomar Orden", command=parent.menuOrderView, font=("Helvetica", 12))
    # btn_MenuOrderView.grid(row=2, column=1, columnspan=6, padx=10, pady=20, sticky='ew')

    btn_InvoiceOrderView = ctk.CTkButton(ventana, text="Agregar a la orden", command=parent.invoiceView,
                                         font=("Helvetica", 12))
    btn_InvoiceOrderView.grid(row=3, column=1, columnspan=6, padx=10, pady=20, sticky='ew')

    # Botones (algunos comentados)
    # btn_ConfirmView = ctk.CTkButton(ventana, text="Confirmación", command=parent.confirmView, font=("Helvetica", 12))
    # btn_ConfirmView.grid(row=4, column=1, columnspan=6, padx=10, pady=20, sticky='ew')

    # btn_RejectView = ctk.CTkButton(ventana, text="Rechazo", command=parent.rejectView, font=("Helvetica", 12))
    # btn_RejectView.grid(row=5, column=1, columnspan=6, padx=10, pady=20, sticky='ew')

    btn_SelectorView = ctk.CTkButton(ventana, text="Pedidos", command=parent.selectorView, font=("Helvetica", 12))
    btn_SelectorView.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='ew')

    print(session.user.Email)
    ventana.pack(fill='both', expand=True)
    return ventana

