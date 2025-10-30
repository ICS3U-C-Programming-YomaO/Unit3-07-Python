#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October 2025
# This program checks if user can date my grandchild

import random


def main():

    # get age from user
    user_age = input("Hey! Enter your age please: ")
    # type cast to integer
    try:
        user_age = int(user_age)

        # check if age within requirements 
        if user_age > 25 and user_age < 41:
            print("You can date my grandchild!")
        else:
            print("You cannot date my grandchild")

    except ValueError:
        # exception handling
        print("ERROR! You have to enter a valid age!")
    #end game
    finally:
        print("Thanks for playing my game!")


if __name__ == "__main__":
    main()
