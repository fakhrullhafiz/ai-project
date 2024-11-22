import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Check if a player has won
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left
        [2, 4, 6],  # Diagonal from top-right
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if the game is a draw
def check_draw(board):
    return all(isinstance(x, str) for x in board)

# Get all available moves on the board
def get_available_moves(board):
    return [i for i, x in enumerate(board) if x != 'X' and x != 'O']

# Depth-First Search function to evaluate game states
def dfs(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth  # Computer wins
    if check_winner(board, 'X'):
        return depth - 10  # Player wins
    if check_draw(board):
        return 0  # Draw

    moves = get_available_moves(board)

    if is_maximizing:
        best_score = float('-inf')
        for move in moves:
            board[move] = 'O'  # Simulate move
            score = dfs(board, depth + 1, False)  # Recur
            board[move] = move  # Undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in moves:
            board[move] = 'X'  # Simulate move
            score = dfs(board, depth + 1, True)  # Recur
            board[move] = move  # Undo move
            best_score = min(best_score, score)
        return best_score

# Function to handle the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in get_available_moves(board):
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to determine the computer's move based on difficulty
def computer_move(board, difficulty):
    if difficulty == 'EASY':
        # Random move
        move = random.choice(get_available_moves(board))
        board[move] = 'O'
    elif difficulty == 'MEDIUM':
        # 50% chance to play optimally, 50% random move
        if random.random() < 0.5:
            move = random.choice(get_available_moves(board))
        else:
            best_score = float('-inf')
            best_moves = []
            for move in get_available_moves(board):
                board[move] = 'O'
                score = dfs(board, 0, False)
                board[move] = move
                if score > best_score:
                    best_score = score
                    best_moves = [move]
                elif score == best_score:
                    best_moves.append(move)
            move = random.choice(best_moves)
        board[move] = 'O'
    else:  # HARD (optimal play)
        best_score = float('-inf')
        best_moves = []
        for move in get_available_moves(board):
            board[move] = 'O'
            score = dfs(board, 0, False)
            board[move] = move
            if score > best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)
        move = random.choice(best_moves)
        board[move] = 'O'

# Main function with difficulty selection
def main():
    print("Welcome to Tic-Tac-Toe!")

    while True:  # Allow multiple games
        board = [i for i in range(9)]  # Initialize the board
        display_board(board)

        # Choose difficulty
        difficulty = ''
        while difficulty not in ['EASY', 'MEDIUM', 'HARD']:
            difficulty = input("Choose difficulty (EASY, MEDIUM, HARD): ").upper()

        # Ask the user if they want to make the first move
        first = ''
        while first not in ['Y', 'N']:
            first = input("Do you want to make the first move? (Y/N): ").upper()

        if first == 'Y':
            player_turn = True
        else:
            player_turn = False

        # Game loop
        while True:
            if player_turn:
                player_move(board)
                display_board(board)
                if check_winner(board, 'X'):
                    print("Congratulations! You win!")
                    break
                player_turn = False
            else:
                print("Computer's turn...")
                computer_move(board, difficulty)
                display_board(board)
                if check_winner(board, 'O'):
                    print("Computer wins!")
                    break
                player_turn = True

            if check_draw(board):
                print("It's a draw!")
                break

        # Ask if the user wants to play again
        play_again = ''
        while play_again not in ['Y', 'N']:
            play_again = input("Do you want to play again? (Y/N): ").upper()

        if play_again == 'N':
            print("Thank you for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    main()
