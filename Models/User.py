import json
import sqlite3
class User:
    def __init__(self, nombre, correo, edad, ):
        self.Nombre = nombre
        self.Correo=correo
        self.Edad=edad
        pass
    def ConsultUser(self):
        pass
#clase empleado que podrá realizar las peticiones y tomar las ordenes
'''
La diferencia entre estos residirá en los métodos para poder accesar 
y poder modificar los datos para que se pueda realizar una base de datos. 

'''
class Employee(User):
    def __init__(self, nombre, correo, password,edad):
        self.id= None
        self.Nombre = nombre
        self.Correo=correo
        self.password = password
        self.Edad=edad
        super().__init__()

        pass
class Administrator(User):
    def __init__(self,nombre, correo,password, edad):
        self.id= None
        self.Nombre = nombre
        self.Correo=correo
        self.password = password
        self.Edad=edad
        self.Token = True
        pass
