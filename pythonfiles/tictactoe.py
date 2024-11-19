def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {turn}, enter the row (0-2): "))
        col = int(input(f"Player {turn}, enter the column (0-2): "))
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = turn
        if check_win(board, turn):
            print_board(board)
            print(f"Player {turn} wins!")
            return
        turn = "O" if turn == "X" else "X"
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()
