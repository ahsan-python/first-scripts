def calorie_maintainance():
  data = {}
  print("--Welcome to calories counter--")

  while True:
    try:
      # 1. Age Input & Check (1 to 120 years)
      data["Age"] = int(input("Enter your age (1-120): "))
      if not (1 <= data["Age"] <= 120):
        print("Error: Age must be realistic (between 1 and 120). Try again.\n")
        continue

      # 2. Height Input & Check (50 to 250 cm)
      data["Height"] = int(input("Enter your height in cm (50-250): "))
      if not (50 <= data["Height"] <= 250):
        print("Error: Height must be realistic (between 50 and 250 cm). Try again.\n")
        continue

      # 3. Weight Input & Check (20 to 300 kg)
      data["Weight"] = float(input("Enter your weight in kg (20-300): "))
      if not (20 <= data["Weight"] <= 300):
        print("Error: Weight must be realistic (between 20 and 300 kg). Try again.\n")
        continue

      # Calculation (Mifflin-St Jeor Formula)
      bmr = (
          (10 * data["Weight"]) + (6.25 * data["Height"]) - (5 * data["Age"]) + 5
      )
      print(f"\nSuccess! Your Basal Metabolic Rate (BMR) is: {bmr:.2f} kcal/day.")

      print("--Lets calculate your total intake require for you body according to you daily activities and BMR--")

      
    except ValueError:
      print("Error: Please enter valid numbers only. Try again.\n")


# Run the function
calorie_maintainance()

        
            
