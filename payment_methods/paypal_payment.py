from decimal import Decimal
from .payment import Payment


# ConcreteProductB
class PayPalPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using PayPal")
