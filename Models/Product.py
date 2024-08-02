'''
Clase producto aquí se diseñara las propiedades del producto para
dar de alta como administrador

'''

class Product:
    #constructor de la clase
    def __init__(self, ProductId, Item, Description,Price):
        self.ProductId = ProductId
        self.Item= Item
        self.Description = Description
        self.Price = Price



