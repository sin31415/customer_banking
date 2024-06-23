# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = input('Enter your savings balance: ')
    savings_interest = input('Enter your interest rate: ')
    savings_maturity = input('Enter the number of months for the savings account: ')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    if updated_savings_balance >= 0 and interest_earned >=0:
        print(f"The interest earned for your savings account is ${interest_earned: ,.2F} after which the updated savings account balance is ${updated_savings_balance: ,.2F} for the maturity length of {savings_maturity} months.")
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input('Enter your CD account balance: ')
    cd_interest = input('Enter your interest rate: ')
    cd_maturity = input('Enter the number of months for the savings account: ')
    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    if updated_cd_balance >= 0 and interest_earned >=0:
        print(f"The interest earned for your CD account is ${interest_earned: ,.2F} after which the updated CD account balance is ${updated_cd_balance: ,.2F} for the maturity length of {cd_maturity} months.")

if __name__ == "__main__":
    # Call the main function.
    main()
