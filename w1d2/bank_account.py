# class BankAccount:
#     # don't forget to add some default values for these parameters!
#     def __init__(self, int_rate, balance):
#     account_balance = 0 
#     def deposit(self, amount):
#         # your code here
#     def withdraw(self, amount):
#         # your code here
#     def display_account_info(self):
#         # your code here
#     def yield_interest(self):
#         # your code here

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_bank_account(self):
        print(f"{int(self.balance)}") #need f here?
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
            return f"{int(self.balance)}"
        else:
            return self.balance
account_1 = BankAccount(1.005, 1000)
account_2 = BankAccount(1.007, 1200)


account_1.deposit(100).deposit(300).deposit(150).withdrawal(1000).yield_interest()
account_1.display_bank_account()
    
account_2.deposit(700).deposit(900).withdrawal(1600).withdrawal(900).withdrawal(3200).withdrawal(6).yield_interest()
account_2.display_bank_account()
