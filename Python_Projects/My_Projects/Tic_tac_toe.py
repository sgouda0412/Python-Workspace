from IPython.display import clear_output
import random

def display_board(board):
    '''displaying the Tic Tac Toe board'''
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])
    
def player_input():
    '''Assigning a player the X or O marker'''
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input("Please choose either X or O: ").upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def place_marker(board, marker, position):
    '''placing a marker onto the tic tac toe board'''
    board[position] = marker
    
def check_win(board, mark):
    '''checking to see if three markers are played in a row'''
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or # Top row
            (board[4] == mark and board[5] == mark and board[6] == mark) or # middle row
            (board[7] == mark and board[8] == mark and board[9] == mark) or # Bottom row
            (board[1] == mark and board[4] == mark and board[7] == mark) or # Left Column
            (board[2] == mark and board[5] == mark and board[8] == mark) or # Middle column
            (board[3] == mark and board[6] == mark and board[9] == mark) or # Right column
            (board[1] == mark and board[5] == mark and board[9] == mark) or # Top left bottom right
            (board[7] == mark and board[5] == mark and board[3] == mark) # Bottom left top right
           )

def choose_first():
    '''choosing who goes first'''
    choice = random.randint(0, 1)
    
    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    '''Checking to see if a space is empty'''
    return board[position] == ' '

def full_board_check(board):
    '''check each space to see if it is empty. If board is full, returns true'''
    for i in range(1, 10):
        if space_check(board, i):
            return False
    else:
        return True
        
def player_choice(board):
    '''Choosing where to go'''
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Please choose a number between 1-9: "))
    
    return position

def replay():
    '''Asking if player wants to replay'''
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith('y')
        

game_on = True

print("Welcome to Tic Tac Toe! ")

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first!')
    
    play_game = input("Are you ready to play? Yes or No: ")
    
    if play_game.lower()[0] == 'y':
        game_on == True
    else:
        game_on == False
        
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            
            if check_win(the_board, player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a TIE!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("The game is a TIE!")
                    game_on = False
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break

