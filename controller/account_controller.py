class AccountController:
    def __init__(self, account_service, account_view):
        self.account_service = account_service
        self.account_view = account_view
        self.connect_view()

    def connect_view(self):
        self.account_view.on_check_balance = self.on_check_balance
        self.account_view.on_deposit = self.on_deposit
        self.account_view.on_withdraw = self.on_withdraw

    def on_check_balance(self, account_id):
        balance = self.account_service.get_account_balance(account_id)
        if balance is not None:
            self.account_view.show_balance(balance)
        else:
            self.account_view.show_message("Счет не найден.")

    def on_deposit(self, account_id, amount):
        if self.account_service.deposit(account_id, amount):
            self.account_view.show_message("Пополнение успешно!")
        else:
            self.account_view.show_message("Ошибка при пополнении.")

    def on_withdraw(self, account_id, amount):
        if self.account_service.withdraw(account_id, amount):
            self.account_view.show_message("Снятие успешно!")
        else:
            self.account_view.show_message("Ошибка при снятии.")