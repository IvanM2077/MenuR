'''
Esta clase se especializará en el uso de querys para poder utiizar y accesar a bases
de datos con sql
y poder hacer las consultas SQL

'''
import DB


class OrderNtoN:
    def _init_(self, Id, Usuario, Products):
        self.id =Id
        self.usuario =Usuario
        self.products = Products
        self.paym = False
        self.payconfirm = False

    def SearchOrder(self):
        DB.ConsultaOrdenesDelEmpleado(self.id)
        pass