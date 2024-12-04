class PaymentController:
    def __init__(self, payment_service, payment_view):
        self.payment_service = payment_service
        self.payment_view = payment_view
        self.connect_view()

    def connect_view(self):
        self.payment_view.on_process_payment = self.on_process_payment

    def on_process_payment(self, account_id, amount):
        if self.payment_service.process_payment(account_id, amount):
            self.payment_view.show_message("Платеж успешно обработан!")
        else:
            self.payment_view.show_message("Недостаточно средств на счете.")