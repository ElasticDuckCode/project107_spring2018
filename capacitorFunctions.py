#!/usr/bin/env python3
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

Eo = 8.85e-12

def printTitle():
    print("\nWritten by Jake Millhiser and Lina Yi.",
          "\nECE 107 Project: Discrete Capacitance of Square Capacitor"
          "\nMay 2018\n")
    try:
        image = open('img.txt','r')
    except IOError:
        pass
    else:
        imageLd = image.read()
        print(imageLd)
        image.close()
    return


def getNumberOfSquares():  # Obtains numerical input x from the user, and returns 4**x if valid. Otherwise returns 0
    squareNumberN = int(input("Give a positive integer (n) for 4^(n) discrete segments of the capacitor surface > "))
    if squareNumberN < 0:
        print("Can't do such a calculation.")
        return 0
    else:
        return  4**squareNumberN

def printMatrix(matrix, rowMax, columnMax):  # prints python list as a matrix in a neat manner
    # matrix:  python list
    # rowMax:  largest row index
    # column max:  largest column index
    for row in range(0, rowMax):
        print("[ ", end="")
        for column in range(0, columnMax):
            print(matrix[row][column], end=" ")
        print("]", end="\n")
    return

def calcCoord(x, y, zBot, zTop, dx):  # Calculates the discrete coordinates of the capacitor segments
    # x:  length of capacitor plate
    # y:  width of capactior plate
    # zBot:  z coordinate of bottom plate
    # zTop:  z coordinate of top plate
    # dx:  step value for plate creation

    array = [] # make list for appending coordinates
    xpos = 0 
    ypos = 0

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

    array = np.array(array) # return numpy array instead of list
    return array

def getZMatrix(squareNumber, Coord, dx):  # Creates the Z Matrix in descretized capacitance equation
    Z = np.zeros((2*squareNumber,2*squareNumber))
    dSn = (dx)**2

    for m in range(2*squareNumber):
        for n in range (2*squareNumber):
            if m == n:
                Z[m][n] = 1/(2*Eo*np.sqrt(np.pi*dSn))
            else:
                r = np.linalg.norm(Coord[m] - Coord[n])
                Z[m][n] = 1/(4*(np.pi)*Eo*r)
    return Z

def getvVector(Coord, squareNumber, v0, dBot, dTop):  # Creates the voltage vector of both the top and bottom surfaces.
    # Coord:  coordinate matrix 
    # squareNumber:  number of squares on one surface
    # v0:  voltage difference between the two plates
    # dBot:  position of bottom plate
    # dTop:  position of the top plate

    # Top voltage is assigned v0/2, bottom voltage assigned -v0/2
    v = np.zeros(2*squareNumber) # 2 * squareNumber because doing top and bottom surfaces
    for i in range(0, 2*squareNumber):
        if Coord[i][2] == dBot:
            v[i] = -v0 / 2
        if Coord[i][2] == dTop:
            v[i] = v0 / 2
    return v

def solveCharge(Z, v):
    # Z:  descretized matrix (numpy array)
    # v:  voltage vector (numpy array)

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

def solveCapacitance(q, v0, squareNumber):
    # q: charge vector
    # v0: voltage applied to plates
    # squareNumber: number of squares on a plate

    Q = 0 # total charge on plate initally 0
    for dankmemes in range(squareNumber):
        Q = Q + q[dankmemes]
    C = -Q/v0 # negate Q since we are summing charges on bottom plate rather than top
    return C

def solveChargeMatrix(q, squareNumber, squareInRow):
    # q: charge vector
    # squareNumber: number of squares on a surface
    # squareInRow: number of squares in a row
    #|7|8|9|
    #|4|5|6| how our charges are aranged
    #|1|2|3|
    k = 0 # current vector index
    Q = np.zeros((squareInRow, squareInRow))
    for i in range(squareInRow-1, -1, -1): # from squareNumber-1 to 0
        for j in range(squareInRow):
            Q[i][j] = -q[k] # negate since bottom plate
            k = k + 1 # increment to next charge
    return Q

def surfColorPlt(A):
    # Heat Map
    #A = np.random.random((size, size))
    plt.imshow(A, cmap='plasma',interpolation='gaussian')
    plt.colorbar()
    plt.show()
    return

def surf3DPlt(A, squareInRow):
# Surface Plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = y = np.arange(squareInRow)
    x, y = np.meshgrid(x, y)
    surf =  ax.plot_surface(x,y,A, color='orange')
#fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

