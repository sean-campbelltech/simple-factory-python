from payment_factory import PaymentFactory


def main():
    factory = PaymentFactory()
    payment = factory.create("GooglePayPayment")
    payment.pay(1000.00)


if __name__ == "__main__":
    main()
