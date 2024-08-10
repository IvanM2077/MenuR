import customtkinter as ctk
from tkinter import ttk
import Infraestructure.Helper as IH
import Infraestructure.ViewConfig as IV

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()
def ReturnInvoiceView(parent, session, OrderId, UserIdEmployee):
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)  # Color de fondo en formato hexadecimal
    # Configuración de las columnas
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)
    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de Invoice", bg_color=Bg2, text_color=TextColor, font=FontTitle)
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    Tblgrid = ttk.Treeview(ventana)
    Tblgrid["columns"] = ("#1", "#2")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.heading("#0", text="No. Orden")
    Tblgrid.heading("#1", text="Pago cliente")
    Tblgrid.heading("#2", text="Confirmación aceptacion del pago")
    listProducts = []
    Tblgrid.grid(row=2, column=0, columnspan=8, padx=10, pady=20, sticky='nsew')
    for v in listProducts:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert("", ctk.END, text=f"{v.OrderId}", values=(aux, aux2))



    btn_InvoiceView = ctk.CTkButton(ventana, text="Volver al menu", command=parent.menuView(),font=(FontText))
    btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')
    if OrderId:
        btn_InvoiceView = ctk.CTkButton(ventana, text="Pay", command=lambda: payConfirm(parent, Tblgrid, OrderId,UserIdEmployee), font=(FontText))
        btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')
    if OrderId and parent.rol:
        btn_InvoiceView = ctk.CTkButton(ventana, text="Pay Confirm", command=lambda: payConfirmAdministrator(parent, Tblgrid), font=(FontText))
        btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')

    ventana.pack(fill='both', expand=True)


    return ventana

def payConfirm(parent, Tblgrid, OrderId, UserId):
    pass
def payConfirmAdministrator(parent, Tblgrid, OrderId, UserId):
    pass

