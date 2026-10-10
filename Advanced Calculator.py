def advance_calculator():
    while True:
        operation = input("Enter any operation you want to do '+', '-', '/', '*', '**', '%', or simply type 'exit' to leave: ")
        
        if operation == 'exit':
            print("You have left the calculator")
            break
        
        # Numbers ko loop ke andar hona chahiye taaki har dafa naye numbers le sakein
        try:
            num_1 = float(input("Enter number 1: "))
            num_2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if operation == '+':
            result = num_1 + num_2
            print(f"Result: {result}")

        elif operation == '-':
            result = num_1 - num_2
            print(f"Result: {result}")
            
        elif operation == '*':
            result = num_1 * num_2
            print(f"Result: {result}")
            
        elif operation == '/':
            if num_2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num_1 / num_2
                print(f"Result: {result}")
                
        elif operation == '**':
            result = num_1 ** num_2
            print(f"Result: {result}")
            
        elif operation == '%':
            if num_2 == 0:
                print("Error: Modulo by zero is not allowed!")
            else:
                result = num_1 % num_2
                print(f"Result: {result}")
        else:
            print("Invalid operation! Please try again.")
        # Main loop ke end mein:
while True:
    restart_or_exit = input("Do you want to continue calculating? Type 'yes' to continue or 'exit' to leave: ").lower().strip()
    
    if restart_or_exit == 'exit':
        print("You have successfully exited the calculator.")
        break  # Is se yeh inner loop khatam hoga
    elif restart_or_exit == 'yes':
        print("Calculate again...\n")
        break  # Is inner loop se baahar nikal kar outer loop wapis chalega
    else:
        print("Invalid input! Please type only 'yes' or 'exit'.")
        # Yeh continue nahi bhi likho ge toh loop wapis input poochega
     

# Function ko call karna mat bhoolna
advance_calculator()
        
  
