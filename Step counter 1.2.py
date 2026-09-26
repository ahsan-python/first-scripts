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
total_step_taken()
total_water_intake()
