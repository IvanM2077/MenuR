import customtkinter as ctk
import Models.Session
import Infraestructure.ViewConfig as IV
from PIL import Image
import os
Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()

def returnMenuOrderView(parent, session, OrderId=None):
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)
    ventana.pack(fill='both', expand=True)

    ventana.grid_rowconfigure(0, weight=1)  # row header cabecero
    ventana.grid_rowconfigure(1, weight=9)  # row contenido

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Obtener la ruta del directorio actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_Dir = os.path.dirname(current_dir)
    dirLogoApp = os.path.join(root_Dir, "Images", "MenuRIcon.jpg")
    logo_image = Image.open(dirLogoApp)
    LogoApp = ctk.CTkImage(logo_image, size=(80, 80))

    Name = session.user.FirstName
    Db = session.DataBase.getInstance()
    Db.getAllRol()


    # <editor-fold desc="Header">
    # Frame para el encabezado
    header_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    header_frame.grid(row=0, column=0, columnspan=8, padx=10, pady=20, sticky='nsew')

    # Lbl icon menu
    lbl_IconMenu = ctk.CTkLabel(header_frame, text="", image=LogoApp, text_color=TextColor, font=FontTitle)
    lbl_IconMenu.pack(side="left", padx=10, pady=10)

    # Label de bienvenida en el frame de encabezado
    lbl = ctk.CTkLabel(header_frame, text=f"MenuR Bienvenido {Name}", text_color=TextColor, font=FontTitle)
    lbl.pack(side="left", padx=10, pady=10)

    # </editor-fold>

    # <editor-fold desc="Body">
    # Frame para los botones
    buttons_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    buttons_frame.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky='nsew')

    # Configuración de las columnas y filas en el frame de botones
    for i in range(3):
        buttons_frame.grid_columnconfigure(i, weight=1)
    for i in range(2):
        buttons_frame.grid_rowconfigure(i, weight=1)

    # Botones
    btn_height = 200  # Altura deseada para los botones

    btn_MenuOrderView = ctk.CTkButton(buttons_frame, text="New Order", fg_color=Btn1, command=parent.menuOrderView, font=FontText, height=btn_height)
    btn_MenuOrderView.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

    btn_SelectorOrderView = ctk.CTkButton(buttons_frame, text="Add to Order", fg_color=Btn1, command=parent.selectorView, font=FontText, height=btn_height)
    btn_SelectorOrderView.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

    btn_InvoiceView = ctk.CTkButton(buttons_frame, text="Invoice", fg_color=Btn1, command=parent.confirmView, font=(FontText), height=btn_height)
    btn_InvoiceView.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

    btn_PayView = ctk.CTkButton(buttons_frame, text="Pay", fg_color=Btn1, command=parent.rejectView, font=(FontText), height=btn_height)
    btn_PayView.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    btn_ConfirmPay = ctk.CTkButton(buttons_frame, text="Confirm Pay", fg_color=Btn1, command=parent.selectorView, font=(FontText), height=btn_height)
    btn_ConfirmPay.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
    # </editor-fold>

    return ventana

