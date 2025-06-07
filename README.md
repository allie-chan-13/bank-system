# Simple Banking System

## Overview
This is a simple banking system that allows users to manage their bank accounts. Users can create accounts, deposit and withdraw money, transfer funds between accounts, and save the system state to a CSV file.

## Features
- Create a new bank account with a name and starting balance.
- Deposit money into accounts.
- Withdraw money from accounts without overdrafting.
- Transfer money between accounts within the system.
- Save and load system state to/from a CSV file.

## Requirements
- No external libraries are required for basic functionality.

## Running code
```bash
python3 main.py
```

## CLI Menu Instructions

A command-line interface (CLI) menu is set up for interacting with the banking system with the following options:

### Menu Options
1. **Create Account**
   - **Description**: Create a new bank account.
   - **Input**: Users will be prompted to enter account name and  starting balance (must be greater than 0).
   - **Example**: 
     ```
     Enter account name: Alice
     Enter starting balance: 100.0
     ```

2. **Perform Transactions**
   - **Description**: Conduct various transactions on your account.
   - **Input**: Users will be prompted to enter your account name and choose an action:
     - **Deposit**: Add funds to your account.
     - **Withdraw**: Remove funds from your account.
     - **Transfer**: Move funds to another account.
   - **Example**:
     ```
     Enter your account name for transactions: Alice
     Choose action: D for Deposit, W for Withdraw, T for Transfer: D
     Enter amount to deposit: 50.0
     ```

3. **Save to CSV**
   - **Description**: Save the current state of the banking system to a CSV file.
   - **Input**: Account details will be saved to `bank_accounts.csv`.

4. **Exit**
   - **Description**: Exit the banking system.
   - **Input**: Type `X` and press Enter. The program will be terminated.

5. **Notes**
   - **Validation**: Proper valdiation is implemented to ensure software's integrity
   - **Logging** : Appropriate logging are added for CLI Menu to allow smoother flow

## Project Structure
```bash
bank-system/
├── main.py              # Main entry point for the banking system.
├── README.md            # Project documentation.
├── services/            # Contains business logic and models.
│   ├── helpers.py       # Helper functions for validation.
│   ├── logic.py         # Logic for user interactions.
│   └── models.py        # Contains the BankSystem and BankAccount classes.
└── test.py              # Contains unit tests for the banking system.
```

## Running Tests
```bash
python3 tests/test.py
```