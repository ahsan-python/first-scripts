def collatz_sequence():
    try:
        n = int(input("Enter a positive number: "))
        steps = 0
        
        # Jab tak n 1 nahi ho jata, loop chalega
        while n > 1:
            if n % 2 == 0:
                n = n // 2  # integer division
            else:
                n = (n * 3) + 1
            
            steps += 1
            print(f"Step {steps}: {n}")
            
        print(f"\nFinished! Total steps to reach 1: {steps}")
        
    except ValueError:
        print("Please enter a valid integer!")

collatz_sequence()