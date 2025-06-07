import unittest
import logging
from services.models import BankSystem, BankAccount

class TestBankSystem(unittest.TestCase):

    def setUp(self):
        """Set up a new bank system for testing."""
        self.bank = BankSystem()

    def test_create_account(self):
        
        """Test creating a new account."""
        self.bank.create_account("Alice", 100.0)
        self.assertIn("Alice", self.bank.accounts)
        self.assertEqual(self.bank.accounts["Alice"].balance, 100.0)

    def test_create_account_duplicate(self):
        
        """Test creating a duplicate account."""
        self.bank.create_account("Alice", 100.0)
        self.bank.create_account("Alice", 200.0)
        self.assertEqual(self.bank.accounts["Alice"].balance, 100.0)

    def test_deposit(self):
        
        """Test depositing money into an account."""
        self.bank.create_account("Alice", 100.0)
        self.bank.deposit("Alice", 50.0)
        self.assertEqual(self.bank.accounts["Alice"].balance, 150.0)

    def test_withdraw(self):
        
        """Test withdrawing money from an account."""
        self.bank.create_account("Alice", 100.0)
        self.bank.withdraw("Alice", 50.0)
        self.assertEqual(self.bank.accounts["Alice"].balance, 50.0)

    def test_withdraw_insufficient_funds(self):
        
        """Test withdrawing more than the balance."""
        self.bank.create_account("Alice", 100.0)
        self.bank.withdraw("Alice", 150.0)  # Should not allow
        self.assertEqual(self.bank.accounts["Alice"].balance, 100.0)

    def test_transfer(self):
        """Test transferring money between accounts."""
        
        self.bank.create_account("Alice", 100.0)
        self.bank.create_account("Bob", 50.0)
        self.bank.transfer("Alice", "Bob", 50.0)
        self.assertEqual(self.bank.accounts["Alice"].balance, 50.0)
        self.assertEqual(self.bank.accounts["Bob"].balance, 100.0)

    def test_transfer_insufficient_funds(self):
        """Test transferring more than the balance."""
        
        self.bank.create_account("Alice", 100.0)
        self.bank.create_account("Bob", 50.0)
        self.bank.transfer("Alice", "Bob", 150.0)  # Should not allow
        self.assertEqual(self.bank.accounts["Alice"].balance, 100.0)
        self.assertEqual(self.bank.accounts["Bob"].balance, 50.0)

    def test_save_to_csv(self):
        """Test saving accounts to a CSV file."""
        self.bank.create_account("Alice", 100.0)
        self.bank.create_account("Bob", 50.0)
        self.bank.save_to_csv("test_accounts.csv")

        # Check if the CSV file was created and contains the correct data
        with open("test_accounts.csv", mode='r') as file:
            lines = file.readlines()
            self.assertIn("Alice,100.0\n", lines)
            self.assertIn("Bob,50.0\n", lines)

    def tearDown(self):
        """Clean up any created files or resources after tests."""
        import os
        try:
            os.remove("test_accounts.csv")
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    unittest.main()