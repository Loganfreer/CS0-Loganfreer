def printFlippedTriangle(height):
    """
    # Implement the function that takes height as an argument
    # and prints a triangle with * of given height.
    # Triangle of height 5, e.g., should look like the following.
    * * * * *
    * * * *
    * * *
    * *
    *
    """
    tri_height = range(height+1)
    for i in tri_height:
        print('* '*tri_height[-i])
    print()

def printsquare(height):
    i = 1
    while i <= height:
        print('* '*height)
        i += 1

height = 7
printFlippedTriangle(height)
printsquare(height)
