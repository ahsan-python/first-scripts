def menu_of_tea_shop():
    normal_tea = 200
    special_tea = 350
    sugar_tea = 300
    
    print("Menu: normal_tea, special_tea, sugar_tea")
    order = input("Select, what do you like to order: ").strip().lower()

    if order == "normal_tea":
        print(f"It will be {normal_tea}rs")
    elif order == "special_tea":
        print(f"It will be {special_tea}rs")
    elif order == "sugar_tea":
        print(f"It will be {sugar_tea}rs")
    else:
        print("Sorry, this is not available on the menu")

if __name__ == "__main__":
    menu_of_tea_shop()