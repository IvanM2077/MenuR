import customtkinter as ctk
import os
from PIL import Image
from tkinter import ttk
from tkinter import messagebox
import Infraestructure.ViewConfig as IV
import Infraestructure.Helper as IH
import Models.Session
import Models.Sales

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()


def returnMenuOrderView(parent, session, OrderId=None, UserIdEmployee=None ):
    UserId = session.user.UserId
    Name = session.user.FirstName
    session.DataBase.getInstance()
    ListProducts = session.DataBase.getAllProducts()
    UserIdEmployee =None
    if (parent.rol):
        UserIdEmployee = session.DataBase.FindUserIdByOrderId(OrderId)
    print("Id Employee: ", UserIdEmployee, "Id Session: ", UserId)
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
    listButtons = []
    for i, product in enumerate(ListProducts):
        btn_text = f"{product.Item} - ${product.Price}"

        btn_MenuOrderView = ctk.CTkButton(buttons_frame, text=btn_text, fg_color=Btn1, command=lambda p=product: handleButton(parent, p, Tblgrid), font=FontText, height=btn_height)
        btn_MenuOrderView.grid(row=row, column=col, padx=10, pady=10, sticky='ew')
        listButtons.append(btn_MenuOrderView)
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

    #Lista para eliminar los productos que ya existen y cuano se cargue primero se haga un bulkdelete y despues un bulkinsert
    ListOldProducts = []
    FlagQuery = None
    if OrderId is None: #SI NO EXISTE LA ORDEN se considera como nueva
        print("No. Orden: ", OrderId)
        item1 = Tblgrid.insert("", ctk.END, text="Productos")
        FlagQuery = False






    else: #SI YA EXISTE LA ORDEN
        print("No. Orden: ", OrderId, "IdEmployee: ", UserIdEmployee, " IdSession: ", UserId)
        item1 = Tblgrid.insert("", ctk.END, text="Productos")
        if (parent.rol ==True): #estamos en el rol de administrador por lo que necesitamos  el id del empleado
            print("consulta sales OrderId: ", OrderId, " UserIdFindSales: ", UserIdEmployee)
            ListSale = session.DataBase.getAllSalesByOrderIdAndUserId(OrderId, UserIdEmployee)  #simplemente pasamos el id del usuario en vez del de la session
            ListOldProducts = ListSale
            for i, v in enumerate(ListSale):
                aux = findProductById(ListProducts, v.ProductId)
                Tblgrid.insert("", ctk.END, text=f"{1}", values=(aux.Item, aux.Price))
                FlagQuery = True
            pass


        else: #caso contrario estamos en el rol de empleado por lo que no hacemos modificaciones
            print("consulta sales OrderId: ", OrderId, " UserIdFindSales: ", UserId)
            ListSale = session.DataBase.getAllSalesByOrderIdAndUserId(OrderId, UserId)
            ListOldProducts = ListSale
            for i, v in enumerate(ListSale):
                aux = findProductById(ListProducts, v.ProductId)
                Tblgrid.insert("", ctk.END, text=f"{1}", values=(aux.Item, aux.Price))
                FlagQuery = True



    Tblgrid.pack(fill='both', expand=True)
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=(FontText))
    btn_BackToMenuView.grid(row=2, column=0, padx=10, pady=20, sticky='ew')
    btn_InvoiceView = ctk.CTkButton(ventana, text="Pedir nota", command=lambda: TakeOrder(parent,session,Tblgrid, OrderId, ListProducts, UserId, ListOldProducts, FlagQuery, UserIdEmployee), font=(FontText))
    btn_InvoiceView.grid(row=2, column=1, padx=10, pady=20, sticky='ew')
    return ventana


def TakeOrder(parent, session, Tblgrid, OrderId, ListProducts, UserId, ListOldProducts, FlagQuery, UserIdEmployee):
    if OrderId:  # cuando se seleccione una orden que ya exista
        items = Tblgrid.get_children()
        print(OrderId)
        ListSales = []
        for item in items:
            values = Tblgrid.item(item, 'values')
            if values:
                product_name = values[0]
                product_id = findIdByProductName(ListProducts, product_name)
                if product_id:
                    if (UserIdEmployee):# si existe el useridemployee le damos preferencia a ese
                        aux = Models.Sales.Sales(UserIdEmployee, OrderId, product_id)
                        ListSales.append(aux)
                    else:
                        aux = Models.Sales.Sales(UserId, OrderId, product_id)
                        ListSales.append(aux)
        if (UserIdEmployee):#si no es null id del IdEmployee se hace el insert de sus sales
            OrderObjId = session.DataBase.deleteSalesWithOrderId(ListSales, ListOldProducts, UserIdEmployee, OrderId)
            if OrderObjId == OrderId:
                print(OrderObjId[0], OrderId)
                flag2 = session.DataBase.InsertSalesWithOrderId(ListSales, ListOldProducts, UserIdEmployee, OrderId)
                parent.menuView()
                messagebox.showinfo("Exito OPERACION ADMINISTRADOR", f"Orden actualizada con éxito del usuario con id {UserIdEmployee}")
            else:
                messagebox.showerror("Error OPERACION ADMINISTRADOR", f"No se pudo realizar la operación del usuario con id{UserIdEmployee}")
        else: #si es nulo signofica que estamos haciendo una propia del usuario y no de un 3ro como en el caso anterior
            OrderObjId = session.DataBase.deleteSalesWithOrderId(ListSales, ListOldProducts, UserId, OrderId)
            if OrderObjId == OrderId:
                print(OrderObjId[0], OrderId)
                flag2 = session.DataBase.InsertSalesWithOrderId(ListSales, ListOldProducts, UserId, OrderId)
                parent.menuView()
                messagebox.showinfo("Exito OPERACION EMPLOYEE", "Orden actualizada con éxito")
            else:
                messagebox.showerror("Error OPERACION EMPLOYEE", "No se pudo realizar esta operación")




    else:  # cuando sea una nueva orden #esto solo lo puede agregar el usuario de la sesion
        items = Tblgrid.get_children()
        ListSales = []
        for item in items:
            values = Tblgrid.item(item, 'values')
            if values:
                product_name = values[0]
                product_id = findIdByProductName(ListProducts, product_name)
                if product_id:
                    aux = Models.Sales.Sales(UserId, None, product_id)
                    ListSales.append(aux)

        OrderObjId = session.DataBase.insertNewSalesByOrder(ListSales, UserId, FlagQuery)
        if OrderObjId:
            messagebox.showinfo("Exito", "Orden tomada con éxito")
            parent.menuView()
        else:
            messagebox.showerror("Error", "No se pudo insertar en la base de datos")



# Resto del código permanece igual



def configForNewSale():
    pass
def configForSaleThatExists():
    pass




def findIdByProductName(ListProducts, ProductName):
    for product in ListProducts:
        if product.Item == ProductName:
            return product.ProductId
    return None


def handleButton(parent, product, Tblgrid):
    Tblgrid.insert("", ctk.END, text="1", values=(product.Item, product.Price))
def findProductById(ListProducts, ProductId):
    for product in ListProducts:
        if product.ProductId == ProductId:
            return product
    return None