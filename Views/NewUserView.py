import customtkinter as ctk
from tkinter import messagebox
import Models.User as MU
import Models.DB
import Models.Session
import Infraestructure.Helper as IH
import Infraestructure.ViewConfig as IV

Bg1, Bg2, Btn1, Btn2, Btn3, TextColor = IV.GetPalleteColours()
#Bg2 = Btn1
FontTitle, FontText = IV.getTypeLetters()
def returnNewUserView(parent, session):
    ventana = ctk.CTkFrame(parent, fg_color=Bg1)

    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = ctk.CTkLabel(ventana, text="Create An Account", bg_color=Bg2, text_color=TextColor, font=(FontTitle))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Label y Entry para nombre
    lbl_FirstName = ctk.CTkLabel(ventana, text="Nombre", bg_color=Bg2, text_color=TextColor, font=(FontText))
    lbl_FirstName.grid(row=2, column=1, padx=10, pady=10, sticky='e')
    TextBoxFName = ctk.CTkEntry(ventana)
    TextBoxFName.grid(row=2, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para apellido
    lbl_LastName = ctk.CTkLabel(ventana, text="Apellido", bg_color=Bg2, text_color=TextColor, font=(FontText))
    lbl_LastName.grid(row=2, column=4, padx=10, pady=10, sticky='e')
    TextBoxLName = ctk.CTkEntry(ventana)
    TextBoxLName.grid(row=2, column=5, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para edad
    lbl_Age = ctk.CTkLabel(ventana, text="Edad", bg_color=Bg2, text_color=TextColor, font=(FontText))
    lbl_Age.grid(row=3, column=1, padx=10, pady=10, sticky='e')
    TextBoxAge = ctk.CTkEntry(ventana)
    TextBoxAge.grid(row=3, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para correo
    lbl_Email = ctk.CTkLabel(ventana, text="Email", bg_color=Bg2, text_color=TextColor, font=(FontText))
    lbl_Email.grid(row=4, column=1, padx=10, pady=10, sticky='e')
    TextBoxEmail = ctk.CTkEntry(ventana)
    TextBoxEmail.grid(row=4, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para contraseña
    lbl_Password = ctk.CTkLabel(ventana, text="Password", bg_color=Bg2, text_color=TextColor, font=(FontText))
    lbl_Password.grid(row=4, column=4, padx=10, pady=10, sticky='e')
    TextBoxPassword = ctk.CTkEntry(ventana, show='*')
    TextBoxPassword.grid(row=4, column=5, padx=10, pady=10, columnspan=3, sticky='w')

    # Botones para ingresar y registrarse
    btn_Login = ctk.CTkButton(ventana, text="Register", font=FontText, fg_color=Btn1, command=lambda: verificar_entradas(parent, TextBoxFName, TextBoxLName, TextBoxAge, TextBoxEmail, TextBoxPassword))
    btn_Login.grid(row=6, column=1, columnspan=1, padx=10, pady=20, sticky='n')

    btn_back = ctk.CTkButton(ventana, text="Back to login", font=FontText, fg_color=Btn1, command=lambda: BackToLogin(parent))
    btn_back.grid(row=6, column=6, columnspan=1, padx=10, pady=20, sticky='n')


    ventana.pack(fill='both', expand=True)
    return ventana


def verificar_entradas(parent, TextBoxFName, TextBoxLName, TextBoxAge, TextBoxEmail, TextBoxPassword):
    FN = IH.verifyIsAlpha(TextBoxFName.get())
    LN = IH.verifyIsAlpha(TextBoxLName.get())
    A = IH.verifyIsNumeric(TextBoxAge.get())
    E = IH.verifyIsEmail(TextBoxEmail.get())
    P = IH.verifyIsAlphaNumeric(TextBoxPassword.get())
    TextBoxPasswordSubmit = IH.encrypt(TextBoxPassword.get())  # Encriptar la contraseña

    if FN and LN and A and E and P:
        new_user = MU.User(0, TextBoxFName.get(), TextBoxLName.get(), TextBoxEmail.get(), TextBoxPasswordSubmit, 1)
        session = Models.Session.Session.getInstance()
        SearchUser = session.DataBase.consultPasswordAndEmail(TextBoxEmail.get(), TextBoxPasswordSubmit)
        if SearchUser is not None:
            messagebox.showwarning("Advertencia", "No se puede usar el correo, ya existe en la base de datos")
        else:
            if session.DataBase.InsertNewUser(new_user):
                messagebox.showinfo("Éxito", "Usuario agregado con éxito")
                parent.LoginView()
            else:
                messagebox.showerror("Error", "No se pudo agregar el usuario")
def BackToLogin(parent):
    parent.LoginView()