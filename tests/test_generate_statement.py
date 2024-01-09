
import unittest
from use_case.generate_statement import GenerateStatementUseCase
from infrastructure.account_repository import AccountRepository
from domain.account import Account

class TestGenerateStatement(unittest.TestCase):
    def setUp(self):
        self.generate_statement_use_case = GenerateStatementUseCase()
        self.account_repository = AccountRepository()

    def test_generate_account_statement(self):
        account_id = "2"
        initial_balance = 1000

        # Create a test account with initial balance
        test_account = Account(account_id=account_id, customer_id="456", account_number="ACC456", balance=initial_balance)
        self.account_repository.save_account(test_account)

        # Generate an account statement
        statement = self.generate_statement_use_case.generate_account_statement(test_account)

        # Verify the statement content
        self.assertIn(f"Account Statement for Account ID {account_id}:", statement)
        self.assertIn(f"Initial Balance: ${initial_balance}", statement)

if __name__ == '__main__':
    unittest.main()
