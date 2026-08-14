# EXERCISE
# Create a class for a bank account. Allow a user to deposit and withdraw funds.
# Throw a custom error if there are insufficient funds for a withdrawal.
# Also prevent the account balance from being manually accessed.

# The use of a custom error type aids in debugging. If we see an InsufficientFundsError
# in the logs, we know this class was involved.
class InsuffientFundsError(ValueError):
    # Raised if there is a withdrawal against insuffient funds
    pass

class BankAccount:
    def __init__(self, balance: float = 0.00):
        # Preceding the name of the balance property with two underscores tells 
        # Python to treat this as a private property. Essentially, this transforms
        # the name of the balance property to _BankAccount__balance. While it is still
        # technically accessible via that name, this prevents accidentally overwriting
        # the property in code outside the class.
        self.__balance = balance

    def deposit(self, funds: float):
        self.__balance += funds

    def withdraw(self, funds: float):
        if funds > self.__balance:
            raise InsuffientFundsError('Insufficient Funds.')
        else:
            self.__balance -= funds

    # This set up a "get" handling method for our balance. This makes BankAccount.balance
    # accessible for reading. Because we did not set up a setter method, this makes the 
    # property read-only. It must be modified through the despoit and withdraw methods.
    @property
    def balance(self):
        return self.__balance

# Example usage.
# This block only runs when the script is run directly (i.e. not imported).
if __name__ == '__main__':
    myBank = BankAccount(1000)
    print(f"Balance #1: {myBank.balance}")
    myBank.deposit(200)
    print(f"Balance #2: {myBank.balance}")
    myBank.withdraw(700)
    print(f"Balance #3: {myBank.balance}")
    try:
        myBank.balance = 10000
    except AttributeError:
        print('Confirmed that manually setting the balance is not permitted.')    
    print(f"Balance #4: {myBank.balance}")
    try:
        myBank.withdraw(600)
    except InsuffientFundsError:
        print('Attempt to withdraw more funds than available not permitted.')
    print(f"Balance #5: {myBank.balance}")

    