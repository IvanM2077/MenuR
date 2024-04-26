import sqlite3 as sq
#
nameDB="DBRest.db"
TableUser="USER"
TableOrder="OrderToOrder"
TableProducts="PRODUCTS"



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


    #Borrar Tabla
    #cur.execute(f"DROP TABLE {TableName1}")




#CREACIÓN DE LAS TABLAS
def CreateTableOrderN():
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    try:
        cur.execute(f''' CREATE TABLE {TableOrder} (
                    Id INTEGER NOT NULL PRIMARY KEY,
                    UserId INTEGER,
                    ItemProductId INTEGER,
                    Payment BOOL NOT NULL,
                    PaymentConfirm BOOL NOT NULL,
                    FOREIGN KEY (UserId) REFERENCES {TableUser}(Id),
                    FOREIGN KEY (ItemProductId) REFERENCES {TableProducts}(Id)
                    )
                    ''')
    except Exception as e:
        print(f"La tabla {TableOrder} ya fue creada")

def CreateTableProduct():
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    try:
        cur.execute(f''' CREATE TABLE {TableProducts} (
                    Id INTEGER NOT NULL PRIMARY KEY,
                    Item VARCHAR(50) NOT NULL,
                    Price INTEGER
                    )
                    ''')
    except Exception as e:
        print(f"La tabla {TableProducts} ya fue creada")


def CreateTableUser():
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    try:
        cur.execute(f''' CREATE TABLE {TableUser} (
                    Id INTEGER NOT NULL PRIMARY KEY,
                    Name VARCHAR(50) NOT NULL,
                    Age INTEGER,
                    Email VARCHAR(100) NOT NULL UNIQUE,
                    PassWord VARCHAR(8) NOT NULL
                    )
                    ''')
    except Exception as e:
        print(f"La tabla {TableUser} ya fue creada")











#CONSULTA EMAIL Y CONTRASEÑA
def consultPasswordAndEmail(Email,Password):
    #Creamos una conexión con la base de datos
    con = sq.connect(nameDB)
    #creamos un objeto cursor que ayudará a realizar acciones y consultas
    cur = con.cursor()

    #Le pasamos al objeto cursor el método execute que ejecutará el Query
    #Dandole como propiedas los nombres de la tabla de usuarios y los parametros de la función a recibir
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







#

def ConsultaOrdenesDelEmpleado(id):
    pass

