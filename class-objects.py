#banking system
class BankAccount:
    def __init__(self, account_holder, balance=0, ):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"

account=BankAccount("John Doe", 1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(2000)
print(account.get_balance())

#restaurant management system
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price
        print(f"Added {item_name} to the menu at ${price:.2f}")

    def remove_menu_item(self, item_name):
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"Removed {item_name} from the menu.")
        else:
            print(f"{item_name} not found in the menu.")

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")
restaurant = Restaurant("Gourmet Bistro")
restaurant.add_menu_item("Pasta", 12.99)
restaurant.add_menu_item("Salad", 8.99)
restaurant.display_menu()

