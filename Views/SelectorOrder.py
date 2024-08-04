import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import Models.Session


def ReturnSelectorView(parent):
    ventana = ctk.CTkFrame(parent, fg_color='#41436A')

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Vista de menú orden", bg_color='#C56C86', text_color='#FFFFFF',
                       font=("Helvetica", 18))
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

    # Botón para ver resumen del pedido
    btn_NewOrderView = ctk.CTkButton(ventana, text="Agregar productos a la orden", command=lambda: viewNewOrder(parent),
                                     font=("Helvetica", 12))
    btn_NewOrderView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    # Botón para agregar producto a la orden
    btn_addToOrderView = ctk.CTkButton(ventana, text="Nueva orden la orden",command=lambda: viewAddProductToOrder(parent, Tblgrid), font=("Helvetica", 12))
    btn_addToOrderView.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')

    print(session.user.UserId)
    print(ListOfOrders)
    print(session.ListOrders)
    print(listPaid)
    print(listProcess)
    print(listNoPaid)
    for i, val in enumerate(ListOfOrders):
        print(val.UserId, val.OrderId, val.Payment, val.PaymentConfirm)

    return ventana


def viewNewOrder(parent):
    parent.menuOrderView()


def viewAddProductToOrder(parent, Tblgrid):
    selected_item = Tblgrid.selection()
    if selected_item:
        item_values = Tblgrid.item(selected_item)
        order_id = item_values['text']
        print(f"Orden seleccionada: {order_id}")
        parent.menuOrderView()  # Aquí deberías pasar el OrderId o cualquier información relevante
    else:
        messagebox.showwarning("Error", "Debe seleccionar una orden válida")