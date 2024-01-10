from use_case.create_account import CreateAccountUseCase
from use_case.make_transaction import MakeTransactionUseCase
from use_case.generate_statement import GenerateStatementUseCase
from infrastructure.account_repository import AccountRepository

# Instantiate the repository first
account_repository = AccountRepository()

# Then instantiate use cases
create_account_use_case = CreateAccountUseCase(account_repository)
make_transaction_use_case = MakeTransactionUseCase(account_repository)
generate_statement_use_case = GenerateStatementUseCase(account_repository)

def main():
    try:
        # Example scenario
        new_account = create_account_use_case.create_account(
            customer_id="789",
            name="Jane Doe",
            email="jane.doe@example.com",
            phone_number="789-456-1230"
        )

        print(f"Created Account: {new_account.account_id}")

        make_transaction_use_case.make_transaction(new_account.account_id, 1000, 'deposit')
        make_transaction_use_case.make_transaction(new_account.account_id, 200, 'withdraw')

        account_statement = generate_statement_use_case.generate_account_statement(new_account.account_id)
        print(account_statement)

    except Exception as e:
        print(f"Error in main scenario: {e}")

if __name__ == "__main__":
    main()
