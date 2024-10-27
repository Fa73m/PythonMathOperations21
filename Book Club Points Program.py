# Step 1: Ask for the number of books purchased
books_purchased = int(input("Enter the number of books purchased this month: "))

# Step 2: Determine points based on the number of books
if books_purchased == 0:
    points = 0
elif books_purchased == 2:
    points = 5
elif books_purchased == 4:
    points = 15
elif books_purchased == 6:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0  # This case is unlikely but good for any unexpected inputs

# Step 3: Display the points awarded
print(f"Points awarded: {points}")
