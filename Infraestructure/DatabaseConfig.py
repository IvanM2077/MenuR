import os

def getDataBaseNames():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #Obtiene la direccion del directorio
    database_dir = os.path.join(project_root, 'database') #crea una carpeta en el directorio llamada database
    os.makedirs(database_dir, exist_ok=True) #si existe, no la crea, caso contrario si
    nameDB = os.path.join(database_dir, 'DBRest.db') #monta la base de datos en la carpeta objetivo
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
