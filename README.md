# Banking System Application
 ##Python_version 
 Python 3.8.11  
## Overview
This repository contains a simplified version of a banking system application, developed following the clean architecture principles. The system is organized into three layers: Domain, Use Case, and Infrastructure.

### Layers
1. **Domain Layer:**
   - Entities: Account, Customer
   - Methods: deposit(), withdraw(), get_balance()

2. **Use Case Layer:**
   - Use Cases: Create Account, Make Transaction, Generate Statement
   - Business Logic: Operations related to creating accounts, making transactions, and generating statements.

3. **Infrastructure Layer:**
   - Repository: AccountRepository
   - Interaction with the outside world: Data storage, external service integrations.

## Implementation

### 1. Entities

#### Account
- Attributes: account_id, customer_id, account_number, balance
- Methods: deposit(), withdraw(), get_balance()

#### Customer
- Attributes: customer_id, name, email, phone_number

### 2. Use Case Classes

#### CreateAccountUseCase
- Method: create_account(customer_id, name, email, phone_number)
- Lazy Loading: Objects created on need basis using Builder pattern.

#### MakeTransactionUseCase
- Method: make_transaction(account_id, amount, transaction_type)
- Updates account balance based on transaction type.

#### GenerateStatementUseCase
- Method: generate_account_statement(account_id)
- Retrieves transaction history and generates account statement.

### 3. Infrastructure

#### AccountRepository
- Methods: save_account(), find_account_by_id(), find_accounts_by_customer_id()

## Testing

### Test Cases
- Test each use case with proper test data.
- Ensure assertions for correctness in test cases.
- Cover all service (Use Case) methods with appropriate data simulation.

### Running Tests
Execute individual test scripts in the `tests` folder.

```bash
python -m unittest tests/test_create_account.py
python -m unittest tests/test_make_transaction.py
python -m unittest tests/test_generate_statement.py





