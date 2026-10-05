def Habit_tracker():
    print("--Welcome to Habit Tracker--")
    Habits = {"Gym": 0, "Coding": 0, "Studying": 0}
    while True:
       if Operation == 'exit':
            print("\n--- Final Summary ---")
            print("Yeh raha tera total score:")
            print(Habits)
            print("You have exited the Habit tracker. Keep crushing it! 🚀")
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
                 print("No habit like this exists except for 'Gym', 'Coding', 'Studying'")
                continue

Habit_tracker()
