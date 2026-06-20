class payment:
    def __init__(self, amount):
        self.amount=amount
    def pay(self):
        print("Processing payment of:", self.amount)

class CreditCardPayment(payment):
    pass
class UPIPayment(payment):
    pass

p1= CreditCardPayment(500)
p1.pay()

p2= UPIPayment(1000)
p2.pay()