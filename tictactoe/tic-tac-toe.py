print("ticTacToe")

def get_dimensions():
    return (3,3)

def create_board(rows, columns):
    #board = [[None]*columns]*rows
    return [[None]*columns for row in range(rows)]

def player_choice():
    player_one = input("Please pick a marker 'X' or 'O' ")
    player_two = None
    if player_one == 'X':
        player_two = 'O'
    else:
        player_two = 'X'
        player_one = 'O'
    return (player_one, player_two)

def display_board(board):
    rows, columns = get_dimensions()
    for row in range(rows):
        board_row = ''
        for column in range(columns):
            if column == (columns-1):
                if board[row][column] == None:
                    board_row+='     '
                else:
                    board_row+=f'  {board[row][column]}  '
            else:
                if board[row][column] == None:
                    board_row+='     |'
                else:
                    board_row+=f'  {board[row][column]}  |'
        print(board_row)
        if row == 0 or row == 1:
            print('----- ----- -----')

def player_input():
    return int(input('Please enter a number '))

def get_cordinates(position):
    rows, columns = get_dimensions()
    x = (position-1)/columns
    y = (position-1)%columns
    return (int(x), int(y))


def is_row_completed(board, x, y, value):
    rows, columns = get_dimensions()
    is_row_matched = True
    for column in range(columns):
        if board[x][column] != value:
            is_row_matched = False
            break
    return is_row_matched

def is_column_completed(board, x, y, value):
    rows, columns = get_dimensions()
    is_column_matched = True
    for row in range(rows):
        if board[row][y] != value:
            is_column_matched = False
            break
    return is_column_matched

def is_diagonal_completed(board, value):
    rows, columns = get_dimensions()
    row = 0
    column = 0
    is_diagonal_matched = True
    while row <= rows-1 and column <= columns-1:
        if board[row][column] != value:
            is_diagonal_matched = False
            break
        row+=1
        column+=1

    if not is_diagonal_matched :
        is_diagonal_matched = True
        row = 0
        column = columns-1

        while row <= rows-1 and column >= 0:
            if board[row][column] != value:
                is_diagonal_matched = False
                break
            row+=1
            column-=1

    return is_diagonal_matched

def is_game_over(board, cordinate):
    rows, columns = get_dimensions()
    is_game_over = False
    if cordinate != None:
        x = cordinate[0]
        y = cordinate[1]
        value = board[x][y]

        is_row_matched = is_row_completed(board, x, y, value)
        is_column_matched = is_column_completed(board, x, y, value)
        if (x == 0 and (y == 0 or y == columns-1)) or (x == rows-1 and (y == 0 or y == columns-1)) or (x == y):
            is_diagonal_matched = is_diagonal_completed(board, value)
            is_game_over = is_row_matched or is_column_matched or is_diagonal_matched
        else:
            is_game_over = is_row_matched or is_column_matched
        if is_game_over:
            print(f'player with {value} won!!')
    return is_game_over

def is_space_present(board):
    is_space_present = any(None in x for x in board)
    if not is_space_present:
        print('Game over its a TIE')
    return is_space_present

def play():

    rows, columns = get_dimensions()
    board = create_board(rows, columns)
    player_one, player_two = player_choice()

    is_player_one_chance = True
    cordinate = None
    while True and not is_game_over(board, cordinate) and is_space_present(board):
        position = player_input()

        if position <= rows*columns and position > 0:
            if is_player_one_chance:
                cordinate = get_cordinates(position)
                board[cordinate[0]][cordinate[1]] = player_one
            else:
                cordinate = get_cordinates(position)
                board[cordinate[0]][cordinate[1]] = player_two
            is_player_one_chance = not is_player_one_chance
            display_board(board)
        else:
            print(f'Please enter number from 1 to {rows*columns}')
play()
