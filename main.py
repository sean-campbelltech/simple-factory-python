from dynamic_payment_factory import DynamicPaymentFactory
from payment_factory import PaymentFactory
from payment_method import PaymentMethod


def main():
    # factory = DynamicPaymentFactory()
    # payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    factory = DynamicPaymentFactory()
    payment = factory.create("CreditCardPayment")
    payment.pay(1000.00)


if __name__ == "__main__":
    main()
