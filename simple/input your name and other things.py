# Some code to print the version of your python
import sys
print(f"Python version: {sys.version}") 

# A simple program to input your name and print it
name = input("enter your name ")
print(f"Hi you are {name}, right ?")

#this is who to print whatever you want in python
thing = input("enter what you want to print ")
print(f"{thing}")

# A simple calculator that adds two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

# A simple calculator that subtracts two numbers
num1 = float(input("Enter first number: "))     
num2 = float(input("Enter second number: "))
difference = num1 - num2
print(f"The difference of {num1} and {num2} is {difference}")

# A simple calculator that multiplies two numbers
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
product = num1 * num2
print(f"The product of {num1} and {num2} is {product}")

# A simple calculator that divides two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 != 0:
    quotient = num1 / num2
    print(f"The quotient of {num1} and {num2} is {quotient}")   
else:
    print("Error: Division by zero is not allowed.")

# A simple program to check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

'''this 
is a 
multiline comment'''

# this is a single line coment