##Salary Increment Logic
salary = float(input("Enter the employee salary: "))

if salary < 30000:
    new_salary = salary * 1.20
elif salary >= 30000 and salary < 60000:
    new_salary = salary * 1.10
else:
    new_salary = salary

print("New Salary:", new_salary)


## Multiple Conditions Check
num = int(input("Enter an integer: "))

if num % 3 == 0 and num % 4 == 0:
    print("The number is divisible by both 3 and 4")
elif (num % 3 == 0) or (num % 4 == 0):
    print("The number is divisible by only one of them")
else:
    print("The number is divisible by none")


##Bill Discount Calculator
bill = float(input("Enter bill amount: "))
payment_mode = input("Enter payment mode (card/cash): ").lower()
customer_type = input("Enter customer type (premium/regular): ").lower()

if bill > 5000 and payment_mode == "card":
    discount = 0.15
elif (bill > 5000 or customer_type == "premium"):
    discount = 0.10
else:
    discount = 0.0

final_bill = bill * (1 - discount)

print("Final Bill Amount:", final_bill)


## Even–Odd and Range Check
num = int(input("Enter a number: "))

if num % 2 == 0 and 50 <= num <= 100:
    print("Even and between 50–100")
elif num % 2 != 0 and num > 100:
    print("Odd and greater than 100")
else:
    print("Invalid Category")


##Assignment Operator Tracker
x = int(input("Enter a number: "))

x += 10      # Step 1
x *= 2       # Step 2
x -= 5       # Step 3

# print("Final value:", x)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b < c:
    print("Increasing Order")
else:
    print("Not Increasing")


##Login Attempt Validator

# Maximum allowed login attempts
MAX_ATTEMPTS = 3

username = input("Enter username: ")
password = input("Enter password: ")
login_attempts = int(input("Enter number of login attempts so far: "))

# Check login eligibility
if login_attempts >= MAX_ATTEMPTS:
    print("Login Denied: Maximum attempts reached.")
elif username != "admin":
    print("Login Denied: Incorrect username.")
elif len(password) < 6:
    print("Login Denied: Password too short. Must be at least 6 characters.")
else:
    print("Login Allowed")


##Mathematical Expression Evaluation

# Take inputs
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Evaluate the expression
result = (a + b) ** 2 > a**2 + b**2 + c

# Print the result
print("Expression is", result)


#Divisibility Priority
num = int(input("Enter a number: "))

if num % 2 == 0 and num % 5 == 0:
    print("Divisible by 2 and 5")
elif num % 2 == 0:
    print("Divisible by only 2")
elif num % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 2 or 5")


##10 Income Tax Slab

# Take income input
income = float(input("Enter your income in rupees: "))

# Calculate tax
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.10
else:
    tax = income * 0.20

print("Tax amount:", tax, "rupees")


##Student Grading System (Nested if)

# Take marks input
marks = float(input("Enter marks: "))

# Determine grade
if marks >= 90:
    grade = "A"
    print("Grade:", grade)
    print("Excellent")
elif marks >= 75:
    grade = "B"
    print("Grade:", grade)
elif marks >= 60:
    grade = "C"
    print("Grade:", grade)
else:
    grade = "Fail"
    print("Grade:", grade)


##Electricity Bill Calculation
# Input units consumed
units = int(input("Enter units consumed: "))

# Initialize bill
bill = 0

# Calculate bill using nested conditions
if units <= 100:
    bill = units * 5
else:
    bill = 100 * 5  # First 100 units
    if units <= 200:
        bill += (units - 100) * 7  # Next 100 units
    else:
        bill += 100 * 7             # Units 101-200
        bill += (units - 200) * 10  # Above 200 units

print("Total bill: ₹", bill)


##13 ATM Withdrawal System
# Input current balance and withdrawal amount
balance = float(input("Enter current balance: ₹"))
withdrawal = float(input("Enter withdrawal amount: ₹"))

# Check if amount is multiple of 100
if withdrawal % 100 != 0:
    print("Withdrawal failed: Amount must be multiple of 100.")
# Check if balance is sufficient
elif withdrawal > balance:
    print("Withdrawal failed: Insufficient balance.")
# Check if minimum balance of 500 remains
elif (balance - withdrawal) < 500:
    print("Withdrawal failed: Minimum balance of ₹500 must remain.")
else:
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: ₹{balance}")


## Day Type Checker (Switch / match-case)
# Take input for day number
day = int(input("Enter day number (1-7): "))

# Check day type
if 1 <= day <= 5:
    print("Weekday")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Invalid Day")


## Menu-Driven Calculator
# Take two numbers input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show menu
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take user choice
choice = int(input("Enter choice (1-4): "))

# Perform operation using match-case
match choice:
    case 1:
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    case 2:
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    case 3:
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    case 4:
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid choice")

##16Insurance Eligibility
# Take inputs
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))
medical_history = input("Enter medical history (clear/issue): ").lower()

# Check eligibility using nested if
if age >= 25:
    if salary >= 40000:
        if medical_history == "clear":
            print("Person is eligible")
        else:
            print("Person is not eligible: Medical history not clear")
    else:
        print("Person is not eligible: Salary below 40,000")
else:
    print("Person is not eligible: Age below 25")


##17Traffic Signal Simulator
# Take color input
color = input("Enter a color: ").lower()  # convert to lowercase for consistency

# Check color and print message
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")


##Triangle Type Checker
# Input sides
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check if sides form a valid triangle (triangle inequality)
if a + b > c and a + c > b and b + c > a:
    # Determine type of triangle
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")


##19 Exam Attempt Rules
# Input exam status and attempt count
status = input("Enter exam status (pass/fail): ").lower()
attempts = int(input("Enter number of attempts: "))

# Check eligibility to re-attempt
if status == "fail" and attempts <= 3:
    print("Student can re-attempt")
else:
    print("No more attempts")


##20Password Strength Checker
# Input password
password = input("Enter your password: ")

# Check conditions
has_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

# Determine strength
if has_length and has_digit and has_upper:
    print("Strong")
else:
    print("Weak")

