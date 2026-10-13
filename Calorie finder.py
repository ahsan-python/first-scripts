def calorie_maintainance():
    data = {}   
    print("--Welcome to calories counter--")

    while True:
        try:
            data['Age'] = int(input("Enter your age:"))
            data['Height'] = int(input("Enter you height in (cm):"))
            data['Weight'] = float(input("Enter your weight (kg): "))
           
            if data['Age'] <=0:
                print("Error Age cannot zero or be negative.")
                break

            if data["Weight"] <=0:
                print("Error weight cannot be zero or negative.")
                break

            bmr = (10 * data['Weight']) + (6.25 * data['Height']) - (5 * data['Age']) + 5
            print(f"Your total calorie maintainance {bmr}.")
            break
        except ValueError:
            print("Please! write in numbers.")
            break
            
calorie_maintainance()

        
            
