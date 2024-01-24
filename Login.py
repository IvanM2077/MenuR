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


    @classmethod
    def consultaEmail(cls, email):
        email = Login.getEmail()
        try:
            DB.consultaEmail(email)
        except:
            return f"Error "

        pass


    @classmethod
    def consultaPassword(cls):
        password = Login.getPasword()
        try:
            DB.consultaPassword(password)

        except:
            return f"Error"

        pass


    @classmethod
    def callUser(cls):
        NewUser = User.Employee()
        pass


    def Acces(self):
        # Llama a la clase de db para realizar una busqueda de usuario si existe el correo y password
        # cambia el atributo a true

        self.entry = True

        pass