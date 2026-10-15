def main():
  while True:   
        print("\n--- WELCOME TO CALORY APP ---")
        print("1. Calorie & Macro Tracker")
        print("2. Step Counter")
        print("3. Water Intake Tracker")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            calorie_tracker()
        elif choice == '2':
            total_step_taken()
        elif choice == '3':
            total_water_intake()
        elif choice == '4':
            print("Exiting Calory App. Keep grinding! ⚔️")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")



def calorie_tracker():
    calorie_intake = 2000
    while True:
        calories_total = int(input("Enter how many calories you have taken:"))

        if calories_total >= calorie_intake:
            print("You have hit Your calories target!!")
        else:
            calories_needed = calorie_intake - calories_total
            print("You have not hit Your calories target!!")
            print(f"You need this much {calories_needed} to complete ur cals!!")
            
            last_meal = int(input(f"Enter any extra calories you have eaten throughout the day:"))
            calories_total = calories_total + last_meal
            continue
            
        calories_needed = calorie_intake - calories_total
        if calories_total >= calorie_intake:
            print(f"You have eaten around {calories_total} calories,You have succesfully completed you daily calories intake.")
        else:
            print(f"You are still lacking {calories_needed} , this much calories to complete you total calories")
            continue
            
        ingrediants = input("\nDo you want to know how much protein, carbs and fats you have consumed? Press 'Enter' if yes or type 'exit' if no: ")

        if ingrediants.strip().lower() == 'exit':
                print("You have exited the macro calculator. Keep grinding! ⚔️")
                break
        protein_cals = calories_total * 0.30  # 30% of total
        carbs_cals = calories_total * 0.40    # 40% of total
        fats_cals = calories_total * 0.30     # 30% of total (30 + 40 + 30 = 100%)

        # Grams mein convert karein
        total_protein_g = protein_cals / 4
        total_carbs_g = carbs_cals / 4
        total_fats_g = fats_cals / 9
       # Line-by-line clean output show karein
        print(f"Protein : {total_protein_g:.1f}g")
        print(f"Carbs   : {total_carbs_g:.1f}g")
        print(f"Fats    : {total_fats_g:.1f}g")
        break


# --- FEATURE 2: STEP COUNTER (Tumhara Exact Code) ---
def total_step_taken(step=3000):
    steps_taken = int(input("Please write the number of steps taken:"))
    while steps_taken < step:
     remaining_steps = step - steps_taken
     more_steps = int(input(f"You are left with {remaining_steps}.Add more:"))
     steps_taken += more_steps

    print("You have completed your steps.")

    calories_burned = 0.0
    for _ in range(0, steps_taken, 10):
        calories_burned += 0.4
    calories_burned = round(calories_burned, 2)
    print(f"You have burned {calories_burned:.2f} calories!!")  
    
    total_distance_covered = steps_taken * .5
    print(f"You have covered {total_distance_covered}m")


# --- FEATURE 3: WATER INTAKE (Tumhara Exact Code) ---
def total_water_intake(water_goal=3000):
    water_added = int(input("Please enter how many ml of water you have consumed: "))
    total_consumed = water_added

    # Jab tak goal poora nahi hota, loop chalega
    while total_consumed < water_goal:
        remaining_water = water_goal - total_consumed
        print(f"You have left with {remaining_water}ml to reach your goal.")
        
        water_added = int(input("Add more water: "))
        total_consumed += water_added

    # Agar add karne ke baad goal hit ya exceed ho gaya, toh loop yahan rok do
    if total_consumed >= water_goal:
        print(f"Goal already reached! Total consumed: {total_consumed}ml. Congratulations! 🎉")
        return total_consumed
            

    print(f"You have completed your water intake! Total consumed today: {total_consumed}ml. Congratulations! 🎉")
main()