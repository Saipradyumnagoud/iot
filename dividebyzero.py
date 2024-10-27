numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
try:
    result = numerator / denominator
    
    print("The result of division is: ",result)
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


