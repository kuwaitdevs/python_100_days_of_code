first_number = input("What's the first number?:\n>")
continue_calculation = 'y'

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2

while continue_calculation == 'y':
    operation = input("Pick an operation: + - / *\n>")
    next_number = input("What's the next number?:\n>")

    operation_result = calculate(float(first_number), float(next_number), operation)

    print(f'{str(first_number)} {operation} {next_number} = {operation_result}')

    continue_calculation = input(f"Type 'y' to continue calculating with {operation_result}, or type 'n' to start a new calculation:\n")

    if continue_calculation == 'y':
        first_number = operation_result


