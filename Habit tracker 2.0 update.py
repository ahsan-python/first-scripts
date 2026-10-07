def reset_habits(habit_dict):
    """Reset all habits back to zero"""
    for habit in habit_dict:
        habit_dict[habit] = 0
    # Print aur return loop ke baahar honge taaki saari habits reset hone ke baad message aaye
    print("[+] All habits have been reset back to zero. Fresh start!")
    return habit_dict

def Habit_tracker():
    print("--Welcome to Habit Tracker--")
    Habits = {"Gym": 0, "Coding": 0, "Studying": 0}
def Show_progress(Habit_dict):
    """Display all current progress of All habits performed"""
    print("--current Habit progress--")
    for habit in habit_dict. item():
        print(f" {habit}: {count} time(s)")
        print("---------------------------------\n")
    
    while True:
        Operation = input("Enter a Habit ('Gym, Coding, Studying'), type 'reset' to clear all, or 'exit' to quit: ")
        
        if Operation == 'exit':
            print("You have exited the Habit tracker!")
            break
            
        elif Operation == 'reset':
            # Yahan humne reset function ko call kar diya
            Habits = reset_habits(Habits)
            print(f"Current Status: {Habits}")
            
        elif Operation == "Gym":
            Habits["Gym"] += 1
            print(f"You have performed your workout {Habits['Gym']} time(s).")
            
        elif Operation == "Studying":
            Habits["Studying"] += 1
            print(f"You have studied {Habits['Studying']} time(s).")
            
        elif Operation == "Coding":
            Habits["Coding"] += 1
            print(f"You have written code {Habits['Coding']} time(s).")
            
        else:
            print("Invalid input or no related habit performed.")

# Tracker run karne ke liye
Habit_tracker()
