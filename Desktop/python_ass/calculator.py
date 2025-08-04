# Basic calculator program

# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

#Ask the user for the operation
op = input("Enter an operation (+, -, *, /): ")

#Perform the operation
if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    if num2 != 0:
        result = num1 /num2
    else:
        print("Error: Divison by zero!")
        exit()
else:
    print("invalid operation!")
    exit()
# Print the result in the specified format
print(f"{num1} {op} {num2} = {result}")