"""

This module creates the word search matrix and places the words and randomized letters
to fill the rest of the matrix. It also checks the answer that the user will input.

List of functions created in this module:
 - create_word_search(grid_size, handle)
 - check(x, y, d, word_length)
 - place_word(word, grid)
 - check_answer(guess, grid)


"""

import random
import string
# from pprint import pprint


def create_word_search(grid_size, handle):
    """

    This function takes two arguments: grid_size and handle.
    Both are used to create the word search matrix and to get words to put into
    the matrix. This function returns the matrix and also has a couple nested functions
    that place the word and check if it can be placed.

    Args:
        grid_size (int): This is how large the user wants the word search matrix to be.
        handle: This is the words.txt file however, it can be changed to use any plain text file.

    """

    # this opens the file, reads each line and then closes the file
    file = open(handle)
    words = file.readlines()
    file.close()

    word_list = []
    select_word = False

    # this loop chooses a list of words from the handle then puts it into an empty list,
    # wordList, that has the maximum length of
    # the grid_size-2 and chooses the grid_size//2 for the amount of words
    for word in range(grid_size // 2):
        while not select_word:
            word = random.choice(words).upper().replace("\n", '')
            if len(word) <= grid_size - 2:
                word_list.append(word)
                select_word = True
            else:
                select_word = False

    # If you want to print the list of words that are inside the matrix, then use this statement to do so:
    # pprint(wordList, '\n')
    # If you want to make this game harder for the user, then don't use this statement.


    grid = [['_' for _ in range(grid_size)] for _ in range(grid_size)]

    def check(x, y, d, word_length):
        """

        Args:
            word_length: Takes the value of the length of the word that we are checking
            d (list): Takes the direction of the word that is being placed: Up, Down or Diagonal.
            y (int): The y-value of where the word is being placed.
            x (int): The x-value of where the word is being placed.

        """
        check_word = True

        if d == [1, 0]:
            x = 1
            y = 0
            for i in range(0, word_length):  # for every letter in the length of the word
                if grid[y][x + i] != '_':
                    check_word = False
        if d == [0, 1]:
            x = 0
            y = 1
            for i in range(0, word_length):  # for every letter in the length of the word
                if grid[y + i][x] != '_':
                    check_word = False
        if d == [1, 1]:
            x = 1
            y = 1
            for i in range(0, word_length):  # for every letter in the length of the word
                if grid[y + i][x + i] != '_':
                    check_word = False

        for i in range(0, word_length):  # for every letter in the length of the word
            if grid[y + i][x + i] != '_':  # if the x and y position of the grid contains '_'
                check_word = False
        return check_word

    def place_word(word, grid):
        """
        This function places the word onto the word search matrix, character by character.

        Args:
            grid: This is the matrix, in this context it would place the word onto the matrix.
            word (String): This is the word that will go into the matrix.

        """
        word_length = len(word)

        d = random.choice([[1, 0], [0, 1], [1, 1]])

        x_size = grid_size if d[0] == 0 else grid_size - word_length
        y_size = grid_size if d[1] == 0 else grid_size - word_length

        x = random.randrange(0, x_size)
        y = random.randrange(0, y_size)

        for i in range(0, word_length):
            grid[y + d[1] * i][x + d[0] * i] = word[i]
        return grid

    grid = [[random.choice(string.ascii_uppercase) for i in range(0, grid_size)] for j in range(0, grid_size)]

    for word in word_list:
        # this for loop places each word, and checks if it can be placed.
        # it chooses the coordinates of where the words will be placed (x_size, y_size)
        d = random.choice([[1, 0], [0, 1], [1, 1]])

        x_size = grid_size if d[0] == 0 else abs(grid_size - len(word))
        y_size = grid_size if d[1] == 0 else abs(grid_size - len(word))

        x = random.randrange(0, x_size)
        y = random.randrange(0, y_size)

        check(x_size, y_size, d, len(word))

        if not check(x, y, d, len(word)):
            grid = place_word(word, grid)
        else:
            break

    # grid =  ("\n".join(map(lambda row: " ".join(row), grid))) -->
    # if you printed this, it would print the grid as if cli_formatter() didn't exist

    return grid

    # print ('\n'+"Words are: ")


def check_answer(guess, grid):
    """

    This function checks the answer that the user has inputted and returns True if it is on the grid and in words.txt,
    and False if it is not.

    Args:
        grid: Takes the value of the grid. (the wordsearch matrix)
        guess (String): This is the guess that the user has inputted.

    """
    words_new = []
    file = open('words.txt')
    words = file.readlines()
    for word in words:
        words_new.append(word.upper().replace("\n", ''))
        # this makes sure there are no spaces or "\n" in words.txt and appends the words to a new list, words_new.
    file.close()

    if guess.upper() in words_new:
        # if the word has been placed then return true, otherwise return false
        return True
    else:
        return False

    # this would check if the word is on the grid, however, since check(x, y, d, word_length) already exists,
    # it is not necessary to check the answer as it is checked if the word is placed on the grid anyways.

    # guess_split = []

    # i = 0

    # for i in len(guess):
    #    guess_split.append(guess[i])
    #    i += 1

    # if guess.upper() is wordList:
    #    return True #any(guess_spilt == grid[i:len(guess_split)+i] for i in range(len(grid) - len(guess_split) + 1))
    # else:
    #    return False
