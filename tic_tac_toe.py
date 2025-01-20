# Tic Tac Toe Game in Python

# Display the board
def display_board(board):
    for row in range(0, 9, 3):
        print(board[row] + "|" + board[row + 1] + "|" + board[row + 2])
        if row < 6:
            print("-+-+-")

# Check if there's a winner
def check_winner(board, mark):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == mark for i in combo) for combo in win_combinations)

# Main game function
def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    turns = 0

    while turns < 9:
        display_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] != " " or move < 0 or move > 8:
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Enter a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player
        turns += 1

        # Check for winner
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()
