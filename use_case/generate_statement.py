from infrastructure.account_repository import AccountRepository

class GenerateStatementUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        try:
            # Retrieve the account from the repository
            account = self.account_repository.find_account_by_id(account_id)

            if not account:
                raise ValueError(f"Account with ID {account_id} not found.")

            # Retrieve transaction history from the repository
            transactions = self.retrieve_transaction_history(account)

            # Generate the account statement
            statement = f"Account Statement for Account ID {account.account_id}:\n"
            for transaction in transactions:
                statement += f"{transaction['date']} - {transaction['type']} ${transaction['amount']}\n"

            return statement

        except Exception as e:
            # Handle any unexpected errors
            print(f"Error generating account statement: {e}")
            raise

    def retrieve_transaction_history(self, account):
        try:
            # Retrieve transaction history from the repository
            transactions = self.account_repository.retrieve_transactions(account.account_id)

            # Convert the transactions to the desired format (list of dictionaries)
            return [{'date': transaction['date'], 'type': transaction['type'], 'amount': transaction['amount']}
                    for transaction in transactions]

        except Exception as e:
            # Handle any unexpected errors during transaction retrieval
            print(f"Error retrieving transaction history: {e}")
            raise
