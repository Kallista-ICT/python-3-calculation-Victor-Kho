#This is where you input the measurement
distance = float(input("Enter the distance (in meters): "))
time = float(input("Enter the time (in seconds): "))

#This is the formula of velocity
velocity = distance/time

#This is the final calculation
print(f"The velocity is {velocity:.2f}m/s.")
