# Task: Calculator Program
# Create a Python program that acts as a basic
#  calculator. It should prompt the user to
#  enter two numbers and an operator (+, -, *, /,
#  %), and then display the result of the
#  operation
num1 = float(input("Enter first Number: "))
operator = input("Enter any operator(+ - * / %): ")


match operator:
    case "+":
        num2 = float(input("Enter second Number: "))
        print(round((num1+num2), 2))
    case "-":
        num2 = float(input("Enter second Number: "))
        print(round((num1-num2), 2))
    case "*":
        num2 = float(input("Enter second Number: "))
        print(round((num1*num2), 2))
    case "/":
        num2 = float(input("Enter second Number: "))
        print(round((num1 / num2), 2))
    case "%":
        num2 = float(input("Enter second Number: "))
        print(int(num1 % num2))
    case _:
        print("The operator doesn't matter, what matters is solving problems.")
