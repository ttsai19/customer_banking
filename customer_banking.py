# Import the create_savings_account and create_cd_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt the user to set savings account details
    try:
        savings_balance = float(input("Enter the balance for your savings account: "))
        savings_interest_rate = float(input("Enter the interest rate (as a percentage) for your savings account: "))
        savings_months = int(input("Enter the number of months for your savings account: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for balance, interest rate, and months.")
        return

    # Call create_savings_account function
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance
    print(f"Savings Account:\nInterest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Savings Balance: ${updated_savings_balance:.2f}\n")

    # Prompt the user to set CD account details
    try:
        cd_balance = float(input("Enter the balance for your CD account: "))
        cd_interest_rate = float(input("Enter the interest rate (as a percentage) for your CD account: "))
        cd_months = int(input("Enter the number of months for your CD account: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for balance, interest rate, and months.")
        return

    # Call create_cd_account function
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance
    print(f"CD Account:\nInterest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Balance: ${updated_cd_balance:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
