def play():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    numbers = {
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2)
    }
    winner = False
    turn = 'X'
    nums = [num for num in range(1, 10)]

    print("Type 'Go' to start.")
    start = input()
    while start != 'Go':
        print("Type 'Go' to start.")
        start = input()

    while winner == False:
        print(f"{turn}'s turn. Enter 1-9")
        current = input()
        while current not in numbers or board[numbers[current][0]][numbers[current][1]] != ' ':
            print_board(board)
            print('Incorrect input!')
            current = input()
        new_board(turn, board, numbers[current])
        if check_winner(board):
            print_board(board)
            print(f'{turn} is the winner!')
            print('Play again? Yes/No')
            again = input()
            while again != 'Yes' and again != 'No':
                print('Play again? Yes/No')
                again = input()
            if again == 'Yes':
                reset_game()
                return
            else:
                return None
        elif draw_check(board):
            print_board(board)
            print('Draw!')
            print('Play again? Yes/No')
            again = input()
            while again != 'Yes' and again != 'No':
                print('Play again? Yes/No')
                again = input()
            if again == 'Yes': reset_game()
            else: break
        print_board(board)
        if turn == 'X': turn = 'O'
        else: turn = 'X'

    return None

def new_board(turn, board, tile):
    board[tile[0]][tile[1]] = turn

    return board

def print_board(board):
    print('   |   |   ')
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
    print('   |   |   ')

def check_winner(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return True
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
    return False

def draw_check(board):
    if (board[0][0] != ' ' and
        board[0][1] != ' ' and
        board[0][2] != ' ' and
        board[1][0] != ' ' and
        board[1][1] != ' ' and
        board[1][2] != ' ' and
        board[2][0] != ' ' and
        board[2][1] != ' ' and
        board[2][2] != ' '):
        return True

def reset_game():
    play()
    return None

play()
