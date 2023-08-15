from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully paid ${amount} to merchant using a Credit Card")