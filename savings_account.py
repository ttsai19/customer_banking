from Account import Account

def create_savings_account(balance, apr, months):
    """
    Creates a savings account and calculates the interest earned over a given number of months.

    Args:
        balance (float): The initial balance of the savings account.
        apr (float): The annual percentage rate (APR) as a percentage.
        months (int): The number of months the interest will be calculated for.

    Returns:
        updated_balance (float): The new balance after interest is added.
        interest_earned (float): The total interest earned over the specified period.
    """
    
    # Create an instance of Account with the initial balance and 0 interest
    savings_account = Account(balance, 0)

    # Calculate the interest earned
    interest_earned = balance * (apr / 100 * months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Set the updated balance in the Account instance
    savings_account.set_balance(updated_balance)

    # Set the interest earned in the Account instance (fixed method)
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
