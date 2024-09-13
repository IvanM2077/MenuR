import customtkinter as ctk
from tkinter import ttk
import Infraestructure.ViewConfig as IV
Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()
def ReturnAdministratorView(parent, session):
    ventana = ctk.CTkFrame(parent, fg_color=f'{Bg1}')  # Color de fondo en formato hexadecimal
    listOfUsers = session.DataBase.getAllUsers()
    listOfRols = session.DataBase.getAllRol()
    print(listOfRols)
    print(listOfUsers)
    dictionay = {}
    for v in listOfRols:
        dictionay[v.RolId] = v.NameRol
    # Configuración de las columnas
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de super adminitrador", bg_color=f'{Bg2}', text_color=f'{TextColor}', font=("Helvetica", 18))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida
    # Crear un estilo para Treeview y aplicar fuente grande
    style = ttk.Style()
    style.configure("Treeview", font=(FontTitle[0], 16))
    style.configure("Treeview.Heading", font=(FontText[0], 16))

    Tblgrid = ttk.Treeview(ventana)
    Tblgrid["columns"] = ("#1", "#2", "#3", "#4", "#5")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.column("#3", width=100)
    Tblgrid.column("#4", width=100)
    Tblgrid.column("#5", width=100)
    Tblgrid.heading("#0", text="Identificar unico de usuario")
    Tblgrid.heading("#1", text="Nombre")
    Tblgrid.heading("#2", text="Apellido")
    Tblgrid.heading("#3", text="Email")
    Tblgrid.heading("#4", text="Password")
    Tblgrid.heading("#5", text="Rol")
    Tblgrid.grid(row=2, column=0, columnspan=8, padx=10, pady=20, sticky='nsew')

    #item1 = Tblgrid.insert("", ctk.END, text="Ordenes no pagadas")
    for v in listOfUsers:
        aux = dictionay.get(v.RolId)
        Tblgrid.insert("", ctk.END, text=f"{v.UserId}", values=(v.FirstName, v.LastName, v.Email, v.Password, aux))

    # Botón para volver al menú
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=FontText)
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')
    ventana.pack(fill='both', expand=True)
    return ventana
