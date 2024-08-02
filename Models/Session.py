import Models.DB
import Models.User
import Models.Product
import Models.Orders
import Models.Sales

class Session:
    _instance = None

    def __init__(self):
        if Session._instance is not None:
            raise Exception("Esta clase es un Singleton. Usa getInstance() para obtener la única instancia.")
        else:
            self.user = None
            self.ListProducts = []
            self.ListOrders = []
            self.ListSales = []
            self.DataBase = Models.DB.DB.getInstance()

    @staticmethod
    def getInstance():
        if Session._instance is None:
            Session._instance = Session()
        return Session._instance

