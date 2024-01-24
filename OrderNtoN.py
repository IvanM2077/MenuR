'''
Esta clase se especializará en el uso de querys para poder utiizar y accesar a bases
de datos con sql
y poder hacer las consultas SQL

'''
import DB


class OrderNtoN:
    def _init_(self, Id, Usuario, Products, Delivery, PayM, PayConfirm):
        self.id =Id
        self.usuario =Usuario
        self.Products = Products
        self.delivery = Delivery
        self.paym = PayM
        self.payconfirm = PayConfirm

    def SearchOrder(self):
        DB.ConsultaOrdenesDelEmpleado(self.id)
        pass