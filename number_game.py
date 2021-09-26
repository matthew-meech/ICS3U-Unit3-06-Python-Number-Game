#!/usr/bin/env python3

# Created by: Mr. Matthew Meech
# Created on: Sep 2021
# This program is a number guessing game


import random


def main():

    # input
    answer = random.randint(0, 9)
    number = input("Enter number 0-9: ")
    print("")

    # process & output
    try:
        integer_as_number = int(number)
        if number == answer:
            print("You guess right")
        else:
            print("you guessed wrong!")

    except Exception:
        print("This is not a number 0-9")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
