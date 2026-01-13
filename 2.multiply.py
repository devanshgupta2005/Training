# Program to perform multiplication and division

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
multiplication = num1 * num2

# Checking to avoid division by zero
if num2 != 0:
    division = num1 / num2
    print("Multiplication =", multiplication)
    print("Division =", division)
else:
    print("Multiplication =", multiplication)
    print("Division not possible (cannot divide by zero)")
