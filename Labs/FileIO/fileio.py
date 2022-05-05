"""
File I/O Lab
By: Logan Freerksen #fixed

CSCI 110
Date: 5/5/22 #fixed

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending orders
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME1 which is worth 20 points
"""

totalInts = 10


def readData():
    intList = []
    # FIXME1 (20 points): #fixed
    _numbers_file_ = input('Please enter the file name to the file that contains 10 integers: ')
    # Prompt user to input file name

    with open(_numbers_file_) as fin:
        data = fin.readlines()
        for line in data:
            intList.append(int(line.strip()))
    # open the file; read each number one line at a time;
    # and store it into intList list

    fin.close()
    # close the file
    # return the intList
    return intList


def sortListInAscendingOrder(lstInts):
    # FIXME2 #fixed

    lstInts.sort()
    # sort lstInts list in ascending order



def sortListInDescendingOrder(lstInts):
    # FIXME3 #fixed

    lstInts.sort(reverse = True)
    # sort lstInts in descending order
    


def printList(printFile, lstInts):
    for i in lstInts:
        # FIXME4

        printFile.write(f"{i}\n")
        # write each value one line at a time to file
        # handled by printFile object.
        pass
    printFile.write('\n')


def main():
    integers = []  # list to store integers
    integers = readData()
    outputFileName = input('Enter a file to write output to: ')
    printFile = open(outputFileName, 'w')
    printFile.write("Numbers entered:\n")
    printList(printFile, integers)
    # sort numbers
    sortListInAscendingOrder(integers)
    printFile.write("Numbers sorted in ascending order:\n")
    printList(printFile, integers)

    # FIXME5 #fixed
    # Call sortListInDescendingOrder function
    sortListInDescendingOrder(integers)

    # FIXME6 #fixed
    # Write the sorted list in descending order to the output file
    printFile.write('Numbers sorted in descending order:\n')
    printList(printFile, integers)

    # FIXME7 #fixed
    # Print the largest number to the output file
    printFile.write('The largest number is:\n')
    printFile.write(f"{integers[0]}\n")

    # FIXME8 #fixed
    # Print the smallest number to the output file
    printFile.write('The smallest number is:\n')
    printFile.write(f"{integers[9]}\n")


    printFile.close()
    print('Done executing the program! Check the output file for results.')


# FIXME9
# Call main function if this module is run as the main module
if __name__ == "__main__":
    main()