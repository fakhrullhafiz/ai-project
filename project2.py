# Tic-Tac-Toe Game using Minimax Algorithm

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

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

def check_draw(board):
    return all(isinstance(x, str) for x in board)

def get_available_moves(board):
    return [i for i, x in enumerate(board) if x != 'X' and x != 'O']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return depth - 10
    if check_draw(board):
        return 0

    moves = get_available_moves(board)

    if is_maximizing:
        best_score = float('-inf')
        for move in moves:
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = move  # Undo move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in moves:
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = move  # Undo move
            best_score = min(best_score, score)
        return best_score

def computer_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = move  # Undo move
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

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

def main():
    print("Welcome to Tic-Tac-Toe!")
    board = [i for i in range(9)]
    display_board(board)

    first = ''
    while first not in ['Y', 'N']:
        first = input("Do you want to make the first move? (Y/N): ").upper()

    if first == 'Y':
        player_turn = True
    else:
        player_turn = False

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
            computer_move(board)
            display_board(board)
            if check_winner(board, 'O'):
                print("Computer wins!")
                break
            player_turn = True

        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
