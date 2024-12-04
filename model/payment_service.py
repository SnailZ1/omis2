class PaymentService:
    def __init__(self, payment_repository, account_service):
        self.payment_repository = payment_repository
        self.account_service = account_service

    def process_payment(self, account_id, amount):
        account_balance = self.account_service.get_account_balance(account_id)
        if account_balance and account_balance >= amount:
            self.account_service.withdraw(account_id, amount)
            payment = PaymentModel(payment_id=len(self.payment_repository.payments) + 1, amount=amount, payment_date="2024-12-04")
            self.payment_repository.save_payment(payment)
            return True
        return False