
def display_board(board):

    print("")
    print("*************")
    print(f"* {board[6]} | {board[7]} | {board[8]} *")
    print("*-----------*")
    print(f"* {board[3]} | {board[4]} | {board[5]} *")
    print("*-----------*")
    print(f"* {board[0]} | {board[1]} | {board[2]} *")
    print("*************")
    print("")


def player_input():

    position = int(input("Where do want to make your input? (1-9): "))
    position -= 1 # Shift to 0-8 like board numbers
    return position


def check_win(board):

    win = False

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


def play():

    #Play board gets initialized
    board = [' ', ' ', ' ', 
             ' ', ' ', ' ', 
             ' ', ' ', ' ']
    
    # counts the games with win check after 5 and ends with 9 moves
    game_counter = 9

    # Initialising player
    player = ''

    # Display the board initialy
    display_board(board)

    #While loop for counting down the games
    while game_counter > 0:
        # checks by modulo, if player 1 or player 2 is playing
        if game_counter%2 != 0:
            player = 'X'
            print("Player 1 plays")
        else:
            player = 'O'
            print("Player 2 plays")

        #Player input is checked
        position = player_input()
        
        while position < 0 or position > 8:
            display_board(board)
            print("Must be between 1 and 9")
            position = player_input()

        while board[position] != ' ':
            display_board(board)
            print("Can't place over an occupied field\n")
            position = player_input()

        else:
            board[position] = player

        display_board(board)

        # Check for win
        win_bool = check_win(board)

        if game_counter <= 5 and win_bool:
            if game_counter%2 == 0:
                return print("Congratulations. Player 2 won this game")
            else:
                return print("Congratulations. Player 1 won this game")

        #After player input, game_counter gets a count down
        game_counter -= 1
    else:
        print("Game over. It's a tie")

play() # calling the play function to start the game