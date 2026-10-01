def menu_of_tea_shop():
    cart = {
        "normal_tea": 0,
        'special_tea': 0,
        'sugar_tea': 0
    }
    prices = {
        'normal_tea': 200,
        'special_tea': 350,
        'sugar_tea': 300
    }
    
    while True:
        print("\n--- MENU ---")
        for item in prices:
            print(f"- {item} ({prices[item]}rs)")
            
        choice = input("\nEnter item name to order or type 'exit' to finish: ").strip().lower()
        
        if choice == 'exit':
            print("\nExiting ordering mode...")
            break
            
        # Dynamic check instead of long if-elif chains
        if choice in cart:
            try:
                qty = int(input(f"How many cups of {choice} do you want? "))
                cart[choice] += qty
                print(f"-> Added {qty} {choice}(s) to your cart.")
            except ValueError:
                print("You need to put a number in quantity!")
        else:
            print("Sorry, yeh item menu mein nahi hai!")

    # --- LOOP 2: The Receipt & Total Loop (Ab loop ke BAHAR hai sahi jagah par) ---
    print("\n" + "="*30)
    print("         YOUR FINAL RECEIPT")
    print("="*30)
    
    grand_total = 0
    item_bought = False
    
    for item, qty in cart.items():
        if qty > 0:
            item_bought = True
            cost = qty * prices[item]
            grand_total += cost
            print(f"{item} x {qty} = {cost}rs")
            
    if item_bought:
        print("-"*30)
        print(f"Grand Total: {grand_total}rs")
        print("="*30)
        print("Thank you for visiting! Come again!")
    else:
        print("You haven't ordered anything!")

if __name__ == "__main__": 
    menu_of_tea_shop()