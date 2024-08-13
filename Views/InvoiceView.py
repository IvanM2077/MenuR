import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import Infraestructure.Helper as IH
import Infraestructure.ViewConfig as IV

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()


def ReturnInvoiceView(parent, session, OrderId, Option):
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)
    UserId = session.DataBase.FindUserIdByOrderId(OrderId)
    ListSales = session.DataBase.getAllSalesByOrderIdAndUserId(OrderId, UserId)
    ListProducts = session.DataBase.getAllProducts()

    # Configurar la cuadrícula
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de Invoice", bg_color=Bg2, text_color=TextColor, font=FontTitle)
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')

    # Treeview para mostrar los items de la factura
    Tblgrid = ttk.Treeview(ventana)
    Tblgrid["columns"] = ("#1", "#2")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.heading("#0", text="Cantidad")
    Tblgrid.heading("#1", text="Item")
    Tblgrid.heading("#2", text="Price")

    # Ubicación del Treeview en la cuadrícula
    Tblgrid.grid(row=2, column=1, columnspan=6, padx=10, pady=10, sticky='nsew')

    # Insertar valores en la tabla
    TotalInvoice = 0
    for i, v in enumerate(ListSales):
        product = findProductById(ListProducts, v.ProductId)
        Tblgrid.insert("", ctk.END, text=f"{1}", values=(product.Item, product.Price))
        TotalInvoice += product.Price

    # Insertar total de la factura
    LineSeparation = "------------------------------------------------"
    Tblgrid.insert("", ctk.END, text=f"{LineSeparation}", values=(f"{LineSeparation}",f"{LineSeparation}"))
    Tblgrid.insert("", ctk.END, text="Total de la cuenta", values=("", TotalInvoice))

    # Botón para volver al menú
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=FontText)
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    # Botón de pago
    if OrderId and Option =="pago":
        btn_Pay = ctk.CTkButton(ventana, text="Pay", command=lambda: payConfirm(parent, session, OrderId, UserId), font=FontText)
        btn_Pay.grid(row=6, column=4, columnspan=1, padx=10, pady=20, sticky='ew')
    # Botón de pago
    if OrderId and Option =="nota":
        btn_Pay = ctk.CTkButton(ventana, text="Invoice", command=lambda: invoicePaper(parent, session, OrderId, UserId), font=FontText)
        btn_Pay.grid(row=6, column=4, columnspan=1, padx=10, pady=20, sticky='ew')

    # Botón de confirmación de pago (solo para administradores)
    if OrderId and parent.rol == True:
        btn_PayConfirm = ctk.CTkButton(ventana, text="Pay Confirm", command=lambda: payConfirmAdministrator(parent, session, OrderId, UserId), font=FontText)
        btn_PayConfirm.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')

    ventana.pack(fill='both', expand=True)

    return ventana


def payConfirm(parent, session, OrderId, UserId):
    if OrderId:
        session.DataBase.confirmPayOrderByEmployee(OrderId)
        messagebox.showinfo("Exito", "Confirmación realizada con éxito")
        parent.waitingView(OrderId)
    else:
        messagebox.showwarning("Error FUNCION OBTENER INVOICE", "Debe seleccionar una orden válida")
def payConfirmAdministrator(parent, session, OrderId, UserId):
    if OrderId and parent.rol:
        session.DataBase.confirmPayOrderByAdministrator(OrderId)
        messagebox.showinfo("Exito", "Confirmación realizada con éxito")
    else:
        messagebox.showwarning("Error FUNCION OBTENER INVOICE", "Debe seleccionar una orden válida")
def invoicePaper(parent, Tblgrid, OrderId, UserId):
    if OrderId:
        pass
    else:
        messagebox.showwarning("Error FUNCION OBTENER INVOICE", "Debe seleccionar una orden válida")



def findProductById(ListProducts, ProductId):
    for product in ListProducts:
        if ProductId == product.ProductId:
            return product
    return None
