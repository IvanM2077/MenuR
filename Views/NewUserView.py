import tkinter as tk


def returnNewUserView(parent):
    ventana = tk.Frame(parent)
    ventana.pack()

    lbl = tk.Label(ventana, text="Hola usuario nuevo")  # Aquí se especifica el contenedor (ventana)
    lbl.pack()

    # Crear y agregar un botón para navegar a la siguiente vista
    btn_navigate = tk.Button(ventana, text="Navegar a la siguiente vista", command=parent.LoginView)
    btn_navigate.pack()

    return ventana