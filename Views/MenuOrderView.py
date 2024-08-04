import customtkinter as ctk
import Models.Session

def returnMenuOrderView(parent, session, OrderId=None):
    ventana = ctk.CTkFrame(parent, fg_color='#41436A')

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de menu orden", bg_color='#C56C86', text_color='#FFFFFF', font=("Helvetica", 18))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    ventana.pack(fill='both', expand=True)

    return ventana

