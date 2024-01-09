
import unittest
from use_case.create_account import CreateAccountUseCase
from infrastructure.account_repository import AccountRepository

class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        self.create_account_use_case = CreateAccountUseCase()
        self.account_repository = AccountRepository()

    def test_create_account(self):
        new_account = self.create_account_use_case.create_account(
            customer_id="123",
            name="John Doe",
            email="john.doe@example.com",
            phone_number="123-456-7890"
        )
        self.assertIsNotNone(new_account)
        self.assertEqual(new_account.customer_id, "123")
        self.assertEqual(new_account.balance, 0)

        customer_accounts = self.account_repository.find_accounts_by_customer_id("123")
        self.assertEqual(len(customer_accounts), 1)

if __name__ == '__main__':
    unittest.main()
