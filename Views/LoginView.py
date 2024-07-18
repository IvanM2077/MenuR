import tkinter as tk
import MenuView as MV
import MenuOrderView as MOV
import InvoiceView as IV
import ConfirmView as CV
import RejectView as RV
from PIL import Image, ImageTk

def returnLoginView(parent):
    ventana = tk.Frame(parent, bg='#303A52')  # Color de fondo en formato hexadecimal

    # Configuración de las columnas para centrado
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)
    ventana.grid_columnconfigure(3, weight=1)
    ventana.grid_columnconfigure(4, weight=1)
    ventana.grid_columnconfigure(5, weight=1)
    ventana.grid_columnconfigure(6, weight=1)
    ventana.grid_columnconfigure(7, weight=1)

    # Configuración de las filas para centrado
    ventana.grid_rowconfigure(0, weight=1)
    ventana.grid_rowconfigure(1, weight=1)
    ventana.grid_rowconfigure(2, weight=1)
    ventana.grid_rowconfigure(3, weight=1)
    ventana.grid_rowconfigure(4, weight=1)
    ventana.grid_rowconfigure(5, weight=1)
    ventana.grid_rowconfigure(6, weight=1)

    # Label de bienvenida
    lbl = tk.Label(ventana, text="Hola vista de Login", bg='#596174', bd=5, relief="solid", font=("Helvetica", 18))
    lbl.grid(row=1, column=1, columnspan=6, padx=10, pady=20, sticky='n')  # Centrar el label de bienvenida

    # Label y Entry para correo
    lbl_Email = tk.Label(ventana, text="Correo", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_Email.grid(row=2, column=3, padx=10, pady=10, sticky='e')
    TextBoxEmail = tk.Entry(ventana)
    TextBoxEmail.grid(row=2, column=4, padx=10, pady=10, columnspan=3, sticky='w')

    # Label y Entry para contraseña
    lbl_Password = tk.Label(ventana, text="Password", bg='#303A52', fg='#FFFFFF', font=("Helvetica", 12))
    lbl_Password.grid(row=3, column=3, padx=10, pady=10, sticky='e')
    TextBoxPassword = tk.Entry(ventana, show='*')
    TextBoxPassword.grid(row=3, column=4, padx=10, pady=10, columnspan=3, sticky='w')

    # Botones para ingresar y registrarse
    btn_Login = tk.Button(ventana, text="Ingresar", command=parent.menuView)
    btn_Login.grid(row=5, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    btn_RegisterUser = tk.Button(ventana, text="Regístrese como usuario nuevo", command=parent.RegisteNewUserView)
    btn_RegisterUser.grid(row=6, column=1, columnspan=6, padx=10, pady=20, sticky='ew')  # Ajustar el padding

    ventana.pack(fill='both', expand=True)
    return ventana





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