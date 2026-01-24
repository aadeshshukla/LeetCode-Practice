# grocery store system
class GroceryStore:
    def __init__(self):
        self.inventory = {}
        self.cart = {}

    def add_item_to_inventory(self, item_name, price, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'price': price, 'quantity': quantity}

    def add_item_to_cart(self, item_name, quantity):
        if item_name in self.inventory and self.inventory[item_name]['quantity'] >= quantity:
            if item_name in self.cart:
                self.cart[item_name] += quantity
            else:
                self.cart[item_name] = quantity
            self.inventory[item_name]['quantity'] -= quantity
        else:
            print(f"Sorry, we don't have enough {item_name} in stock.")

    def remove_item_from_cart(self, item_name, quantity):
        if item_name in self.cart and self.cart[item_name] >= quantity:
            self.cart[item_name] -= quantity
            self.inventory[item_name]['quantity'] += quantity
            if self.cart[item_name] == 0:
                del self.cart[item_name]
        else:
            print(f"You don't have enough {item_name} in your cart to remove.")

    def view_cart(self):
        print("Your cart contains:")
        for item_name, quantity in self.cart.items():
            price = self.inventory[item_name]['price']
            print(f"{item_name}: {quantity} @ ${price} each")

    def checkout(self):
        total = 0
        print("Checking out the following items:")
        for item_name, quantity in self.cart.items():
            price = self.inventory[item_name]['price']
            total += price * quantity
            print(f"{item_name}: {quantity} @ ${price} each")
        print(f"Total amount due: ${total}")
        self.cart.clear()
# Example usage
store = GroceryStore()
store.add_item_to_inventory("apple", 0.5, 100)
store.add_item_to_inventory("banana", 0.3, 150)
store.add_item_to_cart("apple", 4)
store.add_item_to_cart("banana", 6)
store.view_cart()
store.checkout()
store.view_cart()
store.remove_item_from_cart("apple", 2)
store.view_cart()
store.add_item_to_cart("apple", 2)
store.view_cart()
store.checkout()

# billing system connected to grocery store
class BillingSystem:
    def __init__(self, grocery_store):
        self.grocery_store = grocery_store

    def generate_bill(self):
        total = 0
        print("Generating bill for the following items:")
        for item_name, quantity in self.grocery_store.cart.items():
            price = self.grocery_store.inventory[item_name]['price']
            total += price * quantity
            print(f"{item_name}: {quantity} @ ${price} each")
        print(f"Total amount due: ${total}")
        return total
# Example usage of BillingSystem
billing_system = BillingSystem(store)
store.add_item_to_cart("apple", 3)
billing_system.generate_bill()
store.checkout()
store.view_cart()
