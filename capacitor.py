#!/usr/bin/env python3

def main():
    w = 1e-2  # width of capacitor
    d = 3e-3  # distance between capacitor plates

    squareNumberN = int(input("How many squares to descretize into (give n in 4^n): "))
    squareNumber = 4**squareNumberN
    print(squareNumber)

main()

