#!/usr/bin/env python3
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getNumberOfSquares():
    # Obtains numerical input (x) from the user, and returns 4**x
    squareNumberN = int(input("How many squares to descretize into (give n in 4^n): "))
    if squareNumberN <= 0:
        print("Can't do such a calculation.")
        return 0
    else:
        return  4**squareNumberN

def printMatrix(matrix, rowMax, columnMax):
    # prints integer matrix in a near manner
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
    capCoordLow = []  # coordinate matrix for descretized bottom
    capCoordTop = []  # coordinate matrix for descritized top

    squareNumber = getNumberOfSquares()  # Obtain the number of squares wanted from the user
    sqaureInRow = int(squareNumber**(1/2))  # Gets the number of sqares per row
    dx = ((w**2) / squareNumber)**(1/2)  # Turns number of squares into dx distance

    calcCoord(capCoordLow, sqaureInRow, sqaureInRow, dx, 0)  # calculate descritized coordinates
    calcCoord(capCoordTop, sqaureInRow, sqaureInRow, dx, d)

    #DEBUGGING
    for s in capCoordLow:
        print(*s)
    print("")
    for s in capCoordTop:
        print(*s)


    return 0


main()

