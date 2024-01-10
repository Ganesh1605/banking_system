# banking_system/tests/test_make_transaction.py
import unittest
from use_case.make_transaction import MakeTransactionUseCase
from infrastructure.account_repository import AccountRepository
from domain.account import Account

class TestMakeTransaction(unittest.TestCase):
    def setUp(self):
        self.account_repository = AccountRepository()
        self.make_transaction_use_case = MakeTransactionUseCase(self.account_repository)

    def test_make_transaction(self):
        account_id = "1"
        initial_balance = 1000
        amount = 1500
        account = Account(account_id=account_id, customer_id="123", account_number="ACC123", balance=initial_balance)
        self.account_repository.save_account(account)

        with self.assertRaises(ValueError) as context:
            self.make_transaction_use_case.make_transaction(account_id, amount, 'withdraw')

        self.assertEqual(str(context.exception), "Insufficient funds")

if __name__ == '__main__':
    unittest.main()
