class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def get_account_balance(self, account_id):
        account = self.account_repository.get_account(account_id)
        if account:
            return account.balance
        return None

    def deposit(self, account_id, amount):
        account = self.account_repository.get_account(account_id)
        if account:
            account.balance += amount
            return True
        return False

    def withdraw(self, account_id, amount):
        account = self.account_repository.get_account(account_id)
        if account and account.balance >= amount:
            account.balance -= amount
            return True
        return False