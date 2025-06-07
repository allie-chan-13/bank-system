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
    
    # Call create_account method from BankSystem
    bank.create_account(name, float(balance))


def transfer_funds(bank, from_account):
    
    """Transfer funds to another account."""
    to_account = get_valid_input("Enter the target account name to transfer to: ")

    if to_account not in bank.accounts:
        logging.warning("Target account not found.")
        return

    amount = get_valid_input("Enter amount to transfer: ", validate_positive_number)
    
    # Call transfer method from BankSystem
    bank.transfer(from_account, to_account, float(amount))
    logging.info(f"Transfer completed from {from_account} to {to_account}.")


def perform_transactions(bank):
    """Perform deposit, withdraw, and transfer operations."""
    name = input("Enter your account name for transactions: ")
    
    if name not in bank.accounts:
        logging.warning("Account not found.")
        return

    action = input("Choose action: D for Deposit, W for Withdraw, T for Transfer: ").upper()
    
    if action == 'D':
        amount = get_valid_input("Enter amount to deposit: ", validate_positive_number)
        bank.deposit(name, float(amount))
    elif action == 'W':
        amount = get_valid_input("Enter amount to withdraw: ", validate_positive_number)
        bank.withdraw(name, float(amount))
    elif action == 'T':
        transfer_funds(bank, name)
    else:
        logging.warning("Invalid action selected.")