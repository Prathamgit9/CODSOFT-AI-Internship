def initialize_board():
    return [' ' for _ in range(9)]

def display_board(board):
    for i in range(0, 9, 3):
        row = " | ".join(board[i:i+3])
        print(row)
        if i < 6:
            print("-" * 9)


def check_winner(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def make_ai_move(board):
    best_move = -1
    best_score = -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    while True:  # Replay loop
        board = initialize_board()
        while True:  # Game loop
            display_board(board)
            player_move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= player_move < 9 and board[player_move] == ' ':
                board[player_move] = 'X'
            else:
                print("Invalid move. Try again.")
                continue

            if check_winner(board, 'X'):
                display_board(board)
                print("You win!")
                break

            if ' ' not in board:
                display_board(board)
                print("It's a tie!")
                break

            ai_move = make_ai_move(board)
            board[ai_move] = 'O'

            if check_winner(board, 'O'):
                display_board(board)
                print("AI wins!")
                break

        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
