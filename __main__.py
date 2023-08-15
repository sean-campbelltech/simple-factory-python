from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create("CreditCardPayment1")
payment.pay(1000)
