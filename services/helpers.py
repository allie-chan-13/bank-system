"""
General helper functions for basic operations
"""

def validate_account_name(name):
    
    """Validate account name."""
    if not (1 <= len(name) <= 50):
        raise ValueError("Account name must be between 1 and 50 characters.")


def validate_positive_number(value):
    
    """Validate that the input is a positive number."""
    num = float(value)
    if num <= 0:
        raise ValueError("Value must be greater than 0.")