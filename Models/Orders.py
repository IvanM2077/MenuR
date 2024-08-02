'''
Esta clase se especializará en el uso de querys para poder utiizar y accesar a bases
de datos con sql
y poder hacer las consultas SQL

'''
class Orders:
    def __init__(self,OrderId, UserId, Payment = False, PaymentConfirm=False):
        self.OrderId =OrderId
        self.UserId =UserId
        self.Payment = Payment
        self.PaymentConfirm = PaymentConfirm

Ordenes = Orders("a","b")