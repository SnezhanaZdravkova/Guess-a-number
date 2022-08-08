"""
used for imports
"""
import random


def welcome():
    """
    Define the decision of the player
    """

    print("Welcome to 'Guess a number game'! ")
    print("In this game you will need to guess a number between 1 and 10. ")
    print("You can guess only one number at a time.")

    name = input("Enter your name, please: \n")
    playing = input(
        f"Hello {name}! Do you want to play? "
        f"Please enter 'Yes' to play or 'Q' to quit: \n")
    if playing.lower() == "q":
        quit()
    else:
        print("Okay! Let's play :)")


welcome()
