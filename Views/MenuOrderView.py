import customtkinter as ctk
import os
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import Infraestructure.ViewConfig as IV
import Infraestructure.Helper as IH
import Models.Session

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()

def returnMenuOrderView(parent, session, OrderId=None, Option=None):
    UserId = session.user.UserId
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)
    ventana.pack(fill='both', expand=True)

    # Configuración de las filas y columnas principales
    ventana.grid_rowconfigure(0, weight=1)  # header
    ventana.grid_rowconfigure(1, weight=9)  # body
    ventana.grid_rowconfigure(2, weight=1)  # footer

    ventana.grid_columnconfigure(0, weight=1)  # left
    ventana.grid_columnconfigure(1, weight=3)  # right

    # Obtener la ruta del directorio actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_Dir = os.path.dirname(current_dir)
    dirLogoApp = os.path.join(root_Dir, "Images", "MenuRIcon.jpg")
    logo_image = Image.open(dirLogoApp)
    LogoApp = ctk.CTkImage(logo_image, size=(80, 80))

    Name = session.user.FirstName
    Db = session.DataBase.getInstance()
    ListProducts = Db.getAllProducts()

    # Header
    header_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    header_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky='nsew')

    lbl_IconMenu = ctk.CTkLabel(header_frame, text="", image=LogoApp, text_color=TextColor, font=FontTitle)
    lbl_IconMenu.pack(side="left", padx=10, pady=10)

    lbl = ctk.CTkLabel(header_frame, text=f"MenuR Bienvenido {Name}", text_color=TextColor, font=FontTitle)
    lbl.pack(side="left", padx=10, pady=10)

    # Body izquierdo
    buttons_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    for i in range(3):
        buttons_frame.grid_columnconfigure(i, weight=1)
    for i in range(3):
        buttons_frame.grid_rowconfigure(i, weight=1)

    btn_height = 200
    col = 0
    row = 0

    for i, product in enumerate(ListProducts):
        btn_text = f"{product.Item} - ${product.Price}"
        btn_MenuOrderView = ctk.CTkButton(buttons_frame, text=btn_text, fg_color=Btn1, command=lambda p=product: parent.menuOrderView(OrderId=OrderId, Option=2), font=FontText, height=btn_height)
        btn_MenuOrderView.grid(row=row, column=col, padx=10, pady=10, sticky='ew')

        col += 1
        if col == 3:
            col = 0
            row += 1

    # Body derecho
    tbl_grid_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    tbl_grid_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    style = ttk.Style()
    style.configure("Treeview", font=(FontTitle[0], 16))
    style.configure("Treeview.Heading", font=(FontText[0], 16))

    Tblgrid = ttk.Treeview(tbl_grid_frame)
    Tblgrid["columns"] = ("#1", "#2")
    Tblgrid.column("#0", width=100)
    Tblgrid.column("#1", width=100)
    Tblgrid.column("#2", width=100)
    Tblgrid.heading("#0", text="Cantidad")
    Tblgrid.heading("#1", text="Item")
    Tblgrid.heading("#2", text="Price")

    if OrderId is None:
        print("No. Orden: ", OrderId)
        item1 = Tblgrid.insert("", ctk.END, text="Productos")
    else:
        print("No. Orden: ", OrderId)
        item1 = Tblgrid.insert("", ctk.END, text="Productos")
        ListSale = Db.getAllSalesByOrderId(OrderId, UserId)
        for i, v in enumerate(ListSale):
            aux = findProductById(ListProducts, v.ProductId)
            Tblgrid.insert(item1, ctk.END, text=f"{i}", values=(aux.Item, aux.Price))

    Tblgrid.pack(fill='both', expand=True)

    # Footer
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=(FontText))
    btn_BackToMenuView.grid(row=2, column=0, padx=10, pady=20, sticky='ew')

    btn_InvoiceView = ctk.CTkButton(ventana, text="Pedir nota", command=lambda: parent.invoiceView(), font=(FontText))
    btn_InvoiceView.grid(row=2, column=1, padx=10, pady=20, sticky='ew')

    return ventana

def findProductById(ListProducts, ProductId):
    for product in ListProducts:
        if product.ProductId == ProductId:
            return product
    return None
