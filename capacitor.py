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

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates

    squareNumber = getNumberOfSquares(); print(squareNumber, " -> number of squares")  # FOR DEGBUGGING

    dx = ((w**2) / squareNumber)**(1/2); print(dx, " -> dx value")  # FOR DEGBUGGING
    return 0


main()

