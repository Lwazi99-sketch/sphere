# Write a program that asks the user to enter the radius of a sphere and calculates and prints the volume.
#Lwazi Somtsewu
# 8 August 2024
import math 

r = eval(input("Enter the radius of the sphere:\n"))

if r >= 0 :
    volume = (4/3)*(math.pi)*(r**3)
    print(f"The volume is {volume:.2f}.")
    
else:
    print("The radius must not be negative.")