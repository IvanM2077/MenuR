class Rol():
    def __init__(self, RolId, NameRol):
        self.RolId = RolId
        self.NameRol = NameRol
    def __str__(self):
        return f"{self.RolId} --> {self.NameRol}"
