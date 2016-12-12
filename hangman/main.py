__author__ = 'Josh'
import sys
import os

hangman = ['      _______\n     |/      |\n     |      \n     |      \n     |       \n     |      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \n     |       \n     |'
           '      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |       |\n     |       \n     |'
           '      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \|\n     |       \n     |'
           '      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       \n     |'
           '      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |'
           '      \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |'
           '      / \n     |\n    _|____',
           '      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |'
           '      / \\\n     |\n    _|____']
true_possible = ['y', '1', 'true', 'yes']
false_possible = ['n', '0', 'false', 'no']
curr_count = 0
curr_word = ''
curr_guessed = []
defaults = [' ', '-', '\'', ':', ';', '<', '>', '?', '&', '\"', '?', '.', ',', '/', '!']

if sys.platform == 'win32':
    clear = lambda: os.system('cls')
elif sys.platform == 'linux2' or sys.platform == 'darwin':
    clear = lambda: os.system('clear')


def exit_game(message):  # Exits game with message
    clear()
    print('\n' + message)
    sys.exit()


def get_bool_input(msg):
    tmp_input = ''
    count = 0
    while not tmp_input and count < 5:
        try:
            tmp_input = raw_input(msg).lower()
            if tmp_input in true_possible:
                return 1
            elif tmp_input in false_possible:
                return 0
            else:
                raise NameError('Must be boolean input. ')
        except NameError:
            print("Must be valid boolean input. ")
            count += 1
            tmp_input = ''
    if count == 5:
        exit_game("Game has ended since you refused to enter a valid number. ")


def get_curr_text():
    out = ''
    for i in curr_word:
        if i in defaults:
            out += i + ' '
        elif i not in curr_guessed:
            out += '_ '
        else:
            out += i + ' '
    return out


def print_board():
    print(hangman[curr_count] + '\n\n')
    print(get_curr_text())


def get_str_input(msg):
    tmp_input = ''
    count = 0
    while not tmp_input and count < 5:
        try:
            tmp_input = raw_input(msg).lower()
            if len(tmp_input) < 3:
                raise NameError('Must be longer than three letters. ')
        except NameError as e:
            print(e)
            count += 1
            tmp_input = ''
    if count == 5:
        exit_game("Game has ended since you refused to enter a valid word. ")
    return tmp_input


def get_char_input(msg, not_in):
    tmp_input = ''
    count = 0
    while not tmp_input and count < 5:
        try:
            tmp_input = raw_input(msg).lower()
            if len(tmp_input) != 1:
                raise NameError('Must be one letter. ')
            if not_in:  # Throw error if the letter has been guessed
                if tmp_input in curr_guessed:
                    raise NameError('Already guessed that letter. ')
                if tmp_input in defaults:
                    raise NameError('That is a default character. ')
        except NameError as e:
            print(e)
            count += 1
            tmp_input = ''
    if count == 5:
        exit_game("Game has ended since you refused to enter a valid letter. ")
    return tmp_input


def guessed_all():
    for i in curr_word:
        if i not in curr_guessed + defaults:
            return False
    return True


def keep_playing():  # Backwards, if not keep playing, keep playing
    if curr_count == 7:
        return 'You loose! '
    elif guessed_all():
        return '\nWinner! '
    else:
        return None


# print reduce(lambda x, y: str(x) + str(y), outstr)
cont = 1
clear()
while cont:
    curr_word = get_str_input('Word? ').lower()
    clear()
    while not keep_playing():
        print_board()
        curr_guessed += get_char_input('Letter guess? ', 1)
        if curr_guessed[-1] not in curr_word:
            curr_count += 1
        clear()
    print_board()
    print(keep_playing())
    if not get_bool_input('Would you like to play again? '):
        exit_game('Thank you for playing! ')
    clear()
    curr_count = 0
    curr_word = ''
    curr_guessed = []

# """