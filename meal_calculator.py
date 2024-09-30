# Part 1: Meal Calculator Program

# Get the charge for the food from the user
food_charge = float(input("Enter the charge for the food: $"))

# Calculate the tip (18% of the food charge)
tip = food_charge * 0.18

# Calculate the sales tax (7% of the food charge)
sales_tax = food_charge * 0.07

# Calculate the total amount (food charge + tip + sales tax)
total_amount = food_charge + tip + sales_tax

# Display the calculated amounts
print(f"Tip: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
