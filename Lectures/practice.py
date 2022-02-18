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
step 2 return product of two numbers
step 3 
'''

#Step 1
def multiply_nums(num1, num2):
    #Step 2
    return num1*num2

#step 3 
answer = multiply_nums(42, 5)
