# infrastructure/account_repository.py
import sqlite3
from threading import Lock
from domain.account import Account

class AccountRepository:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        self._init_db()
        self.lock = Lock()

    def _init_db(self):
        # Initialize the accounts and transactions tables in the in-memory database
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id TEXT PRIMARY KEY,
                customer_id TEXT,
                account_number TEXT,
                balance REAL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id TEXT,
                date TEXT,
                type TEXT,
                amount REAL,
                FOREIGN KEY (account_id) REFERENCES accounts (account_id)
            )
        ''')
        self.connection.commit()

    def save_account(self, account):
        # Save or update an account in the accounts table
        with self.lock:
            try:
                self.cursor.execute('''
                    INSERT OR REPLACE INTO accounts (account_id, customer_id, account_number, balance)
                    VALUES (?, ?, ?, ?)
                ''', (account.account_id, account.customer_id, account.account_number, account.balance))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Error saving account: {e}")
                raise

    def find_account_by_id(self, account_id):
        # Retrieve an account by its ID from the accounts table
        with self.lock:
            try:
                self.cursor.execute('SELECT * FROM accounts WHERE account_id = ?', (account_id,))
                result = self.cursor.fetchone()

                if result:
                    account_id, customer_id, account_number, balance = result
                    return Account(account_id, customer_id, account_number, balance)

                return None
            except sqlite3.Error as e:
                print(f"Error finding account by ID: {e}")
                raise

    def find_accounts_by_customer_id(self, customer_id):
        # Retrieve all accounts belonging to a customer from the accounts table
        with self.lock:
            try:
                self.cursor.execute('SELECT * FROM accounts WHERE customer_id = ?', (customer_id,))
                results = self.cursor.fetchall()
                accounts = [Account(account_id, customer_id, account_number, balance) for
                            account_id, customer_id, account_number, balance in results]
                return accounts
            except sqlite3.Error as e:
                print(f"Error finding accounts by customer ID: {e}")
                raise

    def save_transaction(self, account_id, transaction_type, amount):
        # Save a transaction in the transactions table
        with self.lock:
            try:
                date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.cursor.execute('''
                    INSERT INTO transactions (account_id, date, type, amount)
                    VALUES (?, ?, ?, ?)
                ''', (account_id, date, transaction_type, amount))
                self.connection.commit()
            except sqlite3.Error as e:
                print(f"Error saving transaction: {e}")
                raise

    def retrieve_transactions(self, account_id):
        # Retrieve transaction history for an account from the transactions table
        with self.lock:
            try:
                self.cursor.execute('SELECT * FROM transactions WHERE account_id = ?', (account_id,))
                results = self.cursor.fetchall()
                transactions = [{'date': date, 'type': transaction_type, 'amount': amount} for
                                transaction_id, _, date, transaction_type, amount in results]
                return transactions
            except sqlite3.Error as e:
                print(f"Error retrieving transactions: {e}")
                raise
