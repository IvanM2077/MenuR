import tkinter as tk
from tkinter import messagebox
import Models.User as MU
import Models.DB
import Infraestructure.Helper as IH

def returnNewUserView(parent):
    ventana = tk.Frame(parent, bg='#725A7A')
    # Configuración de las columnas para centrado
    for i in range(8):
        ventana.grid_columnconfigure(i, weight=1)

    # Configuración de las filas para centrado
    for i in range(7):
        ventana.grid_rowconfigure(i, weight=1)

    # Label de bienvenida
    lbl = tk.Label(ventana, text="Hola usuario nuevo", bg='#C56C86', bd=5, relief="solid", font=("Helvetica", 18))
    lbl.grid(row=1, column=3, columnspan=2, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Label y Entry para nombre
    lbl_FirstName = tk.Label(ventana, text="Nombre", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_FirstName.grid(row=2, column=1, padx=10, pady=10, sticky='e')
    TextBoxFName = tk.Entry(ventana)
    TextBoxFName.grid(row=2, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para apellido
    lbl_LastName = tk.Label(ventana, text="Apellido", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_LastName.grid(row=2, column=4, padx=10, pady=10, sticky='e')
    TextBoxLName = tk.Entry(ventana)
    TextBoxLName.grid(row=2, column=5, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y SpinBox para edad
    lbl_Age = tk.Label(ventana, text="Edad", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_Age.grid(row=3, column=1, padx=10, pady=10, sticky='e')
    SpinBoxAge = tk.Spinbox(ventana, from_=0, to=100)
    SpinBoxAge.grid(row=3, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para correo
    lbl_Email = tk.Label(ventana, text="Correo", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_Email.grid(row=4, column=1, padx=10, pady=10, sticky='e')
    TextBoxEmail = tk.Entry(ventana)
    TextBoxEmail.grid(row=4, column=2, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para contraseña
    lbl_Password = tk.Label(ventana, text="Password", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_Password.grid(row=4, column=4, padx=10, pady=10, sticky='e')
    TextBoxPassword = tk.Entry(ventana, show='*')
    TextBoxPassword.grid(row=4, column=5, padx=10, pady=10, columnspan=3, sticky='w')

    # Botones para ingresar y registrarse
    btn_Login = tk.Button(ventana, text="Navegar a la siguiente vista", command=lambda: verificar_entradas(parent, TextBoxFName, TextBoxLName, SpinBoxAge, TextBoxEmail, TextBoxPassword))
    btn_Login.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='n')

    ventana.pack(fill='both', expand=True)
    return ventana

def verificar_entradas(parent, TextBoxFName, TextBoxLName, SpinBoxAge, TextBoxEmail, TextBoxPassword):
    FN = IH.verifyIsAlpha(TextBoxFName)
    LN = IH.verifyIsAlpha(TextBoxLName)
    A = IH.verifyIsNumeric(SpinBoxAge)
    E = IH.verifyIsEmail(TextBoxEmail)
    P = IH.verifyIsAlphaNumeric(TextBoxPassword)
    TextBoxPasswordSubmit = IH.encrypt(TextBoxPassword.get())  # Encriptar la contraseña

    if FN and LN and A and E and P:
        new_user = MU.User(0, TextBoxFName.get(), TextBoxLName.get(), TextBoxEmail.get(), TextBoxPasswordSubmit, 0)
        # Aquí podrías guardar el nuevo usuario en la base de datos, por ejemplo:
        # db_instance = Models.DB.getInstance()
        # db_instance.save_user(new_user)
        parent.LoginView()
