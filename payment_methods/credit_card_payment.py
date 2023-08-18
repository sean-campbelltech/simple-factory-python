from decimal import Decimal
from .payment import Payment


class CreditCardPayment(Payment):
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merchant using a Credit Card")
