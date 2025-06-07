import logging
from services.models import BankSystem
from services.logic import create_account, perform_transactions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    
    bank = BankSystem()

    while True:
        logging.info("\nControl Menu:")
        logging.info("1. Create Account")
        logging.info("2. Perform Transactions")
        logging.info("3. Save to CSV")
        logging.info("X. Exit")
        
        choice = input("Select an option: ").upper()

        if choice == '1':
            create_account(bank)
        elif choice == '2':
            perform_transactions(bank)
        elif choice == '3':
            bank.save_to_csv("bank_accounts.csv")
        elif choice == 'X':
            logging.info("Exiting the banking system.")
            break
        else:
            logging.warning("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()