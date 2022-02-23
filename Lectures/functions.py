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


def test_add():
    assert addition_function(1,4) == 5
    assert addition_function(2,9) == 11

def test_mult():
    assert multiply_function(3,9) == 27
    assert multiply_function(2,5) == 10

def test_div():
    assert divide_function(72,6) == 12
    assert divide_function(9,3) == 3

def test_sub():
    assert subtract_function(9,5) == 4
    assert subtract_function(50,10) == 40

def test_mod():
    assert mod_function(5,10) == 5
    assert mod_function(10,3) == 1

def test_pow():
    assert power_function(2,3) == 3
    assert power_function(5,2) == 25

def test_root():
    assert root_function(25) == 5
    assert root_function(81) == 9


def addition_function(a, b):
    test_add()
    _sum_ = 0
    _sum_ = a + b
    return _sum_
    
#Step 2
def multiply_function(c, d):
    test_mult()
    _product_ = 0
    _product_ = c * d
    return _product_

#Step 3
def divide_function(e, f):
    test_div()
    _quotient_ = 0
    _quotient_ = e / f
    return _quotient_

#Step 4
def subtract_function(g, h):
    test_sub()
    _difference_ = 0
    _difference_ = g - h 
    return _difference_

#Step 5
def mod_function(i, j):
    test_mod()
    _mod_ = 0 
    _mod_ = i % j
    return _mod_

#Step 6
def power_function(k, l):
    test_pow()
    _power_ = 0
    _power_ = k ** l 
    return _power_

#Step 7
def root_function(m):
    test_root()
    _root_ = 0
    _root_ = math.sqrt(m)
    return _root_

#Step 8
number1 = float(input('Please enter one number: '))
number2 = float(input('Please enter another number: '))

print('The program will now compute some operations on the numbers you have provided...')

#Step 9
print(addition_function(number1, number2))

print(multiply_function(number1, number2))

print(divide_function(number1, number2))

print(subtract_function(number1, number2))

print(mod_function(number1, number2))

print(power_function(number1, number2))

print(root_function(number1))

#Step 10
def test_add():
    assert addition_function(1,4) == 5
    assert addition_function(2,9) == 11

def test_mult():
    assert multiply_function(3,9) == 27
    assert multiply_function(2,5) == 10

def test_div():
    assert divide_function(72,6) == 12
    assert divide_function(9,3) == 3

def test_sub():
    assert subtract_function(9,5) == 4
    assert subtract_function(50,10) == 40

def test_mod():
    assert mod_function(5,10) == 5
    assert mod_function(10,3) == 1

def test_pow():
    assert power_function(2,3) == 3
    assert power_function(5,2) == 25

def test_root():
    assert root_function(25) == 5
    assert root_function(81) == 9

#Step 11
def larger_function(n, o):
    if n > o:
        return True
    else:
        return False

if larger_function(number1, number2):
    print(number1, 'Is larger than', number2)
else:
    print(number2, 'Is larger than', number1)
