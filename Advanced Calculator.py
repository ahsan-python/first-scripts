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
