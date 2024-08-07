import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import Models.Session
import Infraestructure.ViewConfig as IV
import Infraestructure.Helper as IH

# Obtener colores de la paleta y fuentes
Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()

def ReturnSelectorView(parent, session, option):
    ventana = ctk.CTkFrame(parent, fg_color='#41436A')

    # Configuración de las columnas y filas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de menú orden", bg_color=Bg2, text_color=TextColor, font=(FontTitle))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    ventana.pack(fill='both', expand=True)

    # Obtener instancia de sesión y órdenes del usuario
    session = Models.Session.Session.getInstance()
    ListOfOrders = session.DataBase.getAllOrderById(session.user.UserId)
    session.ListOrders = ListOfOrders
    listNoPaid = []
    listProcess = []
    listPaid = []

    for obj in ListOfOrders:
        if not obj.Payment and not obj.PaymentConfirm:
            listNoPaid.append(obj)
        elif obj.Payment and not obj.PaymentConfirm:
            listProcess.append(obj)
        elif obj.Payment and obj.PaymentConfirm:
            listPaid.append(obj)

    # Crear un estilo para Treeview y aplicar fuente grande
    style = ttk.Style()
    style.configure("Treeview", font=(FontTitle[0], 16))
    style.configure("Treeview.Heading", font=(FontText[0], 16))

    Tblgrid = ttk.Treeview(ventana)
    Tblgrid["columns"] = ("#1", "#2")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.heading("#0", text="No. Orden")
    Tblgrid.heading("#1", text="Pago cliente")
    Tblgrid.heading("#2", text="Confirmación aceptacion del pago")

    Tblgrid.grid(row=2, column=0, columnspan=8, padx=10, pady=20, sticky='nsew')

    item1 = Tblgrid.insert("", ctk.END, text="Ordenes no pagadas")
    for v in listNoPaid:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item1, ctk.END, text=f"{v.OrderId}", values=(aux, aux2))

    item2 = Tblgrid.insert("", ctk.END, text="Ordenes en proceso de pago")
    for v in listProcess:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item2, ctk.END, text=f"{v.OrderId}", values=(aux, aux2))

    item3 = Tblgrid.insert("", ctk.END, text="Ordenes pagadas")
    for v in listPaid:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item3, ctk.END, text=f"{v.OrderId}", values=(aux, aux2))

    # Botón para agregar producto a la orden
    if option == 2:  # si selecciona la opcion menu 2 order
        btn_addToOrderView = ctk.CTkButton(ventana, text="Add 2 Order", command=lambda: viewAddProductToOrder(parent, Tblgrid), font=(FontText))
        btn_addToOrderView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')
    if option == 3:  # si selecciona la opcion 3
        btn_InvoiceView = ctk.CTkButton(ventana, text="Invoice", command=lambda: viewGetInvoiceOrder(parent, Tblgrid), font=(FontText))
        btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')
    if option == 4:
        btn_InvoiceView = ctk.CTkButton(ventana, text="Pay", command=lambda: viewPayOrder(parent, Tblgrid), font=(FontText))
        btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')
    if option == 5:
        btn_InvoiceView = ctk.CTkButton(ventana, text="Pay Confirm", command=lambda: viewPayConfirmOrder(parent, Tblgrid), font=(FontText))
        btn_InvoiceView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')

    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=(FontText))
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    return ventana


def viewNewOrder(parent):
    parent.menuOrderView()


def viewAddProductToOrder(parent, Tblgrid):
    selected_item = Tblgrid.selection()
    if selected_item:
        item_values = Tblgrid.item(selected_item)
        order_id = item_values['text']
        print(f"Orden seleccionada: {order_id}")
        parent.menuOrderView(Option=2, OrderId=order_id)
    else:
        messagebox.showwarning("Error", "Debe seleccionar una orden válida")

def viewGetInvoiceOrder(parent, Tblgrid):
    selected_item = Tblgrid.selection()
    if selected_item:
        item_values = Tblgrid.item(selected_item)
        order_id = item_values['text']
        print(f"Orden seleccionada: {order_id}")
        parent.menuOrderView(Option=3, OrderId=order_id)
    else:
        messagebox.showwarning("Error", "Debe seleccionar una orden válida")

def viewPayOrder(parent, Tblgrid):
    selected_item = Tblgrid.selection()
    if selected_item:
        item_values = Tblgrid.item(selected_item)
        order_id = item_values['text']
        print(f"Orden seleccionada: {order_id}")
        parent.menuOrderView(Option=4, OrderId=order_id)
    else:
        messagebox.showwarning("Error", "Debe seleccionar una orden válida")

def viewPayConfirmOrder(parent, Tblgrid):
    selected_item = Tblgrid.selection()
    if selected_item:
        item_values = Tblgrid.item(selected_item)
        order_id = item_values['text']
        print(f"Orden seleccionada: {order_id}")
        parent.menuOrderView(Option=5, OrderId=order_id)
    else:
        messagebox.showwarning("Error", "Debe seleccionar una orden válida")
