import customtkinter as ctk
import Views.MenuView as MV
import Views.MenuOrderView as MOV
import Views.InvoiceView as IV
import Views.ConfirmView as CV
import Views.RejectView as RV
import Views.LoginView as LV
import Views.SelectorOrder as SO
import Views.NewUserView as NUW
import Views.waitingView as WV
import Views.AdministratorConfigView as ACW
from Infraestructure import ViewConfig as Config
from Models import DB as Database
from Models.Session import Session

# Dimensiones de la ventana
WIDTH, HEIGHT = Config.GetDimmentions()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Aplicación gestión de restaurantes")
        self.current_view = None  # Para mantener un seguimiento de la vista actual
        self.session = None
        self.rol = False
        self.PermissionLogin = False
        self.currenOpt = None

    def show_view(self, new_view):
        # Si hay una vista actual, se destruye
        if self.current_view:
            self.current_view.destroy()

        # Se muestra la nueva, y no permite que se haga resize
        self.current_view = new_view
        self.resizable(False, False)
        self.current_view.pack()

    def currentOption(self, option):
        if self.currenOpt:
            self.currenOpt = None
        self.currenOpt = option

    def RegisteNewUserView(self):
        registerView = NUW.returnNewUserView(self, self.session)
        self.show_view(registerView)

    def LoginView(self):
        self.session = Session.getInstance()
        loginView = LV.returnLoginView(self, self.session)
        self.show_view(loginView)

    def menuView(self):
        if self.PermissionLogin:
            menuView, opt = MV.ReturnMenuView(self, self.session)
            self.show_view(menuView)
            self.currentOption(opt)

    def menuOrderView(self, OrderId=None, UserIdEmployee=None):
        if self.PermissionLogin:
            menuOrderView = MOV.returnMenuOrderView(self, self.session, OrderId, UserIdEmployee)
            self.show_view(menuOrderView)

    def invoiceView(self, OrderId =None, Option=None):
        if self.PermissionLogin:
            invoiceView = IV.ReturnInvoiceView(self, self.session, OrderId, Option)
            self.show_view(invoiceView)

    def confirmView(self):
        if self.PermissionLogin:
            confirmView = CV.ReturnConfirmView(self, self.session)
            self.show_view(confirmView)
    def AdministratorConfigView(self):
        if self.PermissionLogin:
            AdministratorConfigView = ACW.ReturnAdministratorView(self, self.session)
            self.show_view(AdministratorConfigView)
    def waitingView(self,OrderId):
        if self.PermissionLogin:
            waitingView = WV.returnWaitingView(self, self.session, OrderId)
            self.show_view(waitingView)

    def rejectView(self):
        if self.PermissionLogin:
            rejectView = RV.ReturnRejectView(self, self.session)
            self.show_view(rejectView)

    def selectorView(self, option):
        if self.PermissionLogin:
            selectorView = SO.ReturnSelectorView(self, self.session, option)
            self.show_view(selectorView)

    def initialize_app(self):
        self.LoginView()
        self.mainloop()
