def advance_calculator():
    
    while True:
        print("\n=== Welcome to Calculator ===")
        operation = input("Enter operation (+, -, *, /, **, %) or 'exit' to leave: ").strip()
        
        # 1. Direct Exit Check
        if operation == 'exit':
            print("You have left the calculator.")
            break
        
        # 2. Validation Check (Numbers lene se PEHLE check karega)
        valid_operations = ['+', '-', '*', '/', '**', '%']
        if operation not in valid_operations:
            print("Invalid operation! Please enter a valid symbol.")
            continue  # Direct restarts loop, skips number inputs completely!
        
        # 3. Numbers Input (Sirf valid operation hone par chalega)
        try:
            num_1 = float(input("Enter number 1: "))
            num_2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
# 4. Calculation Execution
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
restart_or_exit = input("\nDo you want to continue calculating? (yes/exit): ").lower().strip()

        if restart_or_exit == 'exit':
            print("You have successfully exited the calculator.")
            break
        elif restart_or_exit == 'yes':
            print("Calculating again...")
            continue
        else:
            print("Invalid choice! Restarting calculator...")
            continue

