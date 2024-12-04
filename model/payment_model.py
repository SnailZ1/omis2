class PaymentModel:
    def __init__(self, payment_id=None, amount=0.0, payment_date=None):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = payment_date