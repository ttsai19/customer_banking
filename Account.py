class Account:
    def __init__(self, balance=0, interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest_rate = interest

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.interest_rate
