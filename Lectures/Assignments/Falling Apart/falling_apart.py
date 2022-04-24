'''
Name: Logan Freerksen
Date: 04/21/22

This program will define a functions that complete the "Falling Apart" activity on Kattis. Taking in a number of pieces
and creating that many elements of things to choose upon, with the elements being integer values between 1 and 100. The output 
is the integer value of the elements collected betweeen the two players as described in the description


'''


def create_list(elements):
    element_list = []
    first_list = elements.split()
    for i in first_list:
         element_list.append(int(i))
    return element_list

def sort_list(element_list):
    element_list.sort()
    return element_list

def splitting_up(sorted_list):
    AliceSum = 0
    BobSum = 0
    AliceTurn = sorted_list[-1::-2]
    BobTurn = sorted_list[-2::-2]
    for i in AliceTurn:
        AliceSum = AliceSum + i
    for j in BobTurn:
        BobSum = BobSum + j
    
    return AliceSum, BobSum

def test():
    assert splitting_up([1, 2, 2, 1]) == (3, 3)
    assert splitting_up([6, 4, 3]) == (9, 4)
    print("All test cases passed!")

def main():
    #test()
    input()
    elements = input()
    element_list = create_list(elements)
    sorted_list = sort_list(element_list)
    AliceSum, BobSum = splitting_up(sorted_list)
    print(f"{AliceSum} {BobSum}")
    




if __name__ == "__main__":
    main()