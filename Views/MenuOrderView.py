import tkinter as tk
from tkinter import ttk
import Models.Session

def returnMenuOrderView(parent, session):
    ventana = tk.Frame(parent, bg='#41436A')

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = tk.Label(ventana, text="Vista de menu orden", bg='#C56C86', bd=5, relief="solid", font=("Helvetica", 18))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    ventana.pack(fill='both', expand=True)

    # Obtener instancia de sesión y órdenes del usuario
    session = Models.Session.Session.getInstance()
    print(session.user.UserId)
    ListOfOrders = session.DataBase.getAllOrderById(session.user.UserId)
    session.ListOrders = ListOfOrders
    print(ListOfOrders)
    print(session.ListOrders)

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

    item1 = Tblgrid.insert("", tk.END, text="Ordenes no pagadas")
    for v in listNoPaid:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item1, tk.END, text=f"{v.OrderId}", values=(aux, aux2))

    item2 = Tblgrid.insert("", tk.END, text="Ordenes en proceso de pago")
    for v in listProcess:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item2, tk.END, text=f"{v.OrderId}", values=(aux, aux2))

    item3 = Tblgrid.insert("", tk.END, text="Ordenes pagadas")
    for v in listPaid:
        aux = "Sí" if v.Payment else "No"
        aux2 = "Sí" if v.PaymentConfirm else "No"
        Tblgrid.insert(item3, tk.END, text=f"{v.OrderId}", values=(aux, aux2))
    return ventana
