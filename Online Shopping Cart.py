class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, item_to_purchase):
        # Placeholder to add an item to the cart
        pass
    
    def remove_item(self, item_name):
        # Placeholder to remove an item from the cart
        pass
    
    def modify_item(self, item_to_purchase):
        # Placeholder to modify an item in the cart
        pass
    
    def get_num_items_in_cart(self):
        # Placeholder to return the total quantity of items
        pass
    
    def get_cost_of_cart(self):
        # Placeholder to return the total cost of items
        pass
    
    def print_total(self):
        # Placeholder to output the total cost of the cart
        pass
    
    def print_descriptions(self):
        # Placeholder to output each item's description
        pass
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_purchase):
        for item in self.cart_items:
            if item.name == item_to_purchase.name:
                if item_to_purchase.description != "none":
                    item.description = item_to_purchase.description
                if item_to_purchase.price != 0:
                    item.price = item_to_purchase.price
                if item_to_purchase.quantity != 0:
                    item.quantity = item_to_purchase.quantity
                return
        print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity
    
    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost
    
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")
    
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")
def print_menu(cart):
    menu_options = {
        'a': "Add item to cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Output items' descriptions",
        'o': "Output shopping cart",
        'q': "Quit"
    }
    
    while True:
        print("\nMENU")
        for option, description in menu_options.items():
            print(f"{option} - {description}")
        choice = input("Choose an option:\n").lower()
        
        if choice == 'a':
            # Prompt user to add item
            name = input("Enter item name:\n")
            description = input("Enter item description:\n")
            price = int(input("Enter item price:\n"))
            quantity = int(input("Enter item quantity:\n"))
            new_item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(new_item)
        
        elif choice == 'r':
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        
        elif choice == 'c':
            name = input("Enter item name:\n")
            description = input("Enter new description (or leave blank):\n")
            price = input("Enter new price (or leave blank):\n")
            quantity = input("Enter new quantity (or leave blank):\n")
            modified_item = ItemToPurchase(
                name=name,
                description=description if description else "none",
                price=int(price) if price else 0,
                quantity=int(quantity) if quantity else 0
            )
            cart.modify_item(modified_item)
        
        elif choice == 'i':
            cart.print_descriptions()
        
        elif choice == 'o':
            cart.print_total()
        
        elif choice == 'q':
            break
        
        else:
            print("Invalid option. Please try again.")

# Example main function to initialize and run the menu
def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

main()
