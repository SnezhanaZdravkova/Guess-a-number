"""
used for imports
"""
import random

number = random.randrange(1, 100)


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


def player_guess():
    """
    Get the guess fuigures input from the player
    """

    guess = int(input("Please, enter a number: \n"))
    validate_guess(guess)


def validate_guess(guess):
    """
    Inside the try,
    check is the value an intiger and is it not less or equal to 0,
    or larger than 100.
    """
    while guess is int:
        try:
            # return int(input(value))
            if guess <= 0 or guess > 100:
                raise ValueError(
                    f"You have entered {guess}."
                    f"Please type a number larger than 0 and les then 100!"
                )
            else:
                play()
        except ValueError as error:
            print(f"Invalid data: {error}, please try again.\n")
            break


def play():
    """
    Function runs the main game
    """
    guess = int(input())
    while guess != number:
        if guess < number:
            print("You need to guess higher. Try again!")
            guess = int(input("Please, enter a number: \n"))
        elif guess > number:
            print("You need to guess lower. Try again")
            guess = int(input("\nPlease, enter a number: \n"))

    print("Congratulations! You guesed the number correctly!")


def main():
    """
    function to run all others functions
    """
    welcome()
    player_guess()
    validate_guess(input())
    play()


main()
