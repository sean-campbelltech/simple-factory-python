from decimal import Decimal
from .payment import Payment


# ConcreteProductA
class CreditCardPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using a Credit Card")
