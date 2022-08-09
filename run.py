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


def player_guess():
    """
    Get the guess fuigures input from the player
    """

    guess = int(input("Please, enter a number: \n"))
    validate_guess(guess)


def validate_guess(value):
    """
    Inside the try,
    check is the value an intiger and is it not less or equal to 0
    """

    try:
        if value <= 0:
            raise ValueError(
                f"You have entered {value}."
                f"Please type a number larger than 0 next time"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


player_guess()
