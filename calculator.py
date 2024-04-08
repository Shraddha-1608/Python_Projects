logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)


# Calculator
# Add
def add(n1, n2):
    return n1 + n2

# Subtract


def sub(n1, n2):
    return n1 - n2

# Multiplication


def mul(n1, n2):
    return n1 * n2

# Division


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("What is the first number?"))
    for symbol in operations:
        print(symbol)
        # operation_symbol=input("Pick up any symbol from the above lines")
    continue_code = False
    while not continue_code:
        operation_symbol = input("Pick up any symbol from the above lines")
        num2 = float(input("What is the second number?"))

        # for symbol in operations:
        # print(symbol)
        # operation_symbol=input("Pick up any symbol from the above lines")

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2}={answer}")
        should_continue = input(
            f"Type 'y' to continue calculating with {answer} ,or type 'n'to exit:")
        if should_continue == 'y':
            num1 = answer
            print(num1)
        else:
            continue_code = True
            calculator()


calculator()
