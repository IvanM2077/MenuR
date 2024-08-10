#Patron de desarrollo singleton
#<editor-fold desc="CreationDatabase">
#CREACIÓN DE LA BASE DE DATOS AL INICIALIZAR las tablas y consulta toda en una clase
import sqlite3 as sq

import Models.User
import Models.Orders
import Models.Rol
import Models.Product
import Models.Sales
from Infraestructure.DatabaseConfig import getDataBaseNames  # Asegúrate de que la importación sea correcta

# Obtén los nombres de la base de datos y tablas
nameDB, TableUser, TableOrder, TableProducts, TableRol, TableSale = getDataBaseNames()

class DB:
    _instance = None  # Única instancia

    @staticmethod
    def getInstance():
        if DB._instance is None:
            DB._instance = DB()
        return DB._instance

    def __init__(self):
        if DB._instance is not None:
            raise Exception("Error: clase singleton monohilo!")
        self.connection = None
        self.nameDB = nameDB
        self.TableUser = TableUser
        self.TableOrder = TableOrder
        self.TableProducts = TableProducts
        self.TableRol = TableRol
        self.TableSale = TableSale
        self.Initialiate()

    def Initialiate(self):
        self.getConnection()
        self.createTables()

    def getConnection(self):
        if self.connection is None:
            self.connection = sq.connect(self.nameDB)
        return self.connection

    def closeConnection(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def createTables(self):
        self.CreateTableRolId()
        self.CreateTableUser()
        self.CreateTableProduct()
        self.CreateTableOrder()
        self.CreateTableSale()

    def CreateTableRolId(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TableRol} (
                    RolId INTEGER PRIMARY KEY AUTOINCREMENT,
                    NameRol TEXT NOT NULL
                )
            ''')
            self.connection.commit()
        except sq.Error as e:
            print(f"Error al crear la tabla {self.TableRol}: {e}")
            self.connection.rollback()

    def CreateTableUser(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TableUser} (
                    UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                    FirstName TEXT NOT NULL,
                    LastName TEXT NOT NULL,
                    Email TEXT NOT NULL UNIQUE,
                    Password TEXT NOT NULL,
                    RolId INTEGER NOT NULL,
                    FOREIGN KEY (RolId) REFERENCES {self.TableRol}(RolId)
                )
            ''')
            self.connection.commit()
        except sq.Error as e:
            print(f"Error al crear la tabla {self.TableUser}: {e}")
            self.connection.rollback()

    def CreateTableProduct(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TableProducts} (
                    ProductId INTEGER PRIMARY KEY AUTOINCREMENT,
                    Item TEXT NOT NULL,
                    Description TEXT NOT NULL,
                    Price REAL NOT NULL
                )
            ''')
            self.connection.commit()
        except sq.Error as e:
            print(f"Error al crear la tabla {self.TableProducts}: {e}")
            self.connection.rollback()

    def CreateTableOrder(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TableOrder} (
                    OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
                    UserId INTEGER NOT NULL,
                    Payment INTEGER NOT NULL,
                    PaymentConfirm INTEGER NOT NULL,
                    FOREIGN KEY(UserId) REFERENCES {self.TableUser}(UserId)
                )
            ''')
            self.connection.commit()
        except sq.Error as e:
            print(f"Error al crear la tabla {self.TableOrder}: {e}")
            self.connection.rollback()

    def CreateTableSale(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TableSale} (
                    UserId INTEGER NOT NULL,
                    OrderId INTEGER NOT NULL,
                    ProductId INTEGER NOT NULL,
                    FOREIGN KEY(UserId) REFERENCES {self.TableUser}(UserId),
                    FOREIGN KEY(OrderId) REFERENCES {self.TableOrder}(OrderId),
                    FOREIGN KEY(ProductId) REFERENCES {self.TableProducts}(ProductId)
                )
            ''')
            self.connection.commit()
        except sq.Error as e:
            print(f"Error al crear la tabla {self.TableSale}: {e}")
            self.connection.rollback()

    def getAllUsersByIds(self, listIds):
        try:
            if not listIds:
                print("Lista vacía")
                return []
            cur = self.getConnection().cursor()
            cur.execute("BEGIN")
            placeholders = ', '.join(['?'] * len(listIds))
            query = f"SELECT * FROM {self.TableUser} WHERE UserId IN ({placeholders})"
            cur.execute(query, listIds)
            UsersQuerys = cur.fetchall()
            ListOfUsers = []
            for obj in UsersQuerys:
                aux = Models.User.User(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
                ListOfUsers.append(aux)
            self.connection.commit()
            return ListOfUsers
        except sq.Error as e:
            self.connection.rollback()
            print("Error, no se pudieron obtener todos los usuarios:", e)
            return None

    def getAllRol(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f"SELECT * FROM {self.TableRol}")
            RolsDb = cur.fetchall()
            RolsFound = []
            for i, v in enumerate(RolsDb):
                aux = Models.Rol.Rol(v[0], v[1])
                RolsFound.append(aux)
            if(RolsFound is not None):
                return RolsFound
            else:
                return None
                print("No existe valores en la db")
        except sq.Error as e:
            print("Error al consultar los roles: ", e)
    def getAllProducts(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f"SELECT * FROM {self.TableProducts}")
            ProductsDb = cur.fetchall()
            ProductsFound = []
            for i, v in enumerate(ProductsDb):
                aux = Models.Product.Product(v[0], v[1], v[2], v[3])
                ProductsFound.append(aux)
            if(ProductsFound is not None):
                return ProductsFound
            else:
                return None
                print("No existe valores en la db")
        except sq.Error as e:
            print("Error al consultar los productos: ", e)
    def consultPasswordAndEmail(self, Email, Password):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''SELECT * FROM {self.TableUser} WHERE {self.TableUser}.Email = ? AND {self.TableUser}.Password = ?''',(Email,Password))
            user_data = cur.fetchone()
            if user_data:
                if user_data[3] == Email and user_data[4] == Password:
                    return Models.User.User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
                if user_data[3] == Email and user_data[3] != Password:
                    return False
            else:
                return None
        except sq.Error as e:
            print("Error al consultar el usuario y/o contraseña: ", e)
            return None

    def consultEmail(self, Email, Password):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''SELECT * FROM {self.TableUser} WHERE {self.TableUser}.Email = ?''', (Email,))
            user_data = cur.fetchone()
            if user_data:
                if user_data[3] == Email and user_data[4] == Password:
                    return Models.User.User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5])
                if user_data[3] == Email and user_data[3] != Password:
                    return False
                self.connection.commit()
            else:
                self.connection.commit()
                return None

        except sq.Error as e:
            self.connection.rollback()
            print("Error al consultar el usuario y/o contraseña: ", e)
            return None


    def InsertNewUser(self, User):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''INSERT INTO {self.TableUser} (FirstName, LastName, Email, Password, RolId) VALUES (?, ?, ?, ?, ?)''',(User.FirstName, User.LastName, User.Email, User.Password, User.RolId))
            self.connection.commit()
            return True
        except sq.Error as e:
            print(f"Error no se pudo agregar el usuario: {e}")
            self.connection.rollback()
            return False

    def getAllOrder(self):
        try:
            cur = self.getConnection().cursor()
            cur.execute(f'''
                   SELECT {self.TableUser}.UserId, {self.TableOrder}.OrderId, {self.TableOrder}.Payment, {self.TableOrder}.PaymentConfirm
                   FROM {self.TableUser}
                   INNER JOIN {self.TableOrder} ON {self.TableUser}.UserId = {self.TableOrder}.UserId
                    ''' )
            ListOrders = cur.fetchall()
            if ListOrders != None:
                List = []
                for order in ListOrders:
                    aux = Models.Orders.Orders(order[1], order[0], order[2], order[3])
                    List.append(aux)
                self.connection.commit()
                return List
            else:
                self.connection.commit()
                print("No orders found for the given UserId.")
                return []

        except sq.Error as e:
            print(f"Error al obtener el listado de órdenes: {e}")
            self.connection.rollback()
            return []
    def getAllOrderById(self, UserId):
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute(f'''
                SELECT {self.TableUser}.UserId, {self.TableOrder}.OrderId, {self.TableOrder}.Payment, {self.TableOrder}.PaymentConfirm
                FROM {self.TableUser}
                INNER JOIN {self.TableOrder} ON {self.TableUser}.UserId = {self.TableOrder}.UserId
                WHERE {self.TableUser}.UserId = ?
            ''', (UserId,))
            ListOrders = cur.fetchall()
            if ListOrders != None:
                List = []
                for order in ListOrders:
                    aux = Models.Orders.Orders(order[1], order[0], order[2], order[3])
                    List.append(aux)
                con.commit()
                return List
            else:
                con.commit()
                print("No orders found for the given UserId.")
                return []

        except sq.Error as e:
            print(f"Error al obtener el listado de órdenes: {e}")
            self.connection.rollback()
            return []

    def getAllSalesByOrderId(self, OrderId, UserId):
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute(f"""
                SELECT {self.TableSale}.UserId, {self.TableSale}.OrderId, {self.TableSale}.ProductId
                FROM {self.TableSale}
                INNER JOIN {self.TableOrder} ON {self.TableSale}.OrderId = {self.TableOrder}.OrderId
                WHERE {self.TableSale}.OrderId = ? AND {self.TableSale}.UserId = ?
            """, (OrderId, UserId))
            results = cur.fetchall()
            ListResults = []
            for v in results:
                aux = Models.Sales.Sales(UserId=v[0], OrderId=v[1], ProductId=v[2])
                ListResults.append(aux)
            return ListResults
        except sq.Error as e:
            self.connection.rollback()
            print("Error: ", e)
            return []


    def insertNewSalesByOrder(self, ListSale, UserId, FlagQuery):
        try:
            if FlagQuery == False:
                con = self.getConnection()
                cur = con.cursor()
                con.execute('BEGIN')
                cur.execute(f"INSERT INTO {self.TableOrder} (UserId, Payment, PaymentConfirm) VALUES (?, ?, ?)",(UserId, 0, 0))
                cur.execute(f"SELECT * FROM {self.TableOrder} WHERE UserId = ? ORDER BY OrderId DESC LIMIT 1", (UserId,))
                NewOrder = cur.fetchone()
                if NewOrder:
                    aux = Models.Orders.Orders(NewOrder[0], NewOrder[1], NewOrder[2], NewOrder[3])
                    sales_data = [(aux.UserId, aux.OrderId, sale.ProductId) for sale in ListSale]
                    cur.executemany(f"INSERT INTO {self.TableSale} (UserId, OrderId, ProductId) VALUES (?, ?, ?)",
                                    sales_data)
                con.commit()
                print("Valores insertados con éxito.")
                return True
            else:
                return False
        except sq.Error as e:
            self.connection.rollback()
            print("Error no se pudo insertar valor: ", e)
            return False

    def deleteSalesWithOrderId(self, ListSale, OldListSale, UserId, OrderId):
        try:
            print(UserId, OrderId, ListSale)
            con = self.getConnection()
            cur = con.cursor()
            con.execute('BEGIN')
            cur.execute(f"DELETE FROM {self.TableSale} WHERE UserId = ? AND OrderId = ?", (UserId, OrderId))
            cur.execute(f"SELECT * FROM {self.TableOrder} WHERE UserId = ? AND OrderId = ? LIMIT 1", (UserId, OrderId))
            Order = cur.fetchone()
            con.commit()
            return OrderId
        except sq.Error as e:
            con.rollback()
            print("Error no se pudo insertar valor: ", e)
            return False

    def InsertSalesWithOrderId(self, ListSale, OldListSale, UserId, OrderId):
        try:
            print(UserId, OrderId, ListSale)
            con = self.getConnection()
            cur = con.cursor()
            con.execute('BEGIN')
            sales_data = [(UserId, OrderId, sale.ProductId) for sale in ListSale]
            if sales_data and OrderId:
                cur.executemany(f"INSERT INTO {self.TableSale} (UserId, OrderId, ProductId) VALUES (?, ?, ?)", sales_data)
            con.commit()
            print("Valores insertados con éxito.")
            return True
        except sq.Error as e:
            con.rollback()
            print("Error no se pudo insertar valor: ", e)
            return False
#</editor-fold>
#<editor-fold desc="CreationTables">
#CREACIÓN DE LAS TABLAS
#Roles
def CreateTableRolId():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''CREAE TABLE IF NOT EXISTS {TableRol} 
                    (
                    RolId INTEGER PRIMARY KEY AUTOINCREMENT,
                    NameRol VARCHAR(20) NOT NULL
                    )
                    ''')
        return True
    except Exception as e:
        return False
#Usuarios
def CreateTableUser():
    con = sq.connect(nameDB)
    # Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    try:
        cur.execute(f''' 
            CREATE TABLE IF NOT EXISTS {TableUser} (
                UserId INTEGER PRIMARY KEY AUTOINCREMENT,
                FirstName TEXT NOT NULL,
                LastName TEXT NOT NULL,
                Email TEXT NOT NULL UNIQUE,
                PasswordEmail TEXT NOT NULL, 
                RolId INTEGER NOT NULL,
                FOREIGN KEY (RolId) REFERENCES {TableRol}(RolId)
                );
                    ''')

    except Exception as e:
        print(f"La tabla {TableUser} ya fue creada")
    con.commit()
    con.close()
#Productos
def CreateTableProduct():
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    try:
        cur.execute(f''' 
        CREATE TABLE IF NOT EXISTS {TableProducts} (
            ProductId INTEGER PRIMARY KEY AUTOINCREMENT,
            Item TEXT NOT NULL,
            Description TEXT NOT NULL,
            Price REAL NOT NULL
        );
                    ''')

    except Exception as e:
        print(f"La tabla {TableProducts} ya fue creada")
    con.commit()
    con.close()
#Ordenes
def CreateTableOrder():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f''' 
                    CREATE TABLE IF NOT EXISTS {TableOrder} (
                        OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
                        UserId INTEGER NOT NULL,
                        Payment INTEGER NOT NULL,  
                        PaymentConfirm INTEGER NOT NULL,
                        FOREIGN KEY(UserId) REFERENCES {TableUser}(UserId)
                    );
                    ''')
    except Exception as e:
        print(f"La tabla {TableOrder} ya fue creada")
    con.commit()
    con.close()
#VentaOrder
def CreateTableSale():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''
                    CREATE TABLE IF NOT EXISTS {TableSale} (
                        UserId INTEGER NOT NULL,
                        OrderId INTEGER NOT NULL,
                        ProductId INTEGER NOT NULL,
                        FOREIGN KEY(UserId) REFERENCES {TableUser}(UserId),
                        FOREIGN KEY(OrderId) REFERENCES {TableOrder}(OrderId),
                        FOREIGN KEY(ProductId) REFERENCES {TableProducts}(ProductId)
                    );

                    )''')
        con.commit()
        con.close()
    except Exception as e:
        print(f"La tabla {TableSale} ya fue creada")
#</editor-fold>
#<editor-fold desc="User">
def createUser(FirstName, LastName, Email, Password):
    con = sq.connect(nameDB)
    cur=con.cursor()
    RolId = 1
    try:
        var = consultPasswordAndEmail(Email, Password)
        #Si existe el usuario devolverá un true, si no, devolverá un false.
        if(var == True):
            cur.execute(f''' INSERT INTO {TableUser} VALUES({FirstName}, {LastName}, {Email}, {Password}, {RolId})''')
            con.commit()
            con.close()
            return True
        else:
            return False
    except Exception as e:
        return False
def updateUser(id,Fname, LName):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''UPDATE {TableUser} SET FirstName = {Fname}, LastName = {LName} WHERE UserId = {id} ''')
        con.commit()
        con.close()
    except Exception as e:
        return False
def deleteUser(id):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''DELETE FROM {TableUser} WHERE UserId = {id}''')
        con.commit()
        con.close()
        return True
    except Exception as e:
        return False
def getUserById(id):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''SELECT * FROM {TableUser} WHERE UserId = {id}''')
        obj = cur.fetchone()
        con.commit()
        con.close()
        return obj
    except Exception as e:
        return False

def getAllUser():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''SELECT * FROM {TableUser}''')
        objs = cur.fetchall()
        con.commit()
        con.close()
        return objs
    except Exception as e:
        return False
#</editor-fold>
#<editor-fold desc="Login">
#CONSULTA EMAIL Y CONTRASEÑA
def consultPasswordAndEmail(Email,Password):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''
                    SELECT * FROM {TableUser} WHERE {TableUser}.Email = ? AND {TableUser}.PassWord = ?
                    ''', (Email, Password))
        #selecciona el primer usuario que encontró (dado que el email es unique solo puede haber uno de ellos en la base de datos)
        user=cur.fetchone()
        #realizamos un commit para que se realice la acción
        con.commit()
        #cerramos la base de datos
        con.close()
        return True
        #AL realizar la consulta si el usuario existe dado que solo puede haber una unica clave de Email y contraseña
        #Cambiará el atributo de la clase login para que el usuario pueda acceder a la interfaz y realizar sus acciones


    except Exception as e:
        print("Error no existe el usuario y/o contraseña")
        return False

#</editor-fold>
#<editor-fold desc="Orders">
def getAllOrderByID(UserId):
    cur = sq.connect(nameDB)
    con = cur.cursor()
    try:
        cur.execute(f'''
                    SELECT {TableUser}.UserId, {TableOrder}.OrderId FROM {TableUser} INNER JOIN {TableOrder} ON {TableUser}.UserId = {TableOrder}.UserId WHERE {TableUser}.UserId= {UserId}
                    ''')
    except Exception as e:
        return False

def InsertNewOrder(UserId):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(
            f''' INSERT INTO {TableOrder} VALUES ({UserId}, {0}, {0})''')
    except Exception as ex:
        return "Error"
def DoPayment(UserId, OrderId):
    con = sq.connect(nameDB)
    cur= con.cursor()
    try:
        cur.execute(f''' UPDATE {TableOrder} SET Payment ={1} WHERE UserId = {UserId} AND OrderId = {OrderId} ''')
    except Exception as e:
        return "Error"
def ConfirmPayment(UserId, OrderId):
    con = sq.connect(nameDB)
    cur= con.cursor()
    try:
        cur.execute(f''' UPDATE {TableOrder} SET PaymentConfirm = {1} WHERE UserId = {UserId} AND OrderId = {OrderId} ''')
    except Exception as e:
        return "Error"



#</editor-fold>
#<editor-fold desc="Products">
def getAllProduct():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''SELECT * FROM {TableProducts} ''')
        AllProducts=cur.fetchall()
        con.commit()
        con.close()
        return AllProducts
    except Exception as e:
        print("Error no existe el usuario y/o contraseña")
        return False

def getProductById(ProductId):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        if (id != None):
            cur.execute(f'''SELECT * FROM {TableProducts} WHERE ProductId = {ProductId}''')
            ProductObj = cur.fetchone()
            con.commit()
            con.close()
            return ProductObj
        else:
            return False
    except Exception as e:
        print("Error")
        return False
def insertNewProduct(item, description, price):
    con=sq.connect(nameDB)
    cur = con.cursor()
    try:
        if(item ==  None):
            return False
        if(description ==  None):
            return False
        if(price ==  None or not price.isnumeric()):
            return False
        cur.execute(f'''INSERT INTO {TableProducts} VALUES ('{item}', '{description}', {price})''')
        con.commit()
        con.close()

    except Exception as e:
        return False
#</editor-fold>
#<editor-fold desc="Sale">
def getSaleByOrder(UserId, OrderId):
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        "--SELECT * FROM {TableSale} WHERE UserId = {UserId} AND OrderId = {OrderId}"
        cur.execute(f''' 
        SELECT * {TableUser}.UserId, {TableOrder}.OrderId, {TableSale}.ProductId FROM {TableOrder} INNER JOIN {TableSale} ON {TableOrder}.UserId = {TableSale}.UserId AND {TableOrder}.OrderId ={TableSale}.OrderId WHERE {TableSale}.UserId = {UserId}  AND {TableSale}.OrderId = {OrderId}
                    ''')
        return
    except Exception as e:
        return "Error"

#</editor-fold>
#<editor-fold desc="RolId">

#</editor-fold>

