# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is your initial saving acount balance? "))
    saving_interest = float(input("What is your APR for your saving account? "))
    months = int(input("How old is your saving account in months? "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_saving_balance, interest_earned = create_savings_account(savings_balance,saving_interest, months)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned: $," f"{interest_earned:,.2f}")
    print("Updated saving account balance with interest: $," f"{updated_saving_balance:,.2f}")
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_months = int(input('How old is your CD account in months? '))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"interest_earned on CD account: {interest_earned:.2f}")
    print(f"Updated cd account balance with interest earned:{updated_cd_balance:.2f}")
    # Call the main function.
if __name__ == "__main__":
    main()