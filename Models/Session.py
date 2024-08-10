import Models.DB
import Models.User
import Models.Product
import Models.Orders
import Models.Sales

import Models.DB

class Session:
    _instance = None
    user = None
    rol = None
    ListProducts = None
    ListOrders = None
    ListSales = None
    DataBase = None

    @staticmethod
    def getInstance():
        if Session._instance is None:
            Session._instance = Session()
        return Session._instance

    def __init__(self):
        print("Session Initialiate")
        if Session._instance is not None:
            raise Exception("Error: clase singleton monohilo!")
        self.DataBase = Models.DB.DB.getInstance()
        if self.DataBase is None:
            raise Exception("Error al obtener la instancia de la base de datos.")



