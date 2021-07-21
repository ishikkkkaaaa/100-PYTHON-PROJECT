

def add(n1, n2):
    """Add a number to another number"""
    return n1 + n2


def multiply(n1, n2):
    """Multiply a number by another number"""
    return n1 * n2


def divide(n1, n2):
    """Divide a number by another number"""
    return n1 / n2


def subtract(n1, n2):
    """Subtract a number from another number"""
    return n1 - n2


"""create a dictionary of above function with keys as symbols we used"""
operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

num1 = int(input("Enter first number: "))

for i in operations:
    print(i)
should_continue = True
while should_continue:
    symbol = input("Enter symbol: ")
    num2 = int(input("Enter next number: "))
    #answer = operations[symbol](num1, num2)
    first = operations[symbol]
    answer = first(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")
    if input("Continue? (y/n): ") == "y":
        num1 = answer
        should_continue = True
    else:
        print("thank you lol")
        should_continue = False
"""   symbol = input("Enter another symbol: ")
    num3 = int(input("Enter third number: "))
    second = operations[symbol](first(num1, num2), num3)
    
    print(f"{answer} {symbol} {num3} = {second}") """
