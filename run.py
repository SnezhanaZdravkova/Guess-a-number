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


def player_guess():
    """
    Get the guess fuigures input from the player
    """


def validate_guess():
    """
    check is the value an intiger and is it not less or equal to 0,
    or larger than player's guess.
    """
    guess = 0
    if int(guess) < 1 or int(guess) > 100:
        raise ValueError(
            f"You have entered {guess}."
            f"Please type a number larger than 0 and les then 100!"
        )
    else:
        pass


def play():
    """
    Function runs the main game
    """

    num = int(input())
    number = random.randint(1, num)
    guess = None
    score = 0
    while guess != number:
        guess = input(f"Please, enter a number between 1 and {num}: \n")
        if guess.isdigit():
            guess = int(guess)
        if guess < number:
            print("You need to guess higher. Try again!")
            guess = int(input("Please, enter a number: \n"))
            score += 1
        elif guess > number:
            print("You need to guess lower. Try again")
            guess = int(input("Please, enter a number: \n"))
            score += 1

    print("Congratulations! You guesed the number correctly!")
    print(f"You have reached the correct number in {score} guesses.")


def main():
    """
    function to run all others functions
    """
    welcome()
    player_guess()
    validate_guess()
    play()


main()
