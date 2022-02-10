'''
Name: Logan Freerksen 
Date: 02/09/22

This program will calculate the BMI of a person
BMI = kg/m^2

Step 1: Prompt user to enter weight and height
Step 1a: Convert values to floats
Step 2: Calculate BMI using inputed values
Step 3: Print out BMI

'''
#Step 1
weight = float(input("Please enter your weight in pounds: "))
height = float(input("Please enter your height in inches: "))

#Step 2
weight1 = weight/2.205
height1 = height/39.37
bmi = weight1/height1**2

#Step 3
print("Your BMI with weight", 
    weight, "and height", 
    height, "is", bmi)

