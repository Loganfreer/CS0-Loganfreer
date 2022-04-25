"""
CSCI 110
List Lab

By: Logan Freerksen
Date: 04/24/22

Program prompts user to enter 10 integers and stores the entered numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
and print the largest and smallest values in the list.
Program will also print the indices of the largest and smallest numbers in the list.
"""

from audioop import reverse


totalInts = 10


def getIntegers():
    intList = []
    i = 0
    while i < totalInts:
        num = int(input("Enter an integer: "))
        intList.append(num)  # store num into integers list
        i += 1
    return intList


def sortListInAscendingOrder(intList):
    newINTS = intList.copy()
    newINTS.sort()
    return newINTS


def sortListInDescendingOrder(intList):
    desINTS = intList.copy()
    desINTS.sort(reverse = True)#fixed
    return desINTS
    


def printList(intList):
    for val in intList:
        print(val, end=' ')
    print()


def main():
    integers = []  # empty list to store integers
    integers = getIntegers()
    print("Numbers entered are: ")
    print(f"{integers}")
    print()
    # sort numbers
    ascending = sortListInAscendingOrder(integers)
    print("Numbers in ascending order: ")
    print(f"{ascending}")
    # FIXME4 (10 points)
    descending = sortListInDescendingOrder(integers) #fixed
    # Call sortListInDescendingOrder function
    
    print(f"Numbers in descending order: \n{descending}") #fixed
    # Print the sorted list in descending order
    
    print(f"The largest number is: {descending[0]}") #fixed
    # Print the largest number
    
    print(f"The smallest number is: {ascending[0]}") #fixed
    # Print the smallest number
    
    print(f"The index of the smallest number is: {integers.index(ascending[0])} ") #fixed
    # Find and print the index of the smallest number
    
    print(f"The index of the largest number is: {integers.index(descending[0])}") #fixed
    # Print the index of the largest number



# Call main function if this file is run as the main module
print('call main() function to see partial outputs of the program...') #fixed
if __name__ == "__main__":
    main()