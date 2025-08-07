# Some code to print the version of your python
import sys
print(f"Python version: {sys.version}") 

# A simple program to input your name and print it
name = input("enter your name ")
print(f"Hi, you are {name}, right?")

# this is how to print whatever you want in python
thing = input("enter what you want to print ")
print(f"{thing}")

# A simple calculator that performs all basic operations on two numbers
print("\n--- Calculator ---")
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Addition
    # Note: Renamed 'sum' to 'sum_result' to avoid conflict with the built-in sum() function.
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")

    # Subtraction
    difference = num1 - num2
    print(f"The difference of {num1} and {num2} is {difference}")

    # Multiplication
    product = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")

    # Division
    if num2 != 0:
        quotient = num1 / num2
        print(f"The quotient of {num1} and {num2} is {quotient}")
    else:
        print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter only numbers for the calculator.")