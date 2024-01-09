# main.py
from use_case.create_account import CreateAccountUseCase
from use_case.make_transaction import MakeTransactionUseCase
from use_case.generate_statement import GenerateStatementUseCase
from infrastructure.account_repository import AccountRepository

# Instantiate use cases and repository
create_account_use_case = CreateAccountUseCase()
make_transaction_use_case = MakeTransactionUseCase()
generate_statement_use_case = GenerateStatementUseCase()
account_repository = AccountRepository()

# Example scenario
new_account = create_account_use_case.create_account(
    customer_id="789",
    name="Jane Doe",
    email="jane.doe@example.com",
    phone_number="789-456-1230"
)

print(f"Created Account: {new_account.account_id}")

make_transaction_use_case.make_transaction(new_account, 1000, 'deposit')
make_transaction_use_case.make_transaction(new_account, 200, 'withdraw')

account_statement = generate_statement_use_case.generate_account_statement(new_account)
print(account_statement)
