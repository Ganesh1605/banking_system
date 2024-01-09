
import unittest
from use_case.make_transaction import MakeTransactionUseCase
from infrastructure.account_repository import AccountRepository
from domain.account import Account

class TestMakeTransaction(unittest.TestCase):
    def setUp(self):
        self.make_transaction_use_case = MakeTransactionUseCase()
        self.account_repository = AccountRepository()

    def test_make_transaction(self):
        account_id = "1"
        initial_balance = 1000
        amount = 500

        # Create a test account with initial balance
        test_account = Account(account_id=account_id, customer_id="123", account_number="ACC123", balance=initial_balance)
        self.account_repository.save_account(test_account)

        # Make a transaction
        self.make_transaction_use_case.make_transaction(test_account, amount, 'withdraw')

        # Verify the updated balance
        updated_account = self.account_repository.find_account_by_id(account_id)
        self.assertIsNotNone(updated_account)
        self.assertEqual(updated_account.balance, initial_balance - amount)

if __name__ == '__main__':
    unittest.main()
