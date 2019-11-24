#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Nov 2019
# This program calculates volume of a cylinder using multiple functions

import math


def calculator(radius, length):
    # This calculates volume of a cylinder based on inputs from main
    # process
    volume = (math.pi * radius * radius * length)

    return (volume)


def main():
    while True:
        try:
            # input
            radius = float(input("Input the radius of your cylinder: "))
            length = float(input("Input the length of your cylinder: "))

            # runs calculator function
            volume = calculator(radius, length)

            # output
            print("The volume of your cylinder is " + str(volume) + " units^3")
            break
        except Exception:
            print("Please input only proper values.")


if __name__ == "__main__":
    main()
