class AccountRepository:
    accounts = {}

    def save_account(self, account):
        self.accounts[account.account_id] = account

    def find_account_by_id(self, account_id):
        return self.accounts.get(account_id)

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts.values() if account.customer_id == customer_id]
