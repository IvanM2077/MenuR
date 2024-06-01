import tkinter as tk
import MenuView as MV
import MenuOrderView as MOV
import InvoiceView as IV
import ConfirmView as CV
import RejectView as RV
import LoginView as LV

# Dimensiones de la ventana
WIDTH = 400
HEIGHT = 300

class App(tk.Tk):
    def __init__(self):
        # Llama al constructor de tk.Tk
        super().__init__()
        # Establece las dimensiones de la ventana
        self.geometry(f"{WIDTH}x{HEIGHT}")
        # Título de la ventana
        self.title("Aplicación gestión de restaruantes")

        # Puedes agregar widgets y funcionalidad adicional aquí
    def LoginView(self):
        loginView=LV.returnLoginView()
        return loginView

    def menuView(self):
        menuView=MV.ReturnMenuView()
        return menuView
    def menuOrderView(self):
        menuOrderView=MOV.returnMenuOrderView()
        return menuOrderView
    def invoiceView(self):
        invoiceView=IV.ReturnInvoiceView()
        return invoiceView
    def confirmView(self):
        confirmView=CV.ReturnConfirmView()
        return confirmView
    def rejectView(self):
        rejectView=RV.ReturnRejectView()
        return rejectView


# Crea la instancia de la aplicación
myapp = App()
# Inicia el loop principal de Tkinter
myapp.LoginView()
myapp.mainloop()
