"""
Lab - Playing with Loops
Updated By: Logan Freerksen #fixed#
CSCI 110
Date: 04/01/22 #fixed#
Program prints geometric shapes of given height with * using loops
"""
import os
import sys


def printTriangle(height):
    """
    Function takes height as an argument to print the triangle
    of that height with *
    """
    i = 1
    while i <= height:
        print('*  '*i)
        i += 1
    print()  # print an empty line


def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    tri_height = range(height+1)
    for i in tri_height:
        print('* '*tri_height[-i])
    print()
    # FIXME3 ... fixed
    


# FIXME4
# Design and implement a function that takes a number as height and
# prints square of the given height with *.
# Square of height 5, e.g., would look like the following.
"""
*  *  *  *  *  
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
*  *  *  *  *   
"""
#fixed
def printsquare(height):
    i = 1
    while i <= height:
        print('* '*height)
        i += 1
def clearScreen():
    """
    function to clear screen based on the operating system
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    # FIXME7 add a loop to make the program to continue to run until the user wants to quit
    #fixed
    KeepRunning = True
    while(KeepRunning):
        # FIXME8 call clearScreen function to clear the screen for each round of the loop
        #fixed
        clearScreen()
        print('Program prints geometric shapes of given height with *')
        height = int(input('Please enter the height of the shape: '))
        # call printTriangle function passing user entered height
        printTriangle(height)

        # FIXME5 fixed
        # Call printFlippedTriangle passing proper argument
        printFlippedTriangle(height)
        # Manually test the function

    # FIXME6 fixed
        printsquare(height)
    # Manually test the function

    # FIXME9 fixed
    # prompt user to enter y/Y to continue anything else to quit
        answer = input('Would You like to run the program again [Y/N]? ')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            KeepRunning = True
        else:
            KeepRunning = False
    # FIXME10 fixed
    # Use conditional statements to break the loop or continue in the loop


if __name__ == "__main__":
    main()