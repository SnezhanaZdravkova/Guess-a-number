"""
used for imports
"""
import random


def welcome():
    """
    Define the decision of the player
    """

    print("Welcome to 'Guess a number game'! ")
    print("In this game you will need to guess a number between 1 and 100. ")
    print("You can guess only one number at a time ")
    print("And computer will respond.")

    name = input("Enter your name, please: \n")
    playing = input(
        f"Hello {name}! Do you want to play? "
        f"Please enter 'Q' to quit or any letter to play: \n")
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
    check is the value an intiger and is it not less or equal to 0,
    or larger than 100.
    """
    while value is int:
        try:
            # return int(input(value))
            if value <= 0 or value > 100:
                raise ValueError(
                    f"You have entered {value}."
                    f"Please type a number larger than 0 and les then 100!"
                )
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            break
    else:
        print("Please, enter a number between 1 and 100!")


player_guess()
