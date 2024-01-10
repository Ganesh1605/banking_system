# use_case/create_account.py
from domain.account import Account
from domain.customer import Customer
import uuid
from infrastructure.account_repository import AccountRepository

class CreateAccountUseCase:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number):
        try:
            # Check if an account already exists for the given customer_id
            existing_account = self.account_repository.find_accounts_by_customer_id(customer_id)
            if existing_account:
                raise ValueError("An account already exists for this customer.")

            # Generate a unique account number
            account_number = self.generate_account_number()

            # Create a new account
            new_account = Account(account_id=self.generate_unique_id(), customer_id=customer_id, account_number=account_number)

            # Save the new account
            self.account_repository.save_account(new_account)

            return new_account
        except Exception as e:
            print(f"Error creating account: {e}")
            raise

    def generate_account_number(self):
        # Implement logic to generate account numbers
        return f"ACC-{self.generate_unique_id()[:8]}"

    def generate_unique_id(self):
        # Generate a numeric unique ID using uuid
        return str(uuid.uuid4().int)[:10]  # Use the first 10 digits of the UUID
