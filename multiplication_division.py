# Part 2: Multiplication and Division
# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform multiplication
product_result = num1 * num2

# Perform division with check for division by zero
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "undefined (division by zero is not allowed)"

# Display results
print(f"The product of {num1} and {num2} is: {product_result}")
print(f"The result of dividing {num1} by {num2} is: {division_result}")
