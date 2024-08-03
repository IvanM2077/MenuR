import sqlite3 as sq
import Models.DB
def insertTestOrder(self, UserId, Payment, PaymentConfirm):
    try:
        cur = self.getConnection().cursor()
        cur.execute(f'''
            INSERT INTO {self.TableOrder} (UserId, Payment, PaymentConfirm) 
            VALUES (?, ?, ?)
        ''', (UserId, Payment, PaymentConfirm))
        self.connection.commit()
        print("Order inserted successfully")
    except sq.Error as e:
        print(f"Error al insertar la orden: {e}")
        self.connection.rollback()


def test():
    db = Models.DB.DB.getInstance()

    # Verificar la ruta de la base de datos
    print(f"Database Path: {db.nameDB}")

    # Realizar una consulta simple para listar todos los usuarios
    try:
        cur = db.getConnection().cursor()
        cur.execute(f"SELECT * FROM {db.TableUser}")
        users = cur.fetchall()
        print(f"Users: {users}")
    except sq.Error as e:
        print(f"Error al obtener usuarios: {e}")

    try:
        cur = db.getConnection().cursor()
        cur.execute(f"SELECT * FROM {db.TableOrder}")
        orders = cur.fetchall()
        print(f"Orders: {orders}")
    except sq.Error as e:
        print(f"Error al obtener ordenes: {e}")

    # Insertar datos de prueba en la tabla TblOrder
    #db.insertTestOrder(1, 0, 0)  # Añadir orden no pagada
    #db.insertTestOrder(1, 1, 0)  # Añadir orden en proceso de pago
    #db.insertTestOrder(1, 1, 1)  # Añadir orden pagada

    # Realizar una consulta simple para listar todas las órdenes
    try:
        cur = db.getConnection().cursor()
        cur.execute(f"SELECT * FROM {db.TableOrder}")
        orders = cur.fetchall()
        print(f"Orders: {orders}")
    except sq.Error as e:
        print(f"Error al obtener órdenes: {e}")

    # Ejecutar la función getAllOrderById y verificar la salida
    try:
        List = db.getAllOrderById(1)
        print(f"Orders for UserId 1: {List}")
    except sq.Error as e:
        print(f"Error al obtener órdenes por UserId: {e}")


test()
