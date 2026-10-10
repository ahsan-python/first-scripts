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
        if restart_or_exit == 'exit':
            print("You have succesfully exited the calculator")
            break
        else:
            print("Invalid statement. you can only choose from exit or yes")
            continue
        if restart_or_exit == 'yes':
            print("Calculate again")
            continue
           
     

# Function ko call karna mat bhoolna
advance_calculator()
        
  
