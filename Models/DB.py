import sqlite3 as sq
from Infraestructure import DatabaseConfig as DBConfig
#
nameDB, TableUser, TableOrder, TableProducts, TableRol, TableSale = DBConfig.getDataBaseNames()
#Patron de desarrollo singleton
#<editor-fold desc="CreationDatabase">
#CREACIÓN DE LA BASE DE DATOS AL INICIALIZAR
def CreateDB():
    #Creamos un objetoo que realizará la conexión db
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    #Método para ejecutar la cadena de caracteres como si fuese código SQL

    #Crear Tabla
    try:
        #Verificar si las tablas ya fueron creadas.
        #Si fueron creadas dar exception ya fueron creadas
        return f"Bases de datos creadas {nameDB}"

    except Exception as e:
        return "Las bases de datos ya fue creada"
#</editor-fold>
#<editor-fold desc="CreationTables">
#CREACIÓN DE LAS TABLAS
#Roles
def createTableRolId():
    con = sq.connect(nameDB)
    cur = con.cursor()
    try:
        cur.execute(f'''CREAE TABLE {TableRol} 
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
            CREATE TABLE {TableUser} (
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
        CREATE TABLE {TableProducts} (
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
                    CREATE TABLE {TableOrder} (
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
                    CREATE TABLE {TableSale} (
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
                    SELECT * FROM 
                    ''')
    except Exception as e:
        return False

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
#</editor-fold>
#<editor-fold desc="RolId">
#</editor-fold>

