board = [' ', ' ', ' ', 
         ' ', ' ', ' ', 
         ' ', ' ', ' ']

# Flag for win: checks for winning condition
win = False
# counts the games with win check after 5 and ends with 9 moves
game_counter = 0


def display_board():

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

def game():

    global game_counter
    # Display the board initialy
    display_board()
    # Player input is checked
    player_input()
    #After player input, game_counter gets a raise
    game_counter += 1


def player_input():
    position = input("Where do want to make your input? (1-9): ")

def check_win():
    #GLobal variable win is called
    global win
    # Horizontal
    if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
        win = True
    elif board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
        win = True
    elif board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
        win = True
    # Vertical
    elif board[6] == board[3] and board[3] == board[0] and board[6] != ' ':
        win = True
    elif board[7] == board[4] and board[4] == board[1] and board[7] != ' ':
        win = True
    elif board[8] == board[5] and board[5] == board[2] and board[8] != ' ':
        win = True
    # Diagonal
    elif board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
        win = True
    elif board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
        win = True
    else:
        win = False
    return win

game()