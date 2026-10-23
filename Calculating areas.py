def Areas():
  while True:
    # Keep input as string first so 'exit' doesn't crash the program
    choice = input(
        "If you want to find area of rectangle type '1', square type '2',"
        " triangle type '3', or type 'exit' to leave: "
    )
    if choice.lower() == "exit":
      print("Exiting calculator. See you!")
      break

    if choice == "1":
      length = float(input("Type the Length of the Rectangle: "))
      breadth = float(input("Type the Breadth of the Rectangle: "))
      print(f"Total Area of the rectangle is = {length * breadth}\n")
    elif choice == "2":
      length = float(input("Type the Side Length of the Square: "))
      print(f"The total area of the Square is = {length * length}\n")

    elif choice == "3":
      base = float(input("Enter the Base of the Triangle: "))
      height = float(input("Enter the Height of the Triangle: "))
      result = 0.5 * base * height  # Fixed the missing '*' operator
      print(f"The total Area of the Triangle = {result}\n")
    else:
      print("Invalid choice! Please type 1, 2, 3, or 'exit'.\n")
      
