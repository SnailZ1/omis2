class PaymentRepository:
    def __init__(self):
        self.payments = []

    def save_payment(self, payment):
        self.payments.append(payment)

    def get_payment(self, payment_id):
        for payment in self.payments:
            if payment.payment_id == payment_id:
                return payment
        return None