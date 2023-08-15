from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create("CreditCardPayment")
payment.pay(1000)
