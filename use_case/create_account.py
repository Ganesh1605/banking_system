from domain.account import Account
from domain.customer import Customer

class CreateAccountUseCase:
    def create_account(self, customer_id, name, email, phone_number):
        account_number = self.generate_account_number()
        return Account(account_id=self.generate_unique_id(), customer_id=customer_id, account_number=account_number)

    def generate_account_number(self):
        # Implement logic to generate account numbers
        return f"ACC-{self.generate_unique_id()[:8]}"

    def generate_unique_id(self):
        # Implement logic to generate unique IDs
        return "test_id"  # Replace with your implementation
