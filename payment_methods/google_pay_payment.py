from .payment import Payment

class GooglePayPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully paid ${amount} to merchant using Google Pay")