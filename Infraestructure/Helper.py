import re
from tkinter import messagebox

#<editor-fold desc="HelpersVerify">
def verifyIsNumeric(data):
    if data.isnumeric():
        return True
    else:
        messagebox.showerror("Error", "Los datos deben ser numericos")
        return False

def verifyIsAlpha(data):
    if data.isalpha():
        return True
    else:
        messagebox.showerror("Error", "Los datos deben ser caracteres")
        return False

def verifyIsAlphaNumeric(data):
    if data.isalnum():
        return True
    else:
        messagebox.showerror("Error", "Los datos deben ser alfanumericos")
        return False

def verifyIsEmail(data):
    ListData = data.split("@")
    valid_domains = ["gmail.com", "outlook.com", "icloud.com"]
    if len(ListData) == 2 and ListData[1] in valid_domains:
        return True
    else:
        messagebox.showerror("Error", "No es un correo electrónico válido")
        return False

def verifyEmailLogin(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(regex, email):
        return True
    else:
        return False
#</editor-fold>

#<editor-fold desc="Encriptador">
key = 3
pivot = 2
def find(cadena, Char):
    for i, letter in enumerate(cadena):
        if Char == letter:
            return i

def findletter(cadena, index):
    for i, letter in enumerate(cadena):
        if index == i:
            return letter

def encrypt(cadena):
    CadenaEncrpyt = ""
    Alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#$%&/()=¡!¿?;.-_'
    for i, letter in enumerate(cadena):
        index = find(Alphabet, letter)
        newIndex = (key * pivot + index) % len(Alphabet)
        aux = findletter(Alphabet, newIndex)
        print(i, letter, "-->", index, ":", aux)
        CadenaEncrpyt += aux
    return CadenaEncrpyt
#</editor-fold>




#<editor-fold desc="Enum">
def enumRol():
    employeePermission ="Employee"
    adminPermission = "Admin"
    return employeePermission, adminPermission
#</editor-fold>
