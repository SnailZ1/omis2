class AccountRepository:
    def __init__(self):
        self.accounts = []

    def save_account(self, account):
        self.accounts.append(account)

    def get_account(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None