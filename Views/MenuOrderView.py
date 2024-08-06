import customtkinter as ctk
import os
from PIL import Image
import Infraestructure.ViewConfig as IV
import Infraestructure.Helper as IH
import Models.Session

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
FontTitle, FontText = IV.getTypeLetters()


def returnMenuOrderView(parent, session, OrderId=None, Option=None):
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
    ListProducts = Db.getAllProducts()

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

    # <editor-fold desc="Body izquierdo">
    # Frame para los botones
    buttons_frame = ctk.CTkFrame(ventana, fg_color=Bg2)
    buttons_frame.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky='nsew')

    # Configuración de las columnas y filas en el frame de botones
    for i in range(3):
        buttons_frame.grid_columnconfigure(i, weight=1)
    for i in range(3):
        buttons_frame.grid_rowconfigure(i, weight=1)

    # Botones
    btn_height = 200  # Altura deseada para los botones
    col = 0
    row = 0

    for i, product in enumerate(ListProducts):
        btn_text = f"{product.Item} - ${product.Price}"
        btn_MenuOrderView = ctk.CTkButton(buttons_frame, text=btn_text, fg_color=Btn1, command=lambda p=product: parent.menuOrderView(OrderId=OrderId, Option=2), font=FontText,height=btn_height)
        btn_MenuOrderView.grid(row=row, column=col, padx=10, pady=10, sticky='ew')

        col += 1
        if col == 3:
            col = 0
            row += 1
    # </editor-fold>

    if OrderId is None:  # Si el OrderId del selector no se pasa, se considera como nueva orden
        print("No. Orden: ", OrderId)
        # Lógica para manejar nueva orden
    else:  # Si el OrderId se pasa es que seleccionó de la bd, es que existe la orden
        print("No. Orden: ", OrderId)
        # Lógica para cargar orden existente

    btn_BackToMenuView = ctk.CTkButton(ventana, text="Volver al menu", command=lambda: parent.menuView(), font=(FontText))
    btn_BackToMenuView.grid(row=6, column=2, columnspan=1, padx=10, pady=20, sticky='ew')

    return ventana
