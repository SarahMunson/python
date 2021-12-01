class User:
    bank_name ="First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name} {self.account_balance}")


guido = User("guido VonRossum", "guido@python.com")
monty = User("monty Python", "monty@python.com")
nice = User("Nicety Nice", "niceness@gmail.com")

banking_users =[guido, monty, nice]

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
print(guido.display_user_balance())

monty.make_deposit(400)
monty.make_deposit(600)
monty.make_withdrawal(300)
monty.make_withdrawal(300)
print(monty.display_user_balance())

nice.make_deposit(800)
nice.make_withdrawal(200)
nice.make_withdrawal(200)
nice.make_withdrawal(200)
print(nice.display_user_balance())