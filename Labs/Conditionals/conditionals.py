"""
Lab - Conditional Statements

By: FIXME

CSCI 110
Date: FIXME

Program prompts user to enter a number and determines whether the entered number is even or odd, positive or negative or zero.

Algorithm steps:
1. Prompt user to enter a number
2. Convert the value into integer and store it into a variable
3. Define a function that takes a number as parameter and determines whether the number is
even or odd using the following algorithm:
    3.1 If the number is divisible by 2 with the remainder 0, it is an even number
    3.2 Otherwise, it is an odd number
    3.3 The function returns True for even and False for odd number

4. Define a function that takes a number as parameter and determines whether the number is positive or not using the following algorithm:
	4.1 If the number is greater than zero, return True
	4.2 Otherwise, return False

5. FIXME1 – write algorithm steps to determine if the number is zero or not using a function.
6. Call the functions using the entered number and display the results with proper descriptions.
7. Test and validate the program output is correct with several different numbers
"""

import sys
import os


def isEven(num):
    even = False
    # FIXME2
    # determine whether the num is even or odd
    # return True for even; False otherwise
    return even


def isPositive(num):
    # FIXME3 – use your algorithm in step 4 to determin if num is 0 or not
    return True


def isZero(num):
    # Given a num, return True if num equals to zero, False otherwise
    # FIXME4 - fixed
    if num == 0:
        return True
    else:
        return False

# FXIME5:
# Define a function that takes in a string name argument
# function greets the name by printing, e.g.: Hello, John! Welcome onboard...


def clearScreen():
    """
    function that clears the console/terminal
    """
    if os.name == 'nt': # if os is windows
        os.system('cls') # run cls command
    else:
        os.system('clear')  # run clear command

def main():
    """
    main program
    """
    clearScreen() # clear screen
    print("Program determines whether a given number is even or odd")
    ans = input('Do you want to continue? Enter [y|n]: ')
    if ans != 'y':
        sys.exit()  # exit/end the program

    # FIXME6:
    # Prompt user to enter their name and update the name variable
    name = "Anonymous"

    # loop until user wants to quit
    while True:
        # clear the screen for subsequent use
        clearScreen()
        # FIXME7: call function defined in FIXME5 to greet the user
        print("Enter a whole number, {}:".format(name))
        anum = input()
        if not anum.strip('-').isdecimal():
            print('Not a number, enter to continue...')
            input()
            continue

        anum = int(anum)
        if isZero(anum):
            print(anum, "is zero!")
        else:
            # Call isEven function and store the returned value into even variable
            even = isEven(anum)
            if even:
                print(anum, "is an even number!")
            else:
                print(anum, "is an odd number!")

            # FIXME8
            # call isPositive function passing anum and print the result with proper description

        answer = input(
            "Would you like to check another number? Enter y or yes; anything else to quit: ")
        if answer == 'y':
            # FIXME9 - make the progrom continue to run if user entered yes
            continue
        else:
            print('Thanks for using the program, {}! Good bye...'.format(name))
            break


def test():
    # test function to test other functions
    # FIXME10
    # using assert statment write at least 1 test case for
    # isEven, isPositive, isZero functions
    assert isPositive(99) == True
    print('all test cases passed...')


# FIXME10
# call test function


# call main function
main()