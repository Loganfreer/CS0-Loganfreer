'''
Name: Logan Freerksen
Date: 02/15/22

This program will prompt users to enter in three sides to a triangle,
and will use those sides to calculate area and perimteter. The area and 
perimeter will then be printed out for the user

Step 1: prompt user for their name
Step 2: Prompt for side1, side2, and side3 of triangle and covert to floats
Step 3: Create function to determine if given side values are a triangle
Step 4: Calculate area using side1, side2, and side3
Step 5: Calculate perimeter using side1, side2, and side3
Step 6: Print out area and perimeter to user

'''
import math
#Step 1
Name = input("Hi there, what's your name? ")
print('Hey there',Name)
print("Let's calculate the area and perimeter of a triangle for you!")

def valid_triangle_function(s1,s2,s3):
    if s1+s2>=s3 and s2+s3>=s1 and s1+s3>=s2:
        return True
    else:
        return False
    


#Step 2
side1 = float(input('What is the length of side 1: '))
side2 = float(input('What is the length of side 2: '))
side3 = float(input('Finally, what is the length of side 3: '))

if valid_triangle_function(side1, side2, side3):
    print('Alrighty! we are computing that right noow!')
else:
    print("Given inputs do not form a triangle, sorry :'(")


#Step 3
s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))


#Step 4
perim = side1+side2+side3
#Step 5
print('The area of the triangle is,',
    area,' and the perimeter is,',perim)
print('Goodbye!')



