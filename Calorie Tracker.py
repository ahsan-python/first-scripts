calorie_intake = 2000
calorie_eaten = 0

meal_1 = int(input("Please enter your cals:"))
calories_total = calorie_eaten + meal_1

meal_2 = int(input("Please enter your cals:"))
calories_total = calories_total + meal_2

meal_3 = int(input("Please enter you last cals:"))
calories_total = calories_total + meal_3

if calories_total >= calorie_intake:
    print("You have hit Your calories target!!")
else:
    calories_needed = calorie_intake - calories_total
    print("You have not hit Your calories target!!")
    print(f"You need this much {calories_needed} to complete ur cals!!")

last_meal = int(input("please enter the last remaining cals to complete your day:"))
calories_total = calories_total + last_meal

calories_needed = calorie_intake - calories_total
if calories_total >= calorie_intake:
    print(f"You have eaten around {calories_total} calories,You have succesfully completed you daily calories intake.")
else:
    print(f"You are still lacking {calories_needed} , this much calories to complete you total calories")