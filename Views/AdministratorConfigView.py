import customtkinter as ctk
import Infraestructure.ViewConfig as IV
Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()
def ReturnAdministratorView(parent, session):
    ventana = ctk.CTkFrame(parent, fg_color=f'{Bg1}')  # Color de fondo en formato hexadecimal
    # Configuración de las columnas
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de super adminitrador", bg_color=f'{Bg2}', text_color=f'{TextColor}', font=("Helvetica", 18))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Botón para volver al menú
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=FontText)
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')
    ventana.pack(fill='both', expand=True)
    return ventana
