#Patron de desarrollo singleton
#<editor-fold desc="CreationDatabase">
#CREACIÓN DE LA BASE DE DATOS AL INICIALIZAR
import sqlite3 as sq
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
        self.closeConnection()

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
            cur = self.connection.cursor()
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
            cur = self.connection.cursor()
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
            cur = self.connection.cursor()
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
            cur = self.connection.cursor()
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
            cur = self.connection.cursor()
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
        con.commit()
        con.close()
        return True
    except Exception as e:
        return False

def getAllUser():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''SELECT * FROM {TableUser}''')
        con.commit()
        con.close()
        return True
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

