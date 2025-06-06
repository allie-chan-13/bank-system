import logging
from services.helpers import validate_account_name, validate_positive_number


def get_valid_input(prompt, validation_func):
    """Prompt user for input until valid input is received."""
    
    while True:
        user_input = input(prompt)
        try:
            validation_func(user_input)
            return user_input
        except ValueError as e:
            logging.warning(e)


def create_account(bank):
    """Create a new bank account from user input."""
    
    name = get_valid_input("Enter account name: ", validate_account_name)
    balance = get_valid_input("Enter starting balance: ", validate_positive_number)
    bank.create_account(name, float(balance))


def perform_transactions(bank):
    """Perform deposit and withdraw operations."""
    
    name = input("Enter your account name for transactions: ")
    
    if name not in bank.accounts:
        logging.warning("Account not found.")
        return

    action = input("Choose action: D for Deposit, W for Withdraw: ").upper()
    
    if action == 'D':
        amount = get_valid_input("Enter amount to deposit: ", validate_positive_number)
        bank.deposit(name, float(amount))
    elif action == 'W':
        amount = get_valid_input("Enter amount to withdraw: ", validate_positive_number)
        bank.withdraw(name, float(amount))
    else:
        logging.warning("Invalid action selected.")