import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import Infraestructure.ViewConfig as IV
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()


def ReturnInvoiceView(parent, session, OrderId, Option):
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)
    UserId = session.DataBase.FindUserIdByOrderId(OrderId)
    ListSales = session.DataBase.getAllSalesByOrderIdAndUserId(OrderId, UserId)
    ListProducts = session.DataBase.getAllProducts()

    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    if Option == "nota":
        lblNota = ctk.CTkLabel(ventana, text="Vista de Invoice", bg_color=Bg2, text_color=TextColor, font=FontTitle)
        lblNota.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')
    if Option == "pago":
        lblPago = ctk.CTkLabel(ventana, text="Vista de Pago", bg_color=Bg2, text_color=TextColor, font=FontTitle)
        lblPago.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')

    Tblgrid = ttk.Treeview(ventana)
    Tblgrid["columns"] = ("#1", "#2")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.heading("#0", text="Cantidad")
    Tblgrid.heading("#1", text="Item")
    Tblgrid.heading("#2", text="Price")
    Tblgrid.grid(row=2, column=1, columnspan=6, padx=10, pady=10, sticky='nsew')

    TotalInvoice = 0
    for i, v in enumerate(ListSales):
        product = findProductById(ListProducts, v.ProductId)
        Tblgrid.insert("", ctk.END, text=f"{1}", values=(product.Item, product.Price))
        TotalInvoice += product.Price

    LineSeparation = "------------------------------------------------"
    Tblgrid.insert("", ctk.END, text=f"{LineSeparation}", values=(f"{LineSeparation}", f"{LineSeparation}"))
    Tblgrid.insert("", ctk.END, text="Total de la cuenta", values=("", TotalInvoice))

    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=FontText)
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    if OrderId and Option == "pago":
        btn_Pay = ctk.CTkButton(ventana, text="Pay", command=lambda: payConfirm(parent, session, OrderId, UserId),
                                font=FontText)
        btn_Pay.grid(row=6, column=4, columnspan=1, padx=10, pady=20, sticky='ew')

    if OrderId and Option == "nota":
        btn_Pay = ctk.CTkButton(ventana, text="Invoice", command=lambda: generarPdf(parent,Tblgrid, OrderId, UserId),
                                font=FontText)
        btn_Pay.grid(row=6, column=4, columnspan=1, padx=10, pady=20, sticky='ew')

    if OrderId and parent.rol:
        btn_PayConfirm = ctk.CTkButton(ventana, text="Pay Confirm",
                                       command=lambda: payConfirmAdministrator(parent, session, OrderId, UserId),
                                       font=FontText)
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


def generarPdf(parent,tblgrid, OrderId, UserId, output_pdf_name="nota_consumo.pdf"):
    output_dir = os.path.join(os.getcwd(), "invoiceTest")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_pdf_path = os.path.join(output_dir, output_pdf_name)

    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Nota de Consumo - Orden ID: {OrderId}")
    c.drawString(100, 735, f"Cliente ID: {UserId}")
    c.drawString(100, 720, "---------------------------------------------")

    y_position = 700
    total_amount = 0
    Size = len(tblgrid.get_children())
    total_amount = 0

    # Iterar hasta el penúltimo elemento
    for i, child in enumerate(tblgrid.get_children()[:-1]):
        item_quantity = tblgrid.item(child, 'text')
        item_name = tblgrid.item(child, 'values')[0]
        item_price = tblgrid.item(child, 'values')[1]
        try:
            item_price = float(item_price)
            total_amount += item_price
        except ValueError:
            continue

        c.drawString(100, y_position, f"{item_quantity} x {item_name} - ${item_price}")
        y_position -= 20

    c.drawString(100, y_position - 20, "---------------------------------------------")
    c.drawString(100, y_position - 40, f"Total: ${total_amount}")
    c.save()

    messagebox.showinfo("Exito", f"PDF guardado en: {output_pdf_path}")
    parent.menuView()
    return output_pdf_path


def findProductById(ListProducts, ProductId):
    for product in ListProducts:
        if product.ProductId == ProductId:
            return product
    return None
