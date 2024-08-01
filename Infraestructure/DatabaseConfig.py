def getDataBaseNames():
    nameDB = "DBRest.db"
    TableUser = "USER"
    TableOrder = "Order"
    TableProducts = "PRODUCTS"
    TableRol = "ROL"
    TableSale = "SALE"
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