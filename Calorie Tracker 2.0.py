calorie_intake = 2000
calorie_eaten = 0
calories_total = int(input("Enter how many calories you have taken:"))

if calories_total >= calorie_intake:
    print("You have hit Your calories target!!")
else:
    calories_needed = calorie_intake - calories_total
    print("You have not hit Your calories target!!")
    print(f"You need this much {calories_needed} to complete ur cals!!")

last_meal = int(input(f"Enter any extra calories you have eaten throughout the day:"))
calories_total = calories_total + last_meal

calories_needed = calorie_intake - calories_total
if calories_total >= calorie_intake:
    print(f"You have eaten around {calories_total} calories,You have succesfully completed you daily calories intake.")
else:
    print(f"You are still lacking {calories_needed} , this much calories to complete you total calories")

Total_Protein_consumed = (calories_total * 0.30)/4
Total_Carbs_consumed = (calories_total * 0.50)/4
Total_fats_consumed = (calories_total * 0.20)/9

print(f"You have consumed in total of {round(Total_Protein_consumed,2)}g proteins, {round(Total_Carbs_consumed,2)}g of carbs and {round(Total_fats_consumed,2)}g of fats.")