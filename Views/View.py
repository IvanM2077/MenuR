import tkinter as tk
import Views.MenuView as MV
import Views.MenuOrderView as MOV
import Views.InvoiceView as IV
import Views.ConfirmView as CV
import Views.RejectView as RV
import Views.LoginView as LV
import Views.SelectorOrder as SO
import Views.NewUserView as NUW
from Infraestructure import ViewConfig as Config
from Models import DB as Database
from Models.Session import Session

# Dimensiones de la ventana
WIDTH, HEIGHT = Config.GetDimmentions()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Aplicación gestión de restaurantes")
        self.current_view = None  # Para mantener un seguimiento de la vista actual
        self.session = None
        self.PermissionLogin = False

    def show_view(self, new_view):
        # Si hay una vista actual, destrúyela
        if self.current_view:
            self.current_view.destroy()

        # Mostrar la nueva vista
        self.current_view = new_view
        self.resizable(False, False)
        self.current_view.pack()

    def RegisteNewUserView(self):
        registerView = NUW.returnNewUserView(self,self.session)
        self.show_view(registerView)

    def LoginView(self):
        self.session = Session.getInstance()
        loginView = LV.returnLoginView(self, self.session)
        self.show_view(loginView)

    def menuView(self):
        if self.PermissionLogin:
            #print(self.session.user.Email)
            menuView = MV.ReturnMenuView(self, self.session)
            self.show_view(menuView)

    def menuOrderView(self):
        if self.PermissionLogin:
            menuOrderView = MOV.returnMenuOrderView(self, self.session)
            self.show_view(menuOrderView)

    def invoiceView(self):
        if self.PermissionLogin:
            invoiceView = IV.ReturnInvoiceView(self)
            self.show_view(invoiceView)

    def confirmView(self):
        if self.PermissionLogin:
            confirmView = CV.ReturnConfirmView(self)
            self.show_view(confirmView)

    def rejectView(self):
        if self.PermissionLogin:
            rejectView = RV.ReturnRejectView(self)
            self.show_view(rejectView)

    def selectorView(self):
        if self.PermissionLogin:
            selectorView = SO.ReturnSelectorView(self)
            self.show_view(selectorView)

    def initialize_app(self):
        self.LoginView()
        self.mainloop()

