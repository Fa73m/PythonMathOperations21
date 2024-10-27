# Step 1: Ask for the number of years
years = int(input("Enter the number of years: "))

# Step 2: Initialize variables
total_rainfall = 0  # To accumulate the total rainfall
total_months = years * 12  # Calculate the total months

# Step 3: Outer loop for each year
for year in range(1, years + 1):
    print(f"\nYear {year}")
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter inches of rainfall for month {month}: "))
        total_rainfall += rainfall

# Step 4: Calculate the average rainfall
average_rainfall = total_rainfall / total_months

# Step 5: Display the results
print(f"\nTotal months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month: {average_rainfall:.2f}")
