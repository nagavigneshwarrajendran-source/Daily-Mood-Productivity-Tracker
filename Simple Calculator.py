# Simple Calculator
print("Welcome to the Simple Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choose operation
print("\nChoose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operation = input("\nEnter your choice (1/2/3/4): ")

# Perform calculation
if operation == "1":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
elif operation == "2":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif operation == "3":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
    else:
        print("\nError: Cannot divide by zero!")
else:
    print("\nInvalid choice!")
