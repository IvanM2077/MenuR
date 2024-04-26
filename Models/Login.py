import json
import User
import DB
import Menu


class Login:
    def __init__(self,Email, Password):
        self.email = Email
        self.password = Password
        self.entry = False
        pass
    def __str__(self):
        return f"{self.email}"

    def getPasword(self):
        return self.password


    def getEmail(self):
        return self.email

    def consultaEmailandPass(self):
        try:
            self.entry = DB.consultPasswordAndEmail(str(self.password), str(self.email))
        except Exception as e:
            print(f"Error {self.entry} login")

    def CheckEntry(self):
        if self.entry == True:
            print("Ingresó correctamente")
        else:
            print("Error")




    @classmethod
    def callUser(cls):
        NewUser = User.Employee()
        pass


    def Acces(self):
        # Llama a la clase de db para realizar una busqueda de usuario si existe el correo y password
        # cambia el atributo a true

        self.entry = True

        pass