import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def getNumberOfSquares():
    # Obtains numerical input (x) from the user, and returns 4**x
    squareNumberN = int(input("How many squares to descretize a surface into (give n in 4^n): "))
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

def calcCoord(x, y, zBot, zTop, dx):
    # Calculates the discritized coordinates of the capacitor
    xpos = 0 
    ypos = 0
    array = []

    for i in range(0, x):
        for j in range(0, y):
            array.append([xpos, ypos, zBot])
            xpos = xpos + dx
        ypos = ypos + dx
        xpos = 0

    xpos = 0 
    ypos = 0

    for i in range(0, x):
        for j in range(0, y):
            array.append([xpos, ypos, zTop])
            xpos = xpos + dx
        ypos = ypos + dx
        xpos = 0

    array = np.array(array) # return numpy array instead of python list
    return array

def getZMatrix():
    # TODO Lina
    return Z

def getvVector(Coord, squareNumber, v0, dBot, dTop):
    # TODO similar to Z matrix
    v = np.zeros(2*squareNumber) # 2 * squareNumber because doing top and bottom surfaces
    print(v, "getV Zeroes\n")
    for i in range(0, 2*squareNumber):
        if Coord[i][2] == dBot:
            v[i] = -v0 / 2
        if Coord[i][2] == dTop:
            v[i] = v0 / 2
    return v

def solveCharge(Z, v):
    # Z = descretized matrix (numpy array)
    # v = voltage vector (numpy array)
    # equation: v = Zq
    # solution: q = Z^-1 v

    try: # test invertibility of Z
        Zinv = np.linalg.inv(Z)
    except np.linalg.LinAlgError:
        # not invertible. skip this one.
        print("Singluar Z Matrix!")
        return np.zeros([1,1])
        pass
    else:
        q = Zinv.dot(v)
        return q


