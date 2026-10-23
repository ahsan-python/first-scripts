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
