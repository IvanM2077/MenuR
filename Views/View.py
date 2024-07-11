import tkinter as tk
import MenuView as MV
import MenuOrderView as MOV
import InvoiceView as IV
import ConfirmView as CV
import RejectView as RV
import LoginView as LV
import NewUserView as NUW
from Infraestructure import ViewConfig as Config

# Dimensiones de la ventana

WIDTH, HEIGHT = Config.GetDimmentions()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Aplicación gestión de restaruantes")
        self.current_view = None  # Para mantener un seguimiento de la vista actual

    def show_view(self, new_view):
        # Si hay una vista actual, destrúyela
        if self.current_view:
            self.current_view.destroy()

        # Mostrar la nueva vista
        self.current_view = new_view
        self.resizable(False, False)
        self.current_view.pack()
    def RegisteNewUserView(self):
        registerView = NUW.returnNewUserView(self)
        self.show_view(registerView)

    def LoginView(self):
        loginView = LV.returnLoginView(self)
        self.show_view(loginView)

    def menuView(self):
        menuView = MV.ReturnMenuView(self)
        self.show_view(menuView)

    def menuOrderView(self):
        menuOrderView = MOV.returnMenuOrderView(self)
        self.show_view(menuOrderView)

    def invoiceView(self):
        invoiceView = IV.ReturnInvoiceView(self)
        self.show_view(invoiceView)

    def confirmView(self):
        confirmView = CV.ReturnConfirmView(self)
        self.show_view(confirmView)

    def rejectView(self):
        rejectView = RV.ReturnRejectView(self)
        self.show_view(rejectView)

    def initialize_app(self):
        self.LoginView()
        self.mainloop()

# Crea la instancia de la aplicación
myapp = App()
myapp.initialize_app()

