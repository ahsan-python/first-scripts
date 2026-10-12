import numpy as np

def calculate_magnitude():
    # User se coordinates lena
    x = float(input("Enter the x coordinate: "))
    y = float(input("Enter the y coordinate: "))
    
    # NumPy Array create karna
    v = np.array([x, y])
    
    # NumPy ka High-Performance Norm (Magnitude) function
    magnitude = np.linalg.norm(v)
    return magnitude

result = calculate_magnitude()
print(f"The magnitude of the resultant is {result:.2f}.")
 
