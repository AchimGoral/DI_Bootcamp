board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def display_board(board):

    print("")
    print("Tic Tac Toe")
    print("")
    print("*************")
    print(f"* {board[0]} | {board[1]} | {board[2]} *")
    print("*-----------*")
    print(f"* {board[3]} | {board[4]} | {board[5]} *")
    print("*-----------*")
    print(f"* {board[6]} | {board[7]} | {board[8]} *")
    print("*************")
    print("")

def check_board():
    pass


def player_input():
    pass

    

def check_win():
    # Horizontal
    if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
        # condition
        pass
    if board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
        pass
    if board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
        pass
    # Vertical
    if board[6] == board[3] and board[3] == board[0] and board[6] != ' ':
        pass
    if board[7] == board[4] and board[4] == board[1] and board[7] != ' ':
        pass
    if board[8] == board[5] and board[5] == board[2] and board[8] != ' ':
        pass
    # Diagonal
    if board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
        pass
    if board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
        pass



def game():
    pass

display_board(board)