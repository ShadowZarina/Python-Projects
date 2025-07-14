# Simple Calculator

number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
operation = int(input("Please enter the operation: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

def solve_operation(number1, number2, operation):
    match operation:
        case 1:
            sum = number1 + number2
            print(f"{number1} + {number2} = {sum}")
        case 2:
            difference = number1 - number2
            print(f"{number1} - {number2} = {difference}")
        case 3:
            product = number1 * number2
            print(f"{number1} * {number2} = {product}")
        case 4:
            if number2 == 0:
                print("Error: You cannot divide by zero!")
            else:
                quotient = number1 / number2
                print(f"{number1} / {number2} = {quotient}")
        case _:
            print("Please select from numbers 1 to 4!")

solve_operation(number1, number2, operation)
