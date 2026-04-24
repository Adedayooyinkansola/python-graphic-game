import random

# Initialize the board
board = ['1','2','3','4','5','6','7','8','9']

# Winning combinations
wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print("\n")

def check_winner(player):
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_tie():
    return all(cell in ['X', 'O'] for cell in board)

def get_available_moves():
    return [i for i in range(9) if board[i] not in ['X', 'O']]

# Computer starts in the center
board[4] = 'X'

while True:
    print_board()

    # User move
    try:
        move = int(input("Enter your move (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] in ['X', 'O']:
            print("Invalid move. Try again.")
            continue
        board[move] = 'O'
    except ValueError:
        print("Please enter a number.")
        continue

    if check_winner('O'):
        print_board()
        print("You win!")
        break
    if is_tie():
        print_board()
        print("It's a tie!")
        break

    # Computer move
    comp_move = random.choice(get_available_moves())
    board[comp_move] = 'X'
    print(f"Computer chose position {comp_move + 1}")

    if check_winner('X'):
        print_board()
        print("Computer wins!")
        break
    if is_tie():
        print_board()
        print("It's a tie!")
        break
