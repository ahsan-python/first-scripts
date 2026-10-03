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