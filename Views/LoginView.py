import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import Models.User as MU
import Models.DB
import Models.Session
import Infraestructure.Helper as IH
import Infraestructure.ViewConfig as IV
import os

Bg, Bg2, BtnC1, BtnC2, TextColor = IV.GetPalleteColours()
ConfTitles, ConfTexts = IV.getTypeLetters()
def returnLoginView(parent, session):
    #Padre
    ventana = ctk.CTkFrame(parent, fg_color=Bg)  # Color de fondo en formato hexadecimal
    #LadoDerecho
    # <editor-fold desc="Login lado derecho">
    # Configuración de las columnas
    ventana.grid_columnconfigure(0, weight=1)  # Columna para la imagen
    ventana.grid_columnconfigure(1, weight=1)  # Columna para los widgets

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Obtener la ruta del directorio actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #Uno mas arriba
    root_Dir = os.path.dirname(current_dir)
    image_path = os.path.join(root_Dir, "Images", "Login.png")

    # Fondo Lado derecho
    if os.path.exists(image_path):
        password_icon = ctk.CTkImage(Image.open(image_path), size=(800, 700))
        lbl_PasswordIcon = ctk.CTkLabel(ventana, image=password_icon, text="")
        lbl_PasswordIcon.grid(row=0, column=0, rowspan=7, padx=10, pady=10, sticky='nsew')
    else:
        messagebox.showwarning("Advertencia", f"No se encontró el archivo de imagen en {image_path}")

    # </editor-fold>

    # <editor-fold desc="Login lado izquierdo">
    # Frame para los widgets
    widget_frame = ctk.CTkFrame(ventana, fg_color=Bg)
    widget_frame.grid(row=0, column=1, rowspan=7, padx=10, pady=10, sticky='nsew')

    # Configuración de las columnas y filas en el frame de widgets
    for i in range(8):
        widget_frame.grid_columnconfigure(i, weight=1)
    for i in range(7):
        widget_frame.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(widget_frame, text="Sign in With", bg_color=Bg2, text_color=TextColor, font=(ConfTitles))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Label y Entry para correo
    lbl_Email = ctk.CTkLabel(widget_frame, text="Correo", bg_color=Bg2, text_color=TextColor, font=(ConfTexts))
    lbl_Email.grid(row=2, column=3, padx=10, pady=10, sticky='e')
    TextBoxEmail = ctk.CTkEntry(widget_frame)
    TextBoxEmail.grid(row=2, column=4, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para contraseña
    lbl_Password = ctk.CTkLabel(widget_frame, text="Password", bg_color=Bg2, text_color=TextColor, font=(ConfTexts))
    lbl_Password.grid(row=3, column=3, padx=10, pady=10, sticky='e')
    TextBoxPassword = ctk.CTkEntry(widget_frame, show='*')
    TextBoxPassword.grid(row=3, column=4, padx=10, pady=10, columnspan=3, sticky='w')

    # Botones para ingresar y registrarse
    btn_Login = ctk.CTkButton(widget_frame, text="Ingresar", font=ConfTexts, fg_color=BtnC1,command=lambda: verifyEmailAndPass(parent, TextBoxEmail, TextBoxPassword))
    btn_Login.grid(row=5, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    btn_RegisterUser = ctk.CTkButton(widget_frame, text="Regístrese como usuario nuevo",font=ConfTexts,fg_color=BtnC1, command=lambda: gotoNewUser(parent))
    btn_RegisterUser.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    # </editor-fold>


    ventana.pack(fill='both', expand=True)
    return ventana



def verifyEmailAndPass(parent, TextBoxEmail, TextBoxPassword):
    email = TextBoxEmail.get()
    password = TextBoxPassword.get()
    EmailProof = IH.verifyEmailLogin(email)
    PasswordProof = IH.verifyIsAlphaNumeric(password)
    PasswordSubmit = IH.encrypt(password)

    if EmailProof and PasswordProof:
        session = Models.Session.Session.getInstance()
        User = session.DataBase.consultEmail(email, PasswordSubmit)
        if User is not None:
            if User.Email == email and User.Password == PasswordSubmit:
                parent.PermissionLogin = True
                messagebox.showinfo("Éxito", "Login exitoso")
                session.user = User
                parent.menuView()
            if User.Email == email and User.Password != PasswordSubmit:
                messagebox.showwarning("Advertencia", "Contraseña Incorrecta")
        else:
            messagebox.showwarning("Advertencia", "No existe usuario  en la base de datos")
    else:
        messagebox.showwarning("Advertencia", "Datos inválidos")


def gotoNewUser(parent):
    parent.RegisteNewUserView()


'''
import tkinter as tk
from PIL import Image, ImageTk


def returnLoginView(parent):
    ventana = tk.Frame(parent)
    ventana.pack(fill='both', expand=True)

    # Cargar la imagen de fondo
    image_path = ".jpg"  # Reemplaza con la ruta a tu imagen
    image = Image.open(image_path)
    bg_image = ImageTk.PhotoImage(image)

    # Mostrar la imagen de fondo en un Label
    bg_label = tk.Label(ventana, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Crear el label y botones sobre el fondo
    lbl = tk.Label(ventana, text="Hola vista de Login", bg='#FFFFE0', bd=5, relief="solid",
                   highlightbackground='#FF6347', highlightthickness=2, font=("Helvetica", 16))
    lbl.place(x=150, y=100)  # Ajusta las coordenadas según sea necesario

    btn_navigate = tk.Button(ventana, text="Navegar a la siguiente vista", command=parent.menuView,
                             font=("Helvetica", 12))
    btn_navigate.place(x=150, y=150)  # Ajusta las coordenadas según sea necesario

    btn_navigate2 = tk.Button(ventana, text="Regístrese como usuario nuevo", command=parent.RegisteNewUserView,
                              font=("Helvetica", 12))
    btn_navigate2.place(x=150, y=200)  # Ajusta las coordenadas según sea necesario

    return ventana
'''