class User:
    bank_name ="First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name} {self.account_balance}")


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

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(400)
guido.display_user_balance()

monty.make_deposit(400)
monty.make_deposit(600)
monty.make_withdrawal(300)
monty.make_withdrawal(300)
monty.display_user_balance()

nice.make_deposit(800)
nice.make_withdrawal(200)
nice.make_withdrawal(200)
nice.make_withdrawal(200)
nice.display_user_balance()

nice.make_withdrawal(600).make_withdrawal(400).make_deposit(2400).display_user_balance()