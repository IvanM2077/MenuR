import sqlite3 as sq
#
nameDB="DBRest.db"
TableUser="USER"
TableOrder="OrderToOrder"
TableProducts="PRODUCTS"

Create = ''' CREATE TABLE{TableUser} '''

def CreateDB():
    #Creamos un objetoo que realizará la conexión db
    con = sq.connect(nameDB)
    #Crea un objeto tipo cursor que podrá acceder a la base de datos
    cur = con.cursor()
    #Método para ejecutar la cadena de caracteres como si fuese código SQL

    #Crear Tabla


    #Borrar Tabla
    #cur.execute(f"DROP TABLE {TableName1}")


def consultaPassword(password):
    pass

def consultaEmail(email):
    pass