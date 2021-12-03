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



class User(BankAccount):
    bank_name ="First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate =0.02, balance=0)
    
    def deposit(self, amount):
        self.account += amount
        return self

    def withdrawal(self, amount):
        self.account -= amount
        return self

    def display_bank_account(self):
        print(f"{self.name} {self.account}")


guido = User("guido VonRossum", "guido@python.com")
monty = User("monty Python", "monty@python.com")
nice = User("Nicety Nice", "niceness@gmail.com")

# banking_users =[guido, monty, nice]

# print(guido.name)
# print(monty.email)
# guido.name = "guido"
# monty.name = "monty"
# print(guido.name)
# print(monty.name)

# guido.deposit(100)
# guido.deposit(100)
# guido.deposit(100)
# guido.make_withdrawal(400)
# guido.display_user_balance()

# monty.deposit(400)
# monty.deposit(600)
# monty.withdrawal(300)
# monty.withdrawal(300)
# monty.display_user_balance()

# nice.deposit(800)
# nice.withdrawal(200)
# nice.withdrawal(200)
# nice.withdrawal(200)
# nice.display_user_balance()

nice.withdrawal(600).withdrawal(400).deposit(2400).display_user_balance()