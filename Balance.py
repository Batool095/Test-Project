class Account:
    def __init__(self, X = 0):
        self.balance = X

    def bank_deposit(self,x):
        self.balance = self.balance + x
        return self.balance

    def bank_withdraw(self,x):
        self.balance = self.balance - x
        return self.balance


class Bank:
    def __init__(self, x , bank_name:str):
        self.bank_name = bank_name
        self.balance = x

    def bank_deposit(self,x):
        self.balance = self.balance + x
        return self.balance

    def bank_withdraw(self,x):
        self.balance = self.balance - x
        return self.balance


