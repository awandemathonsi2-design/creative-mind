#Enter your mass in kilograms
mass = int(input("m: "))

#This is my way of forming the equation E=m**2
speed_of_light = pow(300000000, 2)
energy = mass * speed_of_light

print("E:", energy)