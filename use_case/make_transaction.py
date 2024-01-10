from infrastructure.account_repository import AccountRepository

class MakeTransactionUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        # Retrieve the account from the repository
        account = self.account_repository.find_account_by_id(account_id)

        if not account:
            raise ValueError(f"Account with ID {account_id} not found.")

        try:
            # Perform the transaction based on the transaction type
            if transaction_type == 'deposit':
                account.deposit(amount)
            elif transaction_type == 'withdraw':
                account.withdraw(amount)
            else:
                raise ValueError("Invalid transaction type. Supported types are 'deposit' and 'withdraw'.")

            # Save the updated account back to the repository
            self.account_repository.save_account(account)
        except ValueError as e:
            # Handle insufficient funds or other errors
            raise ValueError(str(e))
