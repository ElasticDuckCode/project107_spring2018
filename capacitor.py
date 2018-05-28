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

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates

    squareNumber = getNumberOfSquares(); print(squareNumber, " -> number of squares")  # FOR DEGBUGGING
    sqaureInRow = int(squareNumber**(1/2))
    dx = ((w**2) / squareNumber)**(1/2); print(dx, " -> dx value")  # FOR DEGBUGGING

    capCoord = []
    calcCoordBottom(capCoord, sqaureInRow, sqaureInRow, dx)
    print(capCoord)

    return 0

#creating array of 0's for later use
def createCap(capCoord, squareNumber): 
	for i in range(0,squareNumber):
            capCoord.append([0,0,0])
            print(capCoord)

def calcCoordBottom(array, x, y, dx):
    xpos = 0
    ypos = 0
    for i in range(0, x):
        for j in range(0, y):
            array.append([xpos, ypos, 0])
            xpos = xpos + dx
        ypos = ypos + dx
        xpos = 0



main()

