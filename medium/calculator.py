def THE_calculator2():
    import math as ma
    import numpy as np

    print("Hi! This is THE calculator. You can calculate numbers with the following options:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. HCF")
    print("8. LCM")
    print("9. array stuff")
    print("\nType 'exit' at any time to quit the calculator.") # Added exit instruction

    while True: # Start of the infinite loop
        user_input = input("Enter your option (number or 'exit'): ").lower() # Convert to lowercase for easier checking

        if user_input == 'exit':
            print("Exiting the calculator. Goodbye!")
            break # Break the loop if the user types 'exit'

        try:
            option = int(user_input)
        except ValueError: # Catch ValueError specifically for non-integer inputs
            print("Please enter a valid number for the option, or 'exit'.")
            continue # Skip to the next iteration of the loop

        # Your existing calculation logic goes here
        if option == 1:
            try:
                add = float(input("Input the first number you want to add: "))
                add2 = float(input("Input the second number you want to add: "))
                aans = (np.add(add, add2))
                print(f"The sum is = {aans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 2:
            try:
                sub = float(input("Input the number you want to subtract from: "))
                sub2 = float(input("Input the number you want to subtract: "))
                sans = (np.subtract(sub, sub2))
                print(f"The answer is = {sans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 3:
            try:
                mul = float(input("Enter the first number you want to multiply: "))
                mul2 = float(input("Enter the second number you want to multiply: "))
                mans = (np.multiply(mul, mul2))
                print(f"The answer is = {mans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 4:
            try:
                div = float(input("Enter the dividend: "))
                div2 = float(input("Enter the divisor: "))
                if div2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    dans = (np.divide(div, div2))
                    print(f"The answer is = {dans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 5:
            try:
                enum = float(input("Enter the base number: "))
                power = float(input("Enter the exponent (power): "))
                eans = (np.power(enum, power))
                print(f"The answer is = {eans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 6:
            try:
                qnum = float(input("Enter the number you want to square root: "))
                if qnum < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                else:
                    qans = (np.sqrt(qnum))
                    print(f"The answer is = {qans}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        elif option == 7:
            try:
                hnum = int(input("Enter the 1st integer for HCF: "))
                hnum2 = int(input("Enter the 2nd integer for HCF: "))
                hans = (ma.gcd(hnum, hnum2))
                print(f"The HCF = {hans}")
            except ValueError:
                print("Invalid input. Please enter integers only for HCF.")
        elif option == 8:
            try:
                lnum = int(input("Enter the first integer for LCM: "))
                lnum2 = int(input("Enter the second integer for LCM: "))
                lwans = (ma.lcm(lnum, lnum2))
                print(f"The answer = {lwans}")
            except ValueError:
                print("Invalid input. Please enter integers only for LCM.")
        elif option == 9 :
            print("1.add array")
            print("2. subtract array")
            print("3. multiply array")
            print("2. divide array")
            print("what do you want to do")
            arrayop = int(input("enter the option"))
            if arrayop == 1:
                try:
                    arr1 = input("Enter the first array elements separated by spaces: ")
                    arr2 = input("Enter the second array elements separated by spaces: ")
                    arr1 = np.array([float(x) for x in arr1.split()])
                    arr2 = np.array([float(x) for x in arr2.split()])
                    if arr1.shape != arr2.shape:
                        print("Error: Arrays must have the same shape for addition.")
                    else:
                        result = np.add(arr1, arr2)
                        print(f"The result of array addition is: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers only for arrays.")
            elif arrayop == 2:
                try:
                    arr1 = input("Enter the first array elements separated by spaces: ")
                    arr2 = input("Enter the second array elements separated by spaces: ")
                    arr1 = np.array([float(x) for x in arr1.split()])
                    arr2 = np.array([float(x) for x in arr2.split()])
                    if arr1.shape != arr2.shape:
                        print("Error: Arrays must have the same shape for subtraction.")
                    else:
                        result = np.subtract(arr1, arr2)
                        print(f"The result of array subtraction is: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers only for arrays.")
            elif arrayop == 3:
                try:
                    arr1 = input("Enter the first array elements separated by spaces: ")
                    arr2 = input("Enter the second array elements separated by spaces: ")
                    arr1 = np.array([float(x) for x in arr1.split()])
                    arr2 = np.array([float(x) for x in arr2.split()])
                    if arr1.shape != arr2.shape:
                        print("Error: Arrays must have the same shape for multiplication.")
                    else:
                        result = np.multiply(arr1, arr2)
                        print(f"The result of array multiplication is: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers only for arrays.")
            elif arrayop == 4:
                try:
                    arr1 = input("Enter the first array elements separated by spaces: ")
                    arr2 = input("Enter the second array elements separated by spaces: ")
                    arr1 = np.array([float(x) for x in arr1.split()])
                    arr2 = np.array([float(x) for x in arr2.split()])
                    if arr1.shape != arr2.shape:
                        print("Error: Arrays must have the same shape for division.")
                    elif np.any(arr2 == 0):
                        print("Error: Cannot divide by zero in arrays.")
                    else:
                        result = np.divide(arr1, arr2)
                        print(f"The result of array division is: {result}")
                except ValueError:
                    print("Invalid input. Please enter numbers only for arrays.")
            else:
                print("Invalid array operation option. Please choose between 1 and 4.") 
        else:
            print("Invalid option. Please choose a number between 1 and 9.")                           
        print("-" * 30) # Separator for readability
THE_calculator2()