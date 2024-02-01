def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "substract":
        return x - y
    
print(calculate_numbers(2, 3))
print(calculate_numbers(2, 3, "substract"))

