import customtkinter as ctk
from tkinter import ttk
import Infraestructure.Helper as IH
import Infraestructure.ViewConfig as IV

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()


def returnWaitingView(parent, session, OrderId):
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




    # Botón para volver al menú
    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=FontText)
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    btn_PayConfirm = ctk.CTkButton(ventana, text="Actualizar orden", command=lambda: updateWindow(parent, OrderId), font=FontText)
    btn_PayConfirm.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='ew')


    ventana.pack(fill='both', expand=True)

    return ventana

def updateWindow(parent, OrderId):

    pass