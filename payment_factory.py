from payment_method import PaymentMethod
from payment_methods import CreditCardPayment, PayPalPayment, GooglePayPayment


# Creator
class PaymentFactory:
    @staticmethod
    def create(payment_method: PaymentMethod):
        match payment_method:
            case PaymentMethod.CREDIT_CARD:
                return CreditCardPayment()
            case PaymentMethod.PAYPAL:
                return PayPalPayment()
            case PaymentMethod.GOOGLE_PAY:
                return GooglePayPayment()
            case _:
                raise ValueError(
                    f"{payment_method} is not currently supported as a payment method."
                )
