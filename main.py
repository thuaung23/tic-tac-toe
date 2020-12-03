# This is a simple Tic Tac Toe game for two players.
# Written by: Thu Aung
# Written on: Sept 10, 2020

# Display the board.
def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

# Assign X or O by asking player 1 to choose.
def player_input():
    marker = ''
    while marker != 'X' or marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
        elif marker == 'O':
            return ('O', 'X')
        else:
            continue

# Mark the place chosen by player earlier.
def place_marker(board, marker, position):
    board[position] = marker

# Check if either player met any of win conditions.
def win_check(board, mark):
    return (# Horizontal Win Conditions
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            # Vertical Win Conditions
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            # Diagonal Win Conditions
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

# Decide who will go first.
import random
def player_turn():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Check the board for empty spaces
def space_check(board, position):
    return board[position] == ' '

# Check if the board is full.
def full_board_check(board):
    for x in range(1,10):
        if space_check(board, x):
            return False
    return True

# Ask players for their next move.
def player_next_move(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] and not  space_check(board, position):
        position = int(input('Please choose your next position (1-9): '))
    return position

# Ask players if they want to play again.
def play_again():
    return input('Do you want to play again? Y or N: ').lower().startswith('y')

print('Welcome to the game of Tic Tac Toe.')

while True:
    # Set up the game
    theboard = [' '] * 10
    # Unpack tuple and assign items to respective player.
    player1_marker, player2_marker = player_input()
    turn = player_turn()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Y or N: ')
    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        # Player 1
        if turn == 'Player 1':
            display_board(theboard)
            position = player_next_move(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('Congratulations! You\'ve won the game.')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("This game is a draw.")
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player 2
            display_board(theboard)
            position = player_next_move(theboard)
            place_marker(theboard,player2_marker,position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Congratulaitons! You\'ve won the game.')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw.')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break