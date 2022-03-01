'''
Name: Logan Freerksen
Date: 03/01/22

This program will take in five numbers given by the user and complete several
mathematical computations, and does some comparisons using thte numbers

Step 1: Derfine a function that take in 5 numbers and returns the sum of the
        the numbers
Step 2: Define a functions that takes in 5 numbers and returns the product
        of the 5 numbers
Step 3: Define a function that takes in 5 numbers and returns the average of 
        the numbers, this step will include the function from Step 1
Step 4: Define a conditional function that takes in 5 numbers and returns the
        max
Step 5: Define a conditional function that takes in 5 numbers and returns
        the min
Step 6: Define the main function which prompts users for 5 numbers and passes
        them through the previously defined functions
Step 7: Define a test function with at least 2 test cases per function
Step 8: Call main and test functions
'''
#Step 1
def add_nums(n1, n2, n3, n4, n5):
    _sum_ = n1 + n2 + n3 + n4 + n5
    return _sum_

#Step 2
def multiply_nums(n1, n2, n3, n4, n5):
    _product_ = n1 * n2 * n3 * n4 * n5
    return _product_

#Step 3
def average_nums(N1, N2, N3, N4, N5):
    _average_ = add_nums(N1, N2, N3, N4, N5) / 5
    return _average_

#Step 4
def max_function(N1, N2, N3, N4, N5):
    if N1 > N2 and N1 > N3 and N1 > N4 and N1 > N5:
        print(f'{N1} is the largest number')
    elif N2 > N1 and N2 > N3 and N2 > N4 and N2 > N5:
        print(f'{N2} is the largest number')
    elif N3 > N1 and N3 > N2 and N3 > N4 and N3 > N5:
        print(f'{N3} is the largest number')
    elif N4 > N1 and N4 > N2 and N4 > N3 and N4 > N5:
        print(f'{N4} is the largest number')
    else:
        print(f'{N5} is the largest number')

#Step 5 
def min_function(N1, N2, N3, N4, N5):
    if N1 < N2 and N1 < N3 and N1 < N4 and N1 < N5:
        print(f'{N1} is the smallest number')
    elif N2 < N1 and N2 < N3 and N2 < N4 and N2 < N5:
        print(f'{N2} is the smallest number')
    elif N3 < N1 and N3 < N2 and N3 < N4 and N3 < N5:
        print(f'{N3} is the smallest number')
    elif N4 < N1 and N4 < N2 and N4 < N3 and N4 < N5:
        print(f'{N4} is the smallest number')
    else:
        print(f'{N5} is the smallest number')

#Step 7
def test():
    assert add_nums(1,2,3,4,5) == 15
    assert add_nums(2,3,2,1,3) == 11
    assert multiply_nums(1,2,2,1,2) == 8
    assert multiply_nums(3,2,1,3,1) == 18
    assert average_nums(1,2,3,4,5) == 3
    assert average_nums(2,3,4,5,6) == 4
    
#Step 6
def main():
    test()
    num1 = float(input('Please enter a number: '))
    num2 = float(input('Please enter a second number: '))
    num3 = float(input('Please enter a third number: '))
    num4 = float(input('Please enter a fourth number: '))
    num5 = float(input('Finally, enter a fifth number: '))
    print('\n')
    _sum = (add_nums(num1, num2, num3, num4, num5))
    _product = (multiply_nums(num1, num2, num3, num4, num5))
    _average = (average_nums(num1, num2, num3, num4, num5))
    (max_function(num1, num2, num3, num4, num5))
    (min_function(num1, num2, num3, num4, num5))
    print(f'The sum of the number is {_sum}\nThe product is {_product}\nThe average is {_average}')

main()


