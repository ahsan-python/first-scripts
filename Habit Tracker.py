def Habit_tracker():
    print("--Welcome to Habit Tracker--")
    Habits = {"Gym": 0, "Coding": 0, "Studying": 0}
    while True:
        Operation = input("Enter a Habit, You have performed from 'GYM, Coding, Studying' or leave by pressing 'exit':")
        if Operation == 'exit':
            print("You have exited the Habit tracker!")
            break

        else:
               if Operation == "Gym":
                 Habits["Gym"] += 1
                 print(f"You have performed your workout {Habits['Gym']} time(s).")
               elif Operation == "Studying":
                 Habits["Studying"] += 1
                 print(f"You have studied {Habits['Studying']} time(s).")
               elif Operation == "Coding":
                 Habits["Coding"] += 1
                 print(f"You have written code {Habits['Coding']} time(s).")
               else: 
                 print("No related habit performed")

Habit_tracker()
