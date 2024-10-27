class ItemToPurchase:
    # Constructor to set up initial values for attributes
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name      # Name of the item
        self.item_price = item_price    # Price of each item
        self.item_quantity = item_quantity  # Quantity of items

    # Method to print the cost of the item
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")
# Item 1
print("Item 1")
item_name_1 = input("Enter the item name:\n")
item_price_1 = float(input("Enter the item price:\n"))
item_quantity_1 = int(input("Enter the item quantity:\n"))

# Create the first item object using user input
item1 = ItemToPurchase(item_name=item_name_1, item_price=item_price_1, item_quantity=item_quantity_1)

# Item 2
print("\nItem 2")
item_name_2 = input("Enter the item name:\n")
item_price_2 = float(input("Enter the item price:\n"))
item_quantity_2 = int(input("Enter the item quantity:\n"))

# Create the second item object using user input
item2 = ItemToPurchase(item_name=item_name_2, item_price=item_price_2, item_quantity=item_quantity_2)
# Output the total cost
print("\nTOTAL COST")
item1.print_item_cost()
item2.print_item_cost()

# Calculate the total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost}")
