import json
import User
import DB
import Menu


class Login:
    def _init_(self, Email, Password, Entry=False):
        self.email = Email
        self.password = Password
        self.entry = Entry
        pass


    def getPasword(self):
        return self.password


    def getEmail(self):
        return self.email

    def consultaEmailandPass(self):
        email = Login.getEmail()
        try:
            self.entry = DB.consultPasswordAndEmail(self.password, self.email)
        except:
            return f"Error "






    @classmethod
    def callUser(cls):
        NewUser = User.Employee()
        pass


    def Acces(self):
        # Llama a la clase de db para realizar una busqueda de usuario si existe el correo y password
        # cambia el atributo a true

        self.entry = True

        pass