import os

def getDataBaseNames():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Un nivel más arriba
    database_dir = os.path.join(project_root, 'database')
    os.makedirs(database_dir, exist_ok=True)
    nameDB = os.path.join(database_dir, 'DBRest.db')
    TableUser = "TblUser"
    TableOrder = "TblOrder"
    TableProducts = "TblProduct"
    TableRol = "TblRol"
    TableSale = "TblSal"
    return nameDB, TableUser, TableOrder, TableProducts, TableRol, TableSale


def getValuesTblUser():
    UserId = "UserId"
    FirstName = "FirstName"
    LastName = "LastName"
    Email = "Email"
    Password ="Password"
    RolId = "RolId"
    return UserId, FirstName, LastName, Email, Password, RolId

def getValuesTblOrder():
    OrderId = "OrderId"
    UserId = "UserId"
    Payment = "Payment"
    PaymentConfirm = "PaymentConfirm"
    return OrderId, UserId, Payment, PaymentConfirm

def getValuesTblProduct():
    ProductId = "ProductId"
    Item = "Item"
    Description = "Description"
    Price = "Price"
    return ProductId, Item, Description, Price

def getValuesRol():
    RolId = "RolId"
    NameRol = "NameRol"
    return RolId, NameRol

def getValuesSale():
    UserId = "UserId"
    OrderId = "OrderId"
    ProductId ="ProductId"
    return UserId, OrderId, ProductId
