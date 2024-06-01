import tkinter as tk
import MenuView as MV
import MenuOrderView as MOV
import InvoiceView as IV
import ConfirmView as CV
import RejectView as RV


def returnLoginView(parent):
    ventana = tk.Frame(parent)
    ventana.pack()

    lbl = tk.Label(ventana, text="Hola vista de Login")  # Aquí se especifica el contenedor (ventana)
    lbl.pack()



    # Crear y agregar un botón para navegar a la siguiente vista
    btn_navigate = tk.Button(ventana, text="Navegar a la siguiente vista", command=parent.menuView)
    btn_navigate.pack()

    btn_navigate2 = tk.Button(ventana, text="Registrece como usuario nuevo", command=parent.RegisteNewUserView)
    btn_navigate2.pack()

    return ventana


