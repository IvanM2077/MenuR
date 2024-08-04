import customtkinter as ctk

def ReturnConfirmView(parent):
    ventana = ctk.CTkFrame(parent, fg_color='#426D5E')  # Color de fondo en formato hexadecimal
    # Configuración de las columnas
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de confirmación", bg_color='#596174', text_color='#FFFFFF', font=("Helvetica", 18))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    ventana.pack(fill='both', expand=True)
    return ventana
