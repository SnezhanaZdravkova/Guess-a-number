"""
used for imports
"""
import random


def display_title():
    """
    Function used only to print the title of the game.
    """
    print("GUESS A NUMBER")
    print()


def welcome():
    """
    Define the decision of the player
    """

    print("Welcome to 'Guess a number game'! ")
    print("In this game you will need to guess a number. ")
    print("You can guess only one number at a time ")
    print("And computer will respond.")

    name = input("Enter your name, please: \n")
    print("Hello ", name, "!")
    print()
    # playing = input(
    #     f"Hello {name}! Do you want to play? "
    #     f"Please enter 'Q' to quit or any letter to play: \n")
    # if playing.lower() == "q":
    #     quit()
    # else:
    #     print("Okay! Let's play :)")


def play(wins):
    """
    Function runs the main game
    """

    level_dame = input("What game level would you like to play?\
         E for Easy, M for Medium, or H for High: ")

    if level_dame.lower() == "e":
        max_number = 10
        guesses = 5
    elif level_dame.lower() == "m":
        max_number = 100
        guesses = 10
    elif level_dame.lower() == "h":
        max_number = 1000
        guesses = 8
    else:
        print("Sorry! Invalid guess. Please try again!")

    number = random.randint(1, max_number)
    print(f"The secret number is a number inrange from 1 to {max_number}")
    print()
    score = 1
    while score <= guesses:
        guess = int(input("Please, enter a number: \n"))

        if guess < number:
            print("You need to guess higher. Try again!")
            score += 1
        elif guess > number:
            print("You need to guess lower. Try again")
            score += 1
        elif guess == number:
            print(f"Congratulations! You guesed the number {number} correctly!")
            print(f"You have reached the correct number in {score} guesses.")
            wins += 1
            print("You have won ", wins, "games.")
            return wins


def main():
    """
    function to run all others functions
    """
    display_title()
    welcome()
    # Initialize variable
    wins = 0
    # give the player chance to play again
    start_again = "y"
    while start_again.lower() == "y":
        wins = play(wins)
        start_again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")


# If started as the main module, call the main function
if __name__ == "__main__":
    main()
