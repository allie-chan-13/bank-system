import csv
import logging

class BankAccount:
    
    def __init__(self, name, balance):
        if balance <= 0:
            raise ValueError("Initial balance must be greater than 0.")
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(f"Deposited ${amount:.2f} to {self.name}'s account.")
        else:
            logging.warning("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            logging.info(f"Withdrew ${amount:.2f} from {self.name}'s account.")
        else:
            logging.warning("Insufficient funds or invalid amount.")

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            logging.info(f"Transferred ${amount:.2f} from {self.name} to {other_account.name}.")
        else:
            logging.warning("Insufficient funds or invalid amount.")

    def __str__(self):
        return f"{self.name}: ${self.balance:.2f}"


class BankSystem:
    
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, starting_balance):
        if name in self.accounts:
            logging.warning("Account already exists.")
        else:
            try:
                self.accounts[name] = BankAccount(name, starting_balance)
                logging.info(f"Account created for {name} with starting balance ${starting_balance:.2f}.")
            except ValueError as e:
                logging.error(e)

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].deposit(amount)
        else:
            logging.warning("Account not found.")

    def withdraw(self, name, amount):
        if name in self.accounts:
            self.accounts[name].withdraw(amount)
        else:
            logging.warning("Account not found.")

    def transfer(self, from_name, to_name, amount):
        if from_name in self.accounts and to_name in self.accounts:
            self.accounts[from_name].transfer(amount, self.accounts[to_name])
        else:
            logging.warning("One or both accounts not found.")

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])
        logging.info(f"System state saved to {filename}.")

    def __str__(self):
        return '\n'.join(str(account) for account in self.accounts.values())