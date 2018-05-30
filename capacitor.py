#!/usr/bin/env python3
from capacitorFunctions import *


## MAIN FUNCTION ######################################################################################################

# Written By Jake Millhiser & Lina Yi

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates
    v0 = 1  # 1 volt, not specified by problem

    squareNumber = getNumberOfSquares()  # Obtain the number of squares wanted from the user
    sqaureInRow = int(squareNumber**(1/2))  # Set the number of sqares per row
    dx = ((w**2) / squareNumber)**(1/2)  # Turns number of squares into dx distance
    capCoord = calcCoord(sqaureInRow, sqaureInRow, 0, d, dx)  # calculate descritized coordinates (bottom surface)

    v = getvVector(capCoord, squareNumber, v0, 0, d)

    #DEBUGGING
    print(capCoord, "Python List\n")
    print(v, "Volage Vector\n")


    return 0

main()

