"""
Name: Carson Shields
hw9.py

Problem: hw9 problem

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from random import randint
from graphics import Entry, Text, Point, GraphWin, Line, Circle
def get_words(file_name):
    words = []
    file_object = open(file_name, "r")
    lines = file_object.readlines()
    for line in lines:
        words.append(line)

    return words

def get_random_word(words):
    rand = randint(0, len(words)-1)
    rand_word = str(words[rand]).replace("\n", "")
    return rand_word


def letter_in_secret_word(letter, secret_word):
    num = 0
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            num += 1
        num += 0

    if num >= 1:
        return True
    return False


def already_guessed(letter, guesses):
    num = 0
    for i in range(len(guesses)):
        if letter == guesses[i]:
            num += 1
        num += 0

    if num >= 1:
        return True
    return False

#make_hidden_secret("time", ["t", "i", "e"])
def make_hidden_secret(secret_word, guesses):
    hidden_words = []
    #secret_words = []
    lgth = (len(secret_word) * 2) - 1
    secret_words = list(secret_word)
    #print(secret_words)
    secret_words = ' '.join(secret_words)
    #print(secret_words)

    for i in range(lgth):
        if i % 2 == 0:
            hidden_words.append("_")
        else:
            hidden_words.append(" ")
    #print(hidden_words)

    for i in range(len(hidden_words)):
        for guess in guesses:
            if guess == secret_words[i]:
                hidden_words[i] = guess

    return "".join(hidden_words)

    #print(hidden_words)


def won(guessed):
    for guess in guessed:
        if guess == "_":
            return False
    return True


#play_graphics("time")
def play_graphics(secret_word):

    win = GraphWin("HangMan", 600, 600)
    Line(Point(200, 400), Point(300, 400)).draw(win)
    Line(Point(250, 200), Point(250, 400)).draw(win)
    Line(Point(250, 200), Point(200, 200)).draw(win)
    Line(Point(200, 200), Point(200, 250)).draw(win)

    guess_letter = Text(Point(235, 500), "Guess a Letter:")
    guess_letter.draw(win)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"
        , "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    guessed = []
    x_1 = 400
    y_1 = 100
    x_2 = 450
    y_2 = 100
    for i in range(len(alphabet)):
        pos_1 = Point(x_1, y_1)
        pos_2 = Point(x_2, y_2)
        if i <= 12:
            Text(pos_1, alphabet[i]).draw(win)
            y_1 = y_1 + 25
        else:
            Text(pos_2, alphabet[i]).draw(win)
            y_2 = y_2 + 25

    while not won(guessed) and guessed != alphabet:
        enter_guess = Entry(Point(295, 500), 2)
        enter_guess.draw(win)
        if letter_in_secret_word(enter_guess, secret_word):
            make_hidden_secret(secret_word, enter_guess)
        else:
            if enter_guess in alphabet:
                guessed.append(enter_guess)
        guessed.sort()

    if won(guessed):
        Text(Point(225, 100), "You Win").draw(win)
    win.getMouse()
    win.close()

    else:
        Text(Point(225, 100), "You Lose").draw(win)
        win.getMouse()
        win.close()


def play_command_line(secret_word):
    play_graphics(secret_word)



if __name__ == '__main__':
    play_command_line()
    play_graphics()

    # play_graphics(secret_word)
