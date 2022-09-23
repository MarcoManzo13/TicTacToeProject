board = {  #Create a dictionary in which the board is located. T = Top, M = Mid, D = Down
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' ',
}

player = 1  # To initialize the first player
total_moves = 0 # Should no exceed 9 moves.
end_check = 0 # To check if someone won

def check(): # Create a function that checks the winning conditions.
    # Checking the moves of player one
    # For horizontal check of winning (start)
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('Player 1 won !')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player 1 won !')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('Player 1 won !')
        return 1
    # Horizontal check (end)
    # Check diagonal win (start)
    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('Player 1 won !')
        return 1
    # Diagonal check (end)
    # Vertical Win (start)
    if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print('Player 1 won !')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('Player 1 won !')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('Player 1 won !')
        return 1
    # Vertical win (end)
    
    # Checking the moves of player two
    # For horizontal check of winning (start)
    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print('Player 2 won !')
        return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        print('Player 2 won !')
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print('Player 2 won !')
        return 1
    # Horizontal check (end)
    # Check diagonal win (start)
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print('Player 2 won !')
        return 1
    # Diagonal check (end)
    # Vertical Win (start)
    if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
        print('Player 2 won !')
        return 1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
        print('Player 2 won !')
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print('Player 2 won !')
        return 1
    # Vertical win (end)
    return 0 # If check fails

print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print('*****************')

while True:
    print(board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('-+-+-')
    print(board['M1']+'|'+board['M2']+'|'+board['M3'])
    print('-+-+-')
    print(board['D1']+'|'+board['D2']+'|'+board['D3'])
    end_check = check() # To store the return value in end_check
    if total_moves == 9 or end_check == 1:  # To stop the loop if the moves are equal to 9, the maximum number of moves in a tiktaktoe game. To check also if someone won
        break
    while True: # Loop to take input from the players
        if player == 1: # choose player
            p1_input = input('Player one: ') # Getting the input from the player 1
            if p1_input.upper() in board and board[p1_input.upper()] == ' ': # Check if the input is a valid key
                board[p1_input.upper()] = 'X'  # Add the X from the player 1 into the board
                player = 2 # Change into player 2
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('Player two: ') # Getting the input from the player 2
            if p2_input.upper() in board and board[p2_input.upper()] == ' ': # Check if the input is a valid key
                board[p2_input.upper()] = 'O'  # Add the X from the player 1 into the board
                player = 1 # Change into player 1 again
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
    total_moves += 1 # Add to the counter of the total moves
    print('***************************')
    print()
