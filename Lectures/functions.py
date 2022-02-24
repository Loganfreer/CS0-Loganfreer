'''
Name: Logan Freerksen
Date:02/22/22

This program will define a bunch of functions related to mathtematical
operaters and will eventually prompt the user for two numbers and will 
call fumctions using the users entered parameters

Step 1: Define function that takes in two numebrs and returns the sum
Step 2: Define function that takes in two numbers and returns the product
Step 3: Define function that takes in two numbers and returns the quotient
Step 4: Define function that takes in two numbers and returns the difference
Step 5: Define a function that takes in two numbers and returns the 
        remainder of the quotient
Step 6: Define function that takes in two numbers and returns the first number
        to the power of the second
Step 7: Define a function that takes in a number and returns the square root
Step 8: Prompt user to enter two numbers
Step 9: Call all of the functions using the user entered parameters 
        and print out the results
Step 10: Write a test function for each function using at least two cases
Step 11: *Bonus* Define a function that returns the larger of the two numbers 
'''
import math
#Step 1
def addition_function(a, b):
    _sum_ = 0
    _sum_ = a + b
    return _sum_
    
#Step 2
def multiply_function(c, d):
    _product_ = 0
    _product_ = c * d
    return _product_

#Step 3
def divide_function(e, f):
    _quotient_ = 0
    _quotient_ = e / f
    return _quotient_

#Step 4
def subtract_function(g, h):
    _difference_ = 0
    _difference_ = g - h 
    return _difference_

#Step 5
def mod_function(i, j):
    _mod_ = 0 
    _mod_ = i % j
    return _mod_

#Step 6
def power_function(k, l):
    _power_ = 0
    _power_ = k ** l 
    return _power_

#Step 7
def root_function(m):
    _root_ = 0
    _root_ = math.sqrt(m)
    return _root_

#Step 10
def test():
    assert addition_function(1,4) == 5
    assert addition_function(2,9) == 11
    assert multiply_function(3,9) == 27
    assert multiply_function(2,5) == 10
    assert divide_function(72,6) == 12
    assert divide_function(9,3) == 3
    assert subtract_function(9,5) == 4
    assert subtract_function(50,10) == 40
    assert mod_function(5,10) == 5
    assert mod_function(10,3) == 1
    assert power_function(2,3) == 8
    assert power_function(5,2) == 25
    assert root_function(25) == 5
    assert root_function(81) == 9

def main():
    test()
    print('The program will compute mathematical operations on the numbers you provide...')
    #Step 8
    global number1
    global number2
    number1 = float(input('Please enter one number: '))
    number2 = float(input('Please enter another number: '))
    #Step 9
    sum_ = addition_function(number1, number2)

    product_ = multiply_function(number1, number2)

    quotient_ = divide_function(number1, number2)

    difference_ = subtract_function(number1, number2)

    mod_ = mod_function(number1, number2)

    pow_ = power_function(number1, number2)

    root_ = root_function(number1)
    print(f'''The sum is {sum_}, \nThe product is {product_}, \nThe quotient is {quotient_}, \nThe differencce is {difference_}, \nThe remainder of {number1} and {number2} is {mod_},\n{number1} to the power of {number2} is {pow_},\nAnd finally the root of {number1} is {root_}''')

main()

#Step 11
def larger_number(x, y):
    if x>y:
        return True
    else:
        return False

if larger_number(number1, number2):
    print(f'{number1} is larger than {number2}')
else:
    print(f'{number2} is larger than {number1}')





