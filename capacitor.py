#!/usr/bin/env python3
from capacitorFunctions import *


## MAIN FUNCTION ######################################################################################################
## Written By Jake Millhiser & Lina Yi ################################################################################

def main():
    w = 1e-2  # width of capacitor
    d0 = 3e-3  # distance between capacitor plates
    v0 = 1  # 1 volt, not specified by problem

    printTitle() # print our cool title
    squareNumber = getNumberOfSquares()  # Obtain the number of squares wanted from the user

    # Problem 1
    solveDiscrete(w, d0, v0, 1, squareNumber)

    # Problem 2
    d1 = 1e-3
    d2 = 4e-2
    step = d1
    current = d1
    c = []

    while current <= d2:
        c.append(solveDiscrete(w, current, v0, 0, squareNumber))
        current += step
        print("Done! on step: ", current)
    c = np.array(c)

    discreteVSFormula(c, d1, d2, step, w)

main()
