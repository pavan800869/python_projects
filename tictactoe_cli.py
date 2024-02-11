def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False
        
def draw_board(board):
    for row in board:
        print(' | '.join(row))
        print('-'*9)
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
def get_move():
    while True:
        try:
            move = int(input("Enter a move: "))
            if 1<=move <=9:
                return move
            else:
                print("invalid input")
        except ValueError:
            print("Enter a value between (1-9) ")

        
def tictactoe():
    board = [[' ' for i in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        draw_board(board)
        move = get_move()
        row, col = divmod(move-1, 3)
        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board,player):
                draw_board(board)
                print(f"The {player} wins")
                break
            elif is_board_full(board):
                print(f"The board is full it is a tie")
                draw_board(board)
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("invalid move enter a valid move")

if __name__=="__main__":
    tictactoe()
