#Build a basic calculator
num1 = float(input("Enter a number: "))
op = input("Enter your specified operator: ")
num2 = float(input("Enter another number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 // num2)
elif op == '%':
    print(num1 % num2)
else:
    print("Usage specifier, format num1, num2")
