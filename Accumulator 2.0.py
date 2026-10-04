def Accumulator_to_add_sub_numbers():
    while True:
        operation1 = input("Choose an operation ('+', '-', '*', '/') or press 'exit': ").strip()
        
        if operation1.lower() == 'exit':
            print("You have exited the Accumulator!")
            break
            
        if operation1 not in ['+', '-', '*', '/']:
            print("Invalid operation, please try again.")
            continue
            
        try: 
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue
            
        # Step 1: Calculate first operation
        if operation1 == '+':
            result = num1 + num2
        elif operation1 == '-':
            result = num1 - num2
        elif operation1 == '*':
            result = num1 * num2
        elif operation1 == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                continue
            result = num1 / num2
            
        print(f"-> Intermediate Result: {num1} {operation1} {num2} = {result}")

        # Step 2: Ask for 3rd number chaining
        choice = input("Do you want to apply another operation with a 3rd number? (Type 'yes' or 'exit'): ").strip().lower()
        
        if choice == 'exit':
            print(f"Final Result saved: {result}\nYou have left the Accumulator.")
            break
        elif choice == 'yes':
            operation2 = input("Choose second operation ('+', '-', '*', '/'): ").strip()
            
            if operation2 not in ['+', '-', '*', '/']:
                print("Invalid second operation! Skipping 3rd number calculation.")
                continue
                
            try:
                num3 = float(input("Enter number 3: "))
            except ValueError:
                print("Invalid number for number 3. Please try again.")
                continue
                
            # Step 3: Calculate second operation on the previous result
            if operation2 == '+':
                final_result = result + num3
            elif operation2 == '-':
                final_result = result - num3
            elif operation2 == '*':
                final_result = result * num3
            elif operation2 == '/':
                if num3 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                final_result = result / num3
                
            print(f"-> Final Chained Result: ({result}) {operation2} {num3} = {final_result}")
        else:
            print("Invalid choice, returning to main menu.")
            trying_again = input("Do you want to continue type 'Yes' or if no then write 'No':")
            if trying_again == 'No':
               break
            else:
                continue

# Run the function
Accumulator_to_add_sub_numbers()