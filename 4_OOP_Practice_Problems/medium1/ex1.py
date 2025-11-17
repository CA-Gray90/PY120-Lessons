class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance

'''
A:
Alyssa is correct since we can use the property method balance to access the 
value of self._balance in balance_is_positive'''
