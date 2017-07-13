def calculate(operation, x, y):
    result = None
    if operation == "+":
        result = x + y
    elif operation == "-":
        result = x - y
    elif operation == ":":
        result = x / y
    elif operation == "*":
        result = x * y
    elif operation == "e":
        result = x ** y
    elif operation == "%":
        result = x % y
    else:
        print("Unsupported operation")
    if result is not None:
        print("Result", result)

x = float(input("first number: "))
y = float(input("second number: "))
operation = input("operation: ")
calculate(operation, x, y)