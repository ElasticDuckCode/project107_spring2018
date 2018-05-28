#!/usr/bin/env python3
import math
import numpy as np

def getNumberOfSquares():
    squareNumberN = int(input("How many squares to descretize into (give n in 4^n): "))
    if squareNumberN <= 0:
        print("Can't do such a calculation.")
        return 0
    else:
        return  4**squareNumberN

def printMatrix(matrix, rowMax, columnMax):
    for row in range(0, rowMax):
        print("[ ", end="")
        for column in range(0, columnMax):
            print(matrix[row][column], end=" ")
        print("]", end="\n")
    return

def calcCoord(array, x, y, dx, z):
    # Calculates the discritized coordinates of the capacitor
    xpos = 0 
    ypos = 0

    for i in range(0, x):
        for j in range(0, y):
            array.append([xpos, ypos, z])
            xpos = xpos + dx
        ypos = ypos + dx
        xpos = 0

## MAIN FUNCTION ######################################################################################################

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates

    squareNumber = getNumberOfSquares(); print(squareNumber, " -> number of squares")  # FOR DEGBUGGING
    sqaureInRow = int(squareNumber**(1/2))
    dx = ((w**2) / squareNumber)**(1/2); print(dx, " -> dx value")  # FOR DEGBUGGING
    print("")

    capCoord = []
    calcCoord(capCoord, sqaureInRow, sqaureInRow, dx, 0)
    calcCoord(capCoord, sqaureInRow, sqaureInRow, dx, d)
    for s in capCoord:
        print(*s)

    return 0


main()

