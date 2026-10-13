def calorie_maintainance():
    data = {}   
    print("--Welcome to calories counter--")

    while True:
        try:
            data['Age'] = int(input("Enter your age:"))
            data['Height'] = int(input("Enter you height in (cm):"))
            data['Weight'] = float(input("Enter your weight (kg): "))
        except ValueError:
            print("Please! enter numbers only.")
            
            
            if data['Age'] <=0:
                print("Error Age cannot zero or be negative.")
                break

            if data["Weight"] <=0:
                print("Error weight cannot be zero or negative.")
                break

            bmr = (10 * data['weight']) + (6.25 * data['height']) - (5 * data['age']) + 5
            print(f"Your total calorie maintainance {bmr}.")
calorie_maintainance()

        
            