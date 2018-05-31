#!/usr/bin/env python3
from capacitorFunctions import *


## MAIN FUNCTION ######################################################################################################
## Written By Jake Millhiser & Lina Yi ################################################################################

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates
    v0 = 1  # 1 volt, not specified by problem

    printTitle() # print our cool title

    squareNumber = getNumberOfSquares()  # Obtain the number of squares wanted from the user
    squareInRow = int(squareNumber**(1/2))  # Set the number of sqares per row
    dx = ((w**2) / squareNumber)**(1/2)  # Turns number of squares into dx distance
    capCoord = calcCoord(squareInRow, squareInRow, 0, d, dx)  # calculate descritized coordinates (bottom surface)

    v = getvVector(capCoord, squareNumber, v0, 0, d)
    Z = getZMatrix(squareNumber, capCoord, dx)
    Q = solveCharge(Z,v)
    C = solveCapacitance(Q, v0, squareNumber)

#    test = [[7,8,9],
#            [4,5,6],
#            [1,2,3]]
#    test = np.array(test)
#    surfColorPlt(test)

    #DEBUGGING
    print(capCoord, "Coordinate Matrix\n")
    print(v, "Volage Vector\n")
    print(Z, "Z matrix\n")
    print(Q, "Charge Vector\n")
    print(C, "F  Capacitance\n")

    Q0 = solveChargeMatrix(Q, squareNumber, squareInRow)
    surfColorPlt(Q0)
    surf3DPlt(Q0, squareInRow)
    return 0

main()
