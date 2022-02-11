#! /usr/bin/env python3

###
# Circle - Basic Math - Lab
# Updated By: Logan Freerksen #fixed#
# Date: 02/10/22 #fixed#
# CSCI 110
#
# This program prompts user to enter radius of a circle and calculates and displays area
# and circumference of the circle.
#
# Algorithm steps:
#	1. Prompt user to enter radius
#	2. Store radius into a variable
#	2. Calculate area using the formula: pi * radius * radius
#	3. Calculate circumference using the formula: 2 * pi * radius
#	4. Display the calculated values of area and circumference with proper description
###
# import math library that has PI and other functions defined
import math

print("This program finds and displays area and circumference of a circle given some radius.")
input('Enter to continue...')
# Step 1 and 2
radius = input("Enter radius of a circle: ")
radius = float(radius)  # convert string to float value

# Step 3
area = math.pi * radius**2  # * is product and ** is power operator in Python

# Step 4
#fixed#
# calculate and store the circumference into a variable

circumference = 2 * math.pi * radius
# Display the calculated values with proper descriptions
print("Radius of the circle =",  radius)

# FIXME4: display area - already fixed for you! #fixed#
print('Area of the circle =', area)

# #fixed#: display circumference
print('Circmference of the cirlce =', circumference)

# Verify/Test your program if the calculated results are correct
# Run and test your program with different values for radius
print('Good bye...')