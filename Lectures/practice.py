import math as mt
from statistics import multimode

print(mt.radians(270))
print(mt.sqrt(2))
print(mt.gcd(12400000,8212228899000))
def greeting():
    print("Hello Logan")
    print('Outside function')

greeting()
x=9
print(x**2-5)

def calc_value():
    print(x**2 + 7)



x=5
calc_value()
x=9
calc_value()
x=1999
calc_value()
x=100
calc_value()



'''
Name Logan Freerksen
Date 02/18/22

Define afunction that takes two numbers
and returns the product of two numbers

step 1 define function to take two numbers
step 2 return product of two numbers from function
step 3 call function with some parameters
step 4 print out answer
'''

#Step 1
def multiply_nums(num1, num2):
    #Step 2
    multiply_sum = 0
    multiply_sum = num1*num2
    return multiply_sum

print(multiply_nums(42, 5))

#step 3
def test():
    assert multiply_nums(2, 6) == 12
    assert multiply_nums(5, 10) == 50

def main():
    #step 3
    test()
    number1 = float(input("Please enter a number: "))
    number2 = float(input('Please enter another number: '))
    answer = multiply_nums(number1,number2)
    print(f'{number1} * {number2} = {answer}')

main()
 


