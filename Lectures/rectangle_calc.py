'''
step 1: prompt for two sides
step 2: calc area
step 3: calc perimeter
step 4: print out area and perimeter
'''

def calc_area(side1, side2):
    area = side1 * side2 
    return area

def calc_perim(side1, side2): 
    perim = (2 * side1) + (2 * side2)
    return perim


def main():
    #step1
    side1 = float(input('Please enter side 1: '))
    side2 = float(input('Please enter side 2: '))
    
    rect_area = calc_area(side1, side2)
    rect_perim = calc_perim(side1, side2)

    print(f"The area of a rectangle with sides: {side1} and {side2} is {rect_area}")
    print(f"The perimeter of a rectangle with sides: {side1} and {side2} is {rect_perim}")