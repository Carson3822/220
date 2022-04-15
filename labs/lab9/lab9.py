"""

Name: Carson Shields
lab9.py

Problem: tik tac toe
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if type(board[position - 1]) != str:
        return True
    else:
        return False


def fill_spot(board, position, character):
    character = character.lower()
    character = character.strip()
    board[position - 1] = character


def winning_game(board):
    row_1 = [board[0], board[1], board[2]]
    row_2 = [board[3], board[4], board[5]]
    row_3 = [board[6], board[7], board[8]]
    column_1 = [board[0], board[3], board[6]]
    column_2 = [board[1], board[4], board[7]]
    column_3 = [board[2], board[5], board[8]]
    diag_1 = [board[0], board[4], board[8]]
    diag_2 = [board[2], board[4], board[6]]

    list_combos = [row_1, row_2, row_3, column_1, column_2, column_3, diag_1, diag_2]

    for item in list_combos:
        if item[0] == item[1] == item[2]:
            return True

    return False


def game_over(board):
    positions = [board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]]
    for position in positions:
        if type(position) != str:
            return False
    else:
        return True


def get_winner(board):
    item_winner = ""
    row_1 = [board[0], board[1], board[2]]
    row_2 = [board[3], board[4], board[5]]
    row_3 = [board[6], board[7], board[8]]
    column_1 = [board[0], board[3], board[6]]
    column_2 = [board[1], board[4], board[7]]
    column_3 = [board[2], board[5], board[8]]
    diag_1 = [board[0], board[4], board[8]]
    diag_2 = [board[2], board[4], board[6]]

    list_combos = [row_1, row_2, row_3, column_1, column_2, column_3, diag_1, diag_2]

    for item in list_combos:
        if item[0] == item[1] == item[2]:
            item_winner += item[0]

    return item_winner


def play(board):
    y_n = "y"

    while y_n[0] == "y":
        board =  build_board()
        print("tik-tac-toe")
        print("x's go first")
        print_board(board)
        inputs = ["x", "o"]
        counter = 0
        while not game_over(board):
            inpt = inputs[counter % 2]
            play = eval(input(f"{inpt}'s, choose a position: "))
            while not is_legal(board, play):
                play = eval(input("x's, choose a position: "))

            fill_spot(board, play, f"{inpt}")
            print_board(board)
            counter += 1

            if winning_game(board):
                print(f"{get_winner(board)}'s wins!")

        if game_over(board):
            print("tie")
            user_input = input("do you wish to keep playing?: ")
            y_n = user_input.strip().lower()
        else:
            user_input = input("do you wish to keep playing?: ")
            y_n = user_input.strip().lower()


def main():
    board = build_board()
    play(board)


if __name__ == '__main__':
    main()


