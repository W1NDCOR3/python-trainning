class AccountDispatcher:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.id] = account

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")

        return self.accounts.get(account_id)

    def remove_account(self, account_id):
        if not account_id in self.accounts:
            raise ValueError(f"Account {account_id} not found")

        return self.accounts.pop(account_id, None)