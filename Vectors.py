def calculate_magnitude():
  x = float(input("Enter the x cordinate:"))
  y = float(input("Enter the y cordinate:"))
  magnitde = ((x**2)+(y**2))** 0.5
  return magnitde
result = calculate_magnitude()

print(f"The magnitude of the resultant is {result:.2f}.")

 