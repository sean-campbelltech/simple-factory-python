from payment_method import PaymentMethod
from payment_methods import CreditCardPayment, PayPalPayment, GooglePayPayment


# Creator
class PaymentFactory:
    @staticmethod
    def create(paymentMethod: PaymentMethod):
        match paymentMethod:
            case PaymentMethod.CREDIT_CARD:
                return CreditCardPayment()
            case PaymentMethod.PAYPAL:
                return PayPalPayment()
            case PaymentMethod.GOOGLE_PAY:
                return GooglePayPayment()
            case _:
                raise ValueError(
                    f"{paymentMethod} is not currently supported as a payment method."
                )
