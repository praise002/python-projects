class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details:")
        print()
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super(Bank, self).__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Account balance:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds\nBalance available:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance:", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance:", self.balance)


user = Bank("Praise", "21", "F")
user.show_details()
user.deposit(1000)
user.withdraw(500)
user.withdraw(5000)
user.view_balance()
