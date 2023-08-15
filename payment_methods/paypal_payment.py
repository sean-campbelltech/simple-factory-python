from .payment import Payment

class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f"Successfully paid ${amount} to merchant using PayPal")