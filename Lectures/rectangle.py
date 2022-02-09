'''
Name: Logan Freerksen
Date: 02/09/22

This program will prompt for
two sides of a rectangle and will calculate 
the are and perimeter

Step 1: Prompt for side1 and side2 of a rectangle
Step 2: Covert side1 and side2 to float
Step 3: Calculate area using side1 and side2
Step 4: Calculate perimeter using side1 and side2
Step 5: Print out area and perimeter

'''
#Step 1
side1 = input("Please enter one side of the rectangle")
side2 = input("Please enter the other side of the rectangle")

#Step 2
side1 = float(side1)
side2 = float(side2)

#Step 3
area = side1 * side2

#Step 4
perimeter = (2 * side1) + (2 * side2)

#Step 5
print("The area of a rectangle with sides",
    side1, side2,
    "is", area)

print("The perimeter of a rectangle with sides",
    side1, side2, 
    "is", perimeter)
    