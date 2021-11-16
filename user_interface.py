"""

This module formats the word search matrix and also runs the game in the if __name__ = ' __main__ ' loop.
It also has multiple functions which helps to run the matrix and return the points and ask the user input when creating
the board.

List of functions created in this module:
 - cli_formatter(grid)
 - start_game()
 - user_guess()
 - outro(points = 0) --> points is an optional parameter in this function which is why it has a default value.


"""


import time
from refdef import create_word_search
from refdef import check_answer

global board
global correct_guess


def cli_formatter(grid):
    """
    This function formats the word search matrix for the command line

    Args:
        grid (list): In this case, grid is a list because it is coming from the create_word_search function to be formatted.
    """
    for i in range(len(grid)):
        print(' '.join(grid[i]))


def start_game():
    """

    This function starts the game by printing the welcome message onto the command line and asks the user to input
    how large they want their matrix to be, then prints the board and uses cli_formatter to do so.


    """
    file = open('welcome_message.txt', 'r')
    msg = file.read()
    print(msg + "\n")
    file.close()

    grid_size = int(input(
        "Please enter the dimensions for your board.\n(Will be in X by Y format so please just enter one number.): "))

    global board
    board = create_word_search(grid_size, "words.txt")
    cli_formatter(board)


def user_guess():
    """

    This function takes in the user guess and checks if it was correct using the check_answer function from refdef.py.
    If the word is correct, it appends it to a new list, correct_guess. Otherwise, it returns False.

    """
    guess_list = []

    guess = input("Guess here then enter 'FINISHED' to end game: ")

    guess_list.append(guess.upper())

    i = 0
    while i < 3:
        x = input()

        if x == 'FINISHED':
            break
        else:
            guess_list.append(x.upper())
            i = i + 1

    global correct_guess
    correct_guess = []

    for j in range(0, len(guess_list)):

        correct = check_answer(guess_list[j], board)

        if correct:
            correct_guess.append(guess_list[j])

        else:
            return False

    # print(check_answer(guess, board))


def outro(points=0):
    """

    This function checks if the time_elapsed is less than 60 seconds and if it is true, it returns the correct guesses,
    if not it returns that they've not scored any points.

    Args:
        points: This is an optional parameter, specified with the default value of 0.

    Returns:
        This returns how many points the user has scored and how long it took them to do so.
        The points are counted by the sum of the length of each correct word.

    """
    if time_elapsed <= 60:
        for i in range(len(correct_guess)):
            points = points + len(correct_guess[i])

        print("Points scored: ", points)
        print("Time elapsed: ", time_elapsed)

    else:
        print("No points scored.")
        print("Time elapsed: ", time_elapsed)


if __name__ == '__main__':

    start_game()

    start = time.time()

    user_guess()

    end = time.time()

    time_elapsed = end - start

    outro()

    # print("The correct words were: ", word_list) --> if wanted, can print the final word list before or after
    # guessing the words.
