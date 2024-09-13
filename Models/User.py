import json
import sqlite3
class User:
    def __init__(self, UserId, FirstName, LastName, Email, Password, RolId):
        self.UserId = UserId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Password = Password
        self.RolId = RolId

    def __str__(self):
        return f"{self.UserId} --> {self.FirstName}"

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
class Administrator(User):
    def __init__(self,nombre, correo,password, edad):
        self.id= None
        self.Nombre = nombre
        self.Correo=correo
        self.password = password
        self.Edad=edad
        self.Token = True
        pass
