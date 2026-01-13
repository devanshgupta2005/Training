# Program to check if three sides form a valid triangle

# Triangle Inequality Theorem:
# Sum of any two sides > third side
# a + b > c AND b + c > a AND a + c > b

# Input three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if all sides are positive
if a <= 0 or b <= 0 or c <= 0:
    print("Invalid! All sides must be positive numbers.")
# Check triangle inequality theorem
elif a + b > c and b + c > a and a + c > b:
    print(f"Valid Triangle! Sides {a}, {b}, {c} form a valid triangle.")
else:
    print(f"Invalid Triangle! Sides {a}, {b}, {c} do not form a valid triangle.")
